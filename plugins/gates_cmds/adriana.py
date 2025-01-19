from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import (
    anti_bots_telegram,
    get_bin_info,
    get_cc,
    antispam,
    get_text_from_pyrogram,
    user_not_premium,
)
from utilsdf.vars import PREFIXES
from gates.hinata import hinata
from time import perf_counter


@Client.on_message(filters.command("hn", PREFIXES))
async def hn(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_premium(user_id):
            await user_not_premium(m)
            return
        user_info = db.get_info_user(user_id)
        is_free_user = user_info["MEMBERSHIP"]
        is_free_user = is_free_user.lower() == "free user"
        if is_free_user:
            captcha = await anti_bots_telegram(m, client)
            if not captcha:
                return
    text = get_text_from_pyrogram(m)
    ccs = get_cc(text)
    if not ccs:
        return await m.reply(
            "𝙂𝙖𝙩𝙚𝙬𝙖𝙮 <code>𝙃𝙞𝙣𝙖𝙩𝙖 ♻️ -» $20</code>\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/hn cc|month|year|cvc</code>",
            quote=True,
        )
    ini = perf_counter()
    cc = ccs[0]
    mes = ccs[1]
    ano = ccs[2]
    cvv = ccs[3]

    # check antispam
    antispam_result = antispam(user_id, user_info["ANTISPAM"], is_free_user)
    if antispam_result != False:
        return await m.reply(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
        )
    msg = await m.reply("𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...", quote=True)
    cc_formatted = f"{cc}|{mes}|{ano}|{cvv}"

    status, response = await hinata(cc, mes, ano, cvv)

    # Bin information lookup
    bin_info = await get_bin_info(cc)
    issuer = bin_info.get("issuer", "Unknown")
    country = bin_info.get("country", "Unknown")
    gateway = "𝗔𝗱𝗿𝗶𝗮𝗻𝗮"  # Custom gateway name
    bin_website = f"https://binlist.net/?bin={cc[:6]}"  # Example of bin lookup website link

    final = perf_counter() - ini
    with Database() as db:
        db.increase_checks(user_id)

    if "Approved" in status:
        text_ = f"""𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅

𝗖𝗮𝗿𝗱: {cc_formatted}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gateway}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response}

𝗜𝗻𝗳𝗼: {bin_info.get("type", "Unknown")} - {bin_info.get("category", "Unknown")} - {bin_info.get("brand", "Unknown")}
𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country} 

𝗧𝗶𝗺𝗲: {final:0.2} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬

𝗕𝗶𝗻 𝗜𝗻𝗳𝗼: <a href='{bin_website}'>Click here for Bin Info</a>

ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>"""
    else:
        text_ = f"""𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌

𝗖𝗮𝗿𝗱: {cc_formatted}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gateway}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response}

𝗜𝗻𝗳𝗼: {bin_info.get("type", "Unknown")} - {bin_info.get("category", "Unknown")} - {bin_info.get("brand", "Unknown")}
𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country} 

𝗧𝗶𝗺𝗲: {final:0.2} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬

𝗕𝗶𝗻 𝗜𝗻𝗳𝗼: <a href='{bin_website}'>Click here for Bin Info</a>

ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>"""

    await msg.edit(text_)
    
