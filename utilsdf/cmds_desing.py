from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utilsdf.functions import symbol

text_home = """𝙒𝙚𝙡𝙘𝙤𝙢𝙚 »
<code>This bot promises you fast and safe checkups with different gateways and perfect tools for your use! ✨</code>
                  
<a href='tg://user?id={}'>朱 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 </a> -» <code>1.3</code>"""

#exit_button = InlineKeyboardButton("𝙀𝙭𝙞𝙩 ⚠️", "exit")

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
        [InlineKeyboardButton("Premium 🛒", "premium")],
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
return_home_and_exit = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "home")],
        [exit_button],
    ]
)


# GATES AUTH

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
        [InlineKeyboardButton("↩️", "home")],
    ]
)

# GATES CHARGED

text_gates_charged = f"""
Charged Gateway 💰

<code>PayPal -» $0.01</code>
<code>.pp</code> -» <code>Free</code>
<code>On ✅</code>

<code>PayPal -» $1</code>
<code>.ppa</code> -» <code>Free</code>
<code>On ✅</code>

<code>SquareUp -» $10</code>
<code>.gh</code> -» <code>Premium</code>
<code>On ✅</code>

<code>Onrally + Braintree -» $28.99</code>
<code>.chk</code> -» <code>Premium</code>
<code>On ✅</code>

<code>Stripe[Ccn] -» $1</code>
<code>.or</code> -» <code>Premium</code>
<code>On ✅</code>

<code>Stripe[Ccn] -» $26.29</code>
<code>.bo</code> -» <code>Premium</code>
<code>On ✅</code>
"""
buttons_charged_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "home")],
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
        [InlineKeyboardButton("↩️", "home")],
    ]
)

text_premium = f"""🌟 Introducing Premium Subscriptions!

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

buttons_premium_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "home")],
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

{<code>generate address</code>
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
