from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utilsdf.functions import symbol

text_home = """𝙒𝙚𝙡𝙘𝙤𝙢𝙚 »
<code>This bot promises you fast and safe checkups with different gateways and perfect tools for your use! ✨</code>
                  
<a href='tg://user?id={}'>朱 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 </a> -» <code>1.3</code>"""

exit_button = InlineKeyboardButton("𝙀𝙭𝙞𝙩 ⚠️", "exit")

buttons_cmds = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝙂𝙖𝙩𝙚𝙨 ♻️", "gates"),
            InlineKeyboardButton("𝙏𝙤𝙤𝙡𝙨 🛠", "tools"),
        ],
        [InlineKeyboardButton("𝘾𝙝𝙖𝙣𝙣𝙚𝙡 💫", url="https://t.me/GarryPlays")],
        [exit_button],
    ]
)

buttons_gates = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝘼𝙪𝙩𝙝 ", "auths"),
            InlineKeyboardButton("𝘾𝙝𝙖𝙧𝙜𝙚𝙙 ", "chargeds"),
        ],
        [InlineKeyboardButton("𝙎𝙥𝙚𝙘𝙞𝙖𝙡 ", "specials")],
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
        [exit_button],
    ]
)


# RETURN & EXIT GATES
return_and_exit_gates = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "gates")],
        [exit_button],
    ]
)

# RETURN HOME & EXIT
return_home_and_exit = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
        [exit_button],
    ]
)

text_auth_stripe = f"""
🔐 **Stripe Authentication**  
Ensures valid card details for Stripe payment processing.  

🔧 **Usage**  
**Command:** `/chk_stripe`  
**Example:** `/chk_stripe 4833160215879047|07|2026|819`  
"""

buttons_auth_stripe = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_paypal = f"""
🔐 **PayPal Authentication**  
Verifies card validity for transactions on PayPal.

🔧 **Usage**  
**Command:** `/chk_paypal`  
**Example:** `/chk_paypal 4833160215879047|07|2026|819`  
"""

buttons_auth_paypal = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_braintree = f"""
🔐 **Braintree Authentication**  
Validates card data for Braintree payment processing.

🔧 **Usage**  
**Command:** `/chk_braintree`  
**Example:** `/chk_braintree 4833160215879047|07|2026|819`  
"""

buttons_auth_braintree = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_squareup = f"""
🔐 **SquareUp Authentication**  
Authenticates card details for SquareUp transactions.

🔧 **Usage**  
**Command:** `/chk_squareup`  
**Example:** `/chk_squareup 4833160215879047|07|2026|819`  
"""

buttons_auth_squareup = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_shopify = f"""
🔐 **Shopify Authentication**  
Checks card information for Shopify payments.

🔧 **Usage**  
**Command:** `/chk_shopify`  
**Example:** `/chk_shopify 4833160215879047|07|2026|819`  
"""

buttons_auth_shopify = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_authorizenet = f"""
🔐 **Authorize.Net Authentication**  
Validates card details for Authorize.Net payments.

🔧 **Usage**  
**Command:** `/chk_authorizenet`  
**Example:** `/chk_authorizenet 4833160215879047|07|2026|819`  
"""

buttons_auth_authorizenet = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_worldpay = f"""
🔐 **Worldpay Authentication**  
Ensures card validity for Worldpay transactions.

🔧 **Usage**  
**Command:** `/chk_worldpay`  
**Example:** `/chk_worldpay 4833160215879047|07|2026|819`  
"""

buttons_auth_worldpay = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)

text_auth_payflow = f"""
🔐 **Payflow Authentication**  
Verifies card details for Payflow gateways.

🔧 **Usage**  
**Command:** `/chk_payflow`  
**Example:** `/chk_payflow 4833160215879047|07|2026|819`  
"""

buttons_auth_payflow = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Return to Gates Auth", "gates_auth")]]
)


# GATES AUTH

text_gates_auth = f"""
🔐 **Auth Gates**
Verifies the card's validity and ensures that the data matches the information on file with the issuing bank for that card.

🔧 **Usage**  
**Format:** `[command] CC|MM|YYYY|CVV`  
**Example:** `/chk 4833160215879047|07|2026|819`
"""

buttons_gates_auth = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("1️⃣ Stripe", "auth_stripe"),
            InlineKeyboardButton("2️⃣ PayPal", "auth_paypal"),
        ],
        [
            InlineKeyboardButton("3️⃣ Braintree", "auth_braintree"),
            InlineKeyboardButton("4️⃣ SquareUp", "auth_squareup"),
        ],
        [
            InlineKeyboardButton("5️⃣ Shopify", "auth_shopify"),
            InlineKeyboardButton("6️⃣ Authorize.Net", "auth_authorizenet"),
        ],
        [
            InlineKeyboardButton("7️⃣ Worldpay", "auth_worldpay"),
            InlineKeyboardButton("8️⃣ Payflow", "auth_payflow"),
        ],
        [InlineKeyboardButton("🔙 Return", "home")],
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
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

# GATES SPECIALS
text_gates_especials = f"""𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝙎𝙥𝙚𝙘𝙞𝙖𝙡

{symbol("朱 𝙊𝙧𝙤𝙘𝙝𝙞𝙢𝙖𝙧𝙪")} -» <code>Stripe[Ccn] -» $1</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.or</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙤𝙧𝙪𝙩𝙤")} -» <code>Stripe[Ccn] -» $26.29</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.bo</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>
"""
buttons_specials_page_1 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚𝙩𝙪𝙧𝙣 🔄", "home")],
    ]
)

# TOOLS
text_tools = f"""
𝙏𝙤𝙤𝙡𝙨 🛠

{symbol("朱 𝙍𝙚𝙛𝙚")} -» <code>send review reference</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.refe -» reply message</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘽𝙞𝙣")} -» <code>info bin</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.bin</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘾𝙝𝙖𝙩 𝙂𝙋𝙏")} -» <code>ChatGPT</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gpt hola</code> -» <code>Premium</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘼𝙙𝙙𝙧𝙚𝙨𝙨")} -» <code>generate address</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.rnd us</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙎𝙠")} -» <code>info sk</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.sk</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙂𝘽𝙞𝙣")} -» <code>generate bins</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gbin</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝘾𝘾 𝙂𝙚𝙣")} -» <code>generate ccs</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.gen</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙄𝙣𝙛𝙤")} -» <code>info user</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.my</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙡𝙖𝙣")} -» <code>info plan user</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.plan</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>

{symbol("朱 𝙋𝙡𝙖𝙣𝙂")} -» <code>info plan group</code>
{symbol("零 𝘾𝙢𝙙")} -» <code>.plang</code> -» <code>Free</code>
{symbol("ᥫ᭡ 𝙎𝙩𝙖𝙩𝙪𝙨")} -» <code>On ✅</code>"""
