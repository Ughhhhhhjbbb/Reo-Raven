from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from utilsdf.functions import symbol

# Bot start text
start_text = """🤖 Bot Status: Active ✅

📢 For announcements and updates, join us 👉 [here](https://t.me/your_channel_link).

💡 Tip: To use Raven in your group, make sure to set it as an admin.
"""

# Main menu text
main_menu_text = """❓ How can I assist you today?

🌟 Stay updated for the latest features and improvements!

💎 Upgrade to Premium for exclusive benefits.
"""

# CC Killer gate text
cc_killer_text = """💣 **CC Killer Gates**  
                        
Under development, coming soon!⌛️  

Kill a specific card.  

**Command**:  
`/kill CARD_NUMBER | EXP_DATE | CVV`  

**Example**:  
`/kill 4647...6215|11|2024|630`  
"""

# Premium page text
premium_text = """💎 **Premium Membership**

Upgrade to Premium for exclusive benefits, faster services, and priority support.

👑 **Owner/Admin**: [@Reo_47](https://t.me/Reo_47)  
📢 **Updates Channel**: [@blitzupdate](https://t.me/blitzupdate)

To purchase or inquire about Premium, contact the owner directly.  
"""

# Inline buttons
buttons_start = InlineKeyboardMarkup(
    [[InlineKeyboardButton("📝 Menu", callback_data="menu")]]
)

buttons_main_menu = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🔐 Auth", callback_data="auth")],
        [InlineKeyboardButton("💎 Premium", callback_data="premium")],
        [InlineKeyboardButton("⚙️ Other", callback_data="other")],
        [InlineKeyboardButton("💣 CC Killer", callback_data="cc_killer")],
    ]
)

buttons_back_to_menu = InlineKeyboardMarkup(
    [[InlineKeyboardButton("⬅️ Back", callback_data="menu")]]
)

auth_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Adr", callback_data="auth_adr"),
            InlineKeyboardButton("Ak", callback_data="auth_ak"),
        ],
        [
            InlineKeyboardButton("Ass", callback_data="auth_ass"),
            InlineKeyboardButton("At", callback_data="auth_at"),
        ],
        [
            InlineKeyboardButton("Bo", callback_data="auth_bo"),
            InlineKeyboardButton("Br", callback_data="auth_br"),
        ],
        # Add additional auth buttons here
        [InlineKeyboardButton("⬅️ Back", callback_data="menu")],
    ]
)

@Client.on_callback_query()
async def handle_callback_query(client, query: CallbackQuery):
    if query.data == "menu":
        await query.message.edit_text(
            text=main_menu_text,
            reply_markup=buttons_main_menu
        )
    elif query.data == "auth":
        await query.message.edit_text(
            text="🔐 Choose an Auth Option:",
            reply_markup=auth_menu
        )
    elif query.data == "premium":
        await query.message.edit_text(
            text=premium_text,
            reply_markup=buttons_back_to_menu,
            disable_web_page_preview=True
        )
    elif query.data == "cc_killer":
        await query.message.edit_text(
            text=cc_killer_text,
            reply_markup=buttons_back_to_menu,
            disable_web_page_preview=True
        )
    elif query.data.startswith("auth_"):
        auth_name = query.data.split("_")[1].upper()
        await query.message.edit_text(
            text=f"🔑 **{auth_name} Command**\n\nThis is the description and usage information for `{auth_name}`.",
            reply_markup=buttons_back_to_menu
        )
    else:
        await query.answer("Feature coming soon!", show_alert=True)

@Client.on_message()
async def handle_start(client, message):
    await message.reply(
        text=start_text,
        reply_markup=buttons_start,
        disable_web_page_preview=True
    )
