from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utilsdf.functions import symbol

text_home = """
🤖 Bot Status: Active ✅

📢 For announcements and updates, join us 👉 @blitzupdate

💡 Tip: To use Raven in your group, make sure to set it as an admin."""

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
text_gates_auth = f"""
🔐 Auth Gate

Braintree
<code>/chk</code> -» Free
On ✅

Shopify
<code>/sh</code> -» Free
On ✅

Adyne
<code>/ad</code> -» Free
On ✅

CyberSource
<code>/cc</code> -» Free
On ✅

PayPal
<code>/pp</code> -» Free
On ✅

Stripe
<code>/rh</code> -» Free
On ✅

3D Secure VBV
<code>/Vbv</code> -» Free
On ✅
"""

buttons_auth_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)


# GATES CHARGED
text_charge_gates = """
💰 Charge Gates
Initiates a charge on the card by deducting the specified amount from the cardholder's account.

🔧 Usage
Format: `[command] CC|MM|YYYY|CVV`
Example: <code>/dx</code> <code>5154620014869257|04|2026|447</code>

Ensure the card details provided are correct and the transaction is authorized.
"""

buttons_charged_page_1 = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton("Braintree", "specials_3"),
            InlineKeyboardButton("Shopify", "chargeds_2"),
        ],
        [
            InlineKeyboardButton("PayPal Pro ", "chargeds_3"),
            InlineKeyboardButton("Squre", "chargeds_4"),
        ],
        [
            InlineKeyboardButton("CyberSource", "chargeds_5"),
            InlineKeyboardButton("Adyen", "chargeds_6"),
        ],
        
        [InlineKeyboardButton("⬅️", "gates")],  # Update callback data to 'charged_back'
        [exit_button],
    ]
)

text_gates_charged_2 =  f"""
Braintree

- Command: <code>/dx</code>
- ✅ Active | 📅 1/20/25
- $10.0 Charge
- 10 Credit
"""


buttons_charged_page_2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)

text_gates_charged_3 =  f"""
Shopify

- Command: <code>/br</code>
- ✅ Active | 📅 1/20/25
- $0.1 Charge
- 1 Credit
"""


buttons_charged_page_3 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)

text_gates_charged_4 =  f"""
Squre

- Command: <code>/gh</code>
- ✅ Active | 📅 1/20/25
- $10.0 Charge
- 10 Credit
"""


buttons_charged_page_4 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)

text_gates_charged_5  =  f"""
CyberSource

- Command: <code>/bo</code>
- ✅ Active | 📅 1/20/25
- $28.29 Charge
- 25 Credit
"""


buttons_charged_page_5 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)   
text_gates_charged_6 =  f"""
Adyen

- Command: <code>/dkt</code>
- ✅ Active | 📅 1/20/25
- $1.00 Charge
- 1 Credit
"""


buttons_charged_page_6 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
    ]
)

text_gates_especials_3 =  f"""
PayPal Pro

- Command: <code>/ppa</code>
- ✅ Active | 📅 1/20/25
- $1.00 Charge
- 1 Credit
"""


buttons_specials_page_3 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("↩️", "gates")],
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
