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
from gates.ass import ass
from time import perf_counter


@Client.on_message(filters.command("vbv", PREFIXES))
async def ass_(client: Client, m: Message):
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
            "𝙂𝙖𝙩𝙚𝙬𝙖𝙮 <code>𝙑𝙗𝙫 ♻️</code>\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/vbv cc|month|year|cvc</code>",
            quote=True,
        )
    ini = perf_counter()
    cc = ccs[0]
    mes = ccs[1]
    ano = ccs[2]
    cvv = ccs[3]

    # Extract BIN (first 6 digits of CC)
    bin_number = cc[:6]

    # Fetch BIN information
    bin_info = await get_bin_info(bin_number)
    if not bin_info:
        bin_info_text = "Unable to fetch BIN information."
    else:
        bin_info_text = f"""𝗜𝗻𝗳𝗼:
𝐈𝐬𝐬𝐮𝐞𝐫: {bin_info.get("issuer", "N/A")}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {bin_info.get("country", "N/A")}"""

    # Check antispam
    antispam_result = antispam(user_id, user_info["ANTISPAM"], is_free_user)
    if antispam_result != False:
        return await m.reply(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
        )
    msg = await m.reply("𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...", quote=True)
    cc_formatted = f"{cc}|{mes}|{ano}|{cvv}"

    status, response, vbv = await ass(cc, mes, ano, cvv)

    final = perf_counter() - ini
    with Database() as db:
        db.increase_checks(user_id)

    text_ = f"""<b>{status}

𝗖𝗮𝗿𝗱: <code>{cc_formatted}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: 3DS Lookup
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {vbv}

{bin_info_text}

𝗧𝗶𝗺𝗲: <code>{final:0.3}'s</code></b>"""

    await msg.edit(text_)
