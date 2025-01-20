from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utilsdf.functions import symbol

text_home = """𝙒𝙚𝙡𝙘𝙤𝙢𝙚 »
<code>This bot promises you fast and safe checkups with different gateways and perfect tools for your use! ✨</code>
                  
<a href='tg://user?id={}'>朱 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 </a> -» <code>1.3</code>"""

exit_button = InlineKeyboardButton("𝙀𝙭𝙞𝙩 ⚠️", "exit")

buttons_cmds = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Menu 🔍", "gates")],
    ]
)


buttons_gates = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔐 Auth Gate", "auths"),
            InlineKeyboardButton("💰 Charge Gate", "chargeds"),
        ],
        [
            InlineKeyboardButton("💣 CC Killer Gates (soon)", "specials"),
            InlineKeyboardButton("🛠 Other Cmands", "tools"),
        ],
        [
            InlineKeyboardButton("💤 Soon", "soon"),
            InlineKeyboardButton("💤 Soon", "soon"),
        ],
        [InlineKeyboardButton("Premium 🛒", "specials_2")],
    ]
)



# RETURN & EXIT GATES
return_and_exit_gates = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
        [exit_button],
    ]
)

# RETURN HOME & EXIT
return_homae_and_exit = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "home")],
        [exit_button],
    ]
)


# GATES AUTH

# Define PayPal buttons in a 2x2 layout
paypal_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("PayPal 1", "paypal_1"),
            InlineKeyboardButton("PayPal 2", "paypal_2"),
        ],
        [
            InlineKeyboardButton("PayPal 3", "paypal_3"),
            InlineKeyboardButton("PayPal 4", "paypal_4"),
        ],
        [
            InlineKeyboardButton("PayPal 5", "paypal_5"),
            InlineKeyboardButton("PayPal 6", "paypal_6"),
        ],
        [
            InlineKeyboardButton("PayPal 7", "paypal_7"),
            InlineKeyboardButton("PayPal 8", "paypal_8"),
        ],
        [
            InlineKeyboardButton("PayPal 9", "paypal_9"),
            InlineKeyboardButton("PayPal 10", "paypal_10"),
        ],
        [InlineKeyboardButton("⬅️ Back", "chargeds")],  # Centered Back Button
    ]
)





text_gates_auth = f"""
𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝

<code>Shopify -» Auth</code>
<code>.od</code> -» <code>Premium</code>
<code>On ✅</code>

<code>Payflow Avs codes -» Auth</code>
<code>.it</code> -» <code>Premium</code>
<code>On ✅</code>
"""

buttons_auth_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)

# GATES CHARGED
text_gates_charged = f"""
𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙

𝙋𝙖𝙜 -» <code>1</code>

{symbol("朱 𝙋𝙖𝙮𝙋𝙖𝙡")} -» <code>PayPal -» $0.01</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.pp</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙖𝙮𝙋𝙖𝙡")} -» <code>PayPal -» $1</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.ppa</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙂𝙝𝙤𝙪𝙡")} -» <code>SquareUp -» $10</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gh</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙧𝙚𝙣𝙙𝙖 ")} -» <code>Onrally + Braintree -» $28.99</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.br</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""
buttons_charged_page_1 = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton("PayPal 1", "paypal_1"),
            InlineKeyboardButton("PayPal 2", "paypal_2"),
        ],
        [
            InlineKeyboardButton("PayPal 3", "paypal_3"),
            InlineKeyboardButton("PayPal 4", "paypal_4"),
        ],
        [
            InlineKeyboardButton("PayPal 5", "paypal_5"),
            InlineKeyboardButton("PayPal 6", "paypal_6"),
        ],
        [
            InlineKeyboardButton("PayPal 7", "paypal_7"),
            InlineKeyboardButton("PayPal 8", "paypal_8"),
        ],
        [
            InlineKeyboardButton("PayPal 9", "paypal_9"),
            InlineKeyboardButton("PayPal 10", "paypal_10"),
        ],
        [InlineKeyboardButton("⬅️ Back", "gates")],  # Centered Back Button
    ]
)

# GATES SPECIALS
text_gates_especials = f"""💣 CC Killer Gates

Under development, coming soon!⌛️

Kill a specific card.

Command: <code>/kill CARD_NUMBER | EXP_DATE | CVV</code>
Example: <code>/kill 4647...6215|11|2024|630</code>

"""
buttons_specials_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)

text_gates_especials_2 = f"""🌟 Introducing Premium Subscriptions!

❓ Why Choose Premium?

• Unlimited Access: Unlock all commands without restrictions!
• Seamless Experience: No more Anti-Spam or hourly limits.
• Priority Support: Get quick assistance whenever you need it.

🛡️ About Credits: Charge Gates require credits to use. If you run out, you can still access Auth Gates, which don’t need credits, or you can recharge for full access again.

ℹ️ Note: After purchasing, you will receive a serial key. Please check your email to find your serial key and redeem it using the command:

/redeem XXXX-XXXX-XXXX-XXXX

⚠️ Important: Make sure to pay the exact indicated amount within the given timeframe as we're not responsible for any losses of funds.

Enjoy a better experience with our service. Upgrade now! 🚀 Click the button below to upgrade to Premium. 👇

"""

buttons_specials_page_2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
        [exit_button],
    ]
)
# TOOLS
text_tools = f"""
𝙏𝙤𝙤𝙡𝙨 🛠

<code>send review reference</code>
<code>.refe -» reply message</code> -» <code>Free</code>
<code>On ✅</code>

<code>info bin</code>
<code>.bin</code> -» <code>Free</code>
<code>On ✅</code>

<code>ChatGPT</code>
<code>.gpt hola</code> -» <code>Premium</code>
<code>On ✅</code>

<code>generate address</code>
<code>.rnd us</code> -» <code>Free</code>
<code>On ✅</code>

<code>info sk</code>
<code>.sk</code> -» <code>Free</code>
<code>On ✅</code>

<code>generate bins</code>
<code>.gbin</code> -» <code>Free</code>
<code>On ✅</code>

<code>generate ccs</code>
<code>.gen</code> -» <code>Free</code>
<code>On ✅</code>

<code>info user</code>
<code>.my</code> -» <code>Free</code>
<code>On ✅</code>

<code>info plan user</code>
<code>.plan</code> -» <code>Free</code>
<code>On ✅</code>

<code>info plan group</code>
l<code>.plang</code> -» <code>Free</code>
<code>On ✅</code>"""
