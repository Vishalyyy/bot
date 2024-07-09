import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Define the bot token (replace with your actual bot token)
BOT_TOKEN = '6936159316:AAFby_fH3iAa-zSiEk3TYTOD5NMxo7j2Aqg'

# Define the channels that users must join
REQUIRED_CHANNELS = [
    {"name": "Channel 1", "url": "https://t.me/everycookies"},
    {"name": "Channel 2", "url": "https://t.me/pslifafa"},
    {"name": "Channel 3", "url": "https://t.me/+Rkp_uJG9aeU3ODA1"},
    {"name": "Channel 4", "url": "https://t.me/cyberlearnhub"},
    {"name": "Channel 5", "url": "https://t.me/+vrj6OzPQwbZmMGJl"},
    {"name": "Channel 6", "url": "https://t.me/addlist/1rPJCoTSkrg5NTZl"},
    {"name": "Channel 7", "url": "https://t.me/Hacking_WOULD"}
]

# Course source links
COURSE_SOURCES = [
    {"name": "Wifi Hacking", "link": "https://drive.google.com/drive/u/0/mobile/folders/1tgkKt4lSpXD3GnMQRgUb4bbtlmpP9XOE"},
    {"name": "CCTV Hacking", "link": "https://mega.nz/file/OXwHBaJB#e5oIxxvOMSfxngWa8QjHc4fwo3XiNXe5NQcWsRa64-w"},
    {"name": "Burp Suite Master Course", "link": "https://mega.nz/folder/eM8RkKDI#9SdZ2Xl2hVqBlcmZXtTCSA"},
    {"name": "APK Modding Making Course", "link": "https://leakerskimakokuttachodeart.files.wordpress.com/2020/07/apk1.mp4"},
    {"name": "Free RDP method", "link": "https://www.mediafire.com/file/vabr0hpiarmnu1g/free_RDP_method.rar/file"},
    {"name": "APNA College web develoment", "link":"https://mega.nz/folder/FDcADI6R#12n3-mRCHAoy3thnpRGUAg"}
]

# Tools links
TOOLS_LINKS = [
    {"name": "crax rat", "link": "https://www.mediafire.com/file/kzt988cm06qfbpe/CraxsRat_7.4_%2540Hacki.rar/file         for free key contact :- @giveaway_720"},
    {"name": "Bug Bounty Hunting", "link": "https://github.com/rbsec/dnscan"},
    {"name": "GTA SAN ANDREAS","link": "https://www.mediafire.com/file/t1i6hr729yw6cut/GTA_San_Andreas_%255BMod%255D_v2.11.32_%2540proandroid2.apks/file"},
    {"name": "DDOS","link":"https://www.mediafire.com/file/uvhvncmu913icgt/DDosAttacVol7.txt/file"},

    {"name": "TERMUX HACKING FULL", "link" : "https://www.mediafire.com/file/bl6vipkk80yw5a2/Hacking_With_Termux_Complete_Course_By_Prashant_Asoliya.zip/file"},
]

bot = telebot.TeleBot(BOT_TOKEN)

# Check if the user has joined the @cyberlearnhub channel
def user_has_joined_cyberlearnhub(user_id):
    try:
        context = bot.get_chat_member(chat_id="@cyberlearnhub", user_id=user_id)
        if context.status in ["left", "kicked"]:
            return False
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Error checking membership for @cyberlearnhub: {e}")
        return False
    return True

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_join_channels_prompt(message.chat.id)

# Function to send join channels prompt
def send_join_channels_prompt(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    for channel in REQUIRED_CHANNELS:
        buttons.append(InlineKeyboardButton(text=f"Join {channel['name']} 🌟", url=channel['url']))
    markup.add(*buttons)
    markup.add(InlineKeyboardButton(text="✅ I have joined", callback_data="check_membership"))
    bot.send_message(chat_id, "Please join the following channels to use this bot:", reply_markup=markup)

# Function to send main menu with tools, courses, and sources options
def send_main_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🛠 Tools"), KeyboardButton("📚 Courses"))
    markup.add(KeyboardButton("🔗 Sources"))
    bot.send_message(chat_id, "Choose an option:", reply_markup=markup)

# Function to show tools menu
def send_tools_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for tool in TOOLS_LINKS:
        markup.add(KeyboardButton(tool["name"]))
    markup.add(KeyboardButton("Back to Menu"))
    bot.send_message(chat_id, "Choose a tool:", reply_markup=markup)

# Function to show courses menu
def send_courses_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for course in COURSE_SOURCES:
        markup.add(KeyboardButton(course["name"]))
    markup.add(KeyboardButton("Back to Menu"))
    bot.send_message(chat_id, "Choose a course:", reply_markup=markup)

# Function to show sources links
def show_sources(chat_id):
    sources_text = """
    **Sources for Further Learning:**
    - [contact admin](https://t.me/+UEtTsdCwPDk0YzE1)
    - [contact owner](https://t.me/cyberlearnhub)
    """
    bot.send_message(chat_id, sources_text, parse_mode='Markdown')

# Handle callback queries for checking membership and showing tools/courses/sources
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    user_id = call.from_user.id

    if call.data == "check_membership":
        if user_has_joined_cyberlearnhub(user_id):
            bot.answer_callback_query(call.id, "Thank you for joining the required channels!")
            send_main_menu(call.message.chat.id)
        else:
            bot.answer_callback_query(call.id, "You need to join all first.")
            send_join_channels_prompt(call.message.chat.id)

    elif call.data == "back_to_main_menu":
        send_main_menu(call.message.chat.id)

# Handler for back to menu button in tools and courses menu
@bot.message_handler(func=lambda message: message.text == "Back to Menu")
def back_to_menu(message):
    send_main_menu(message.chat.id)

# Handle main menu options
@bot.message_handler(func=lambda message: message.text in ["🛠 Tools", "📚 Courses", "🔗 Sources"])
def handle_menu_option(message):
    if message.text == "🛠 Tools":
        send_tools_menu(message.chat.id)
    elif message.text == "📚 Courses":
        send_courses_menu(message.chat.id)
    elif message.text == "🔗 Sources":
        show_sources(message.chat.id)

# Handle tool buttons
@bot.message_handler(func=lambda message: any(message.text == tool["name"] for tool in TOOLS_LINKS))
def handle_tool_selection(message):
    for tool in TOOLS_LINKS:
        if message.text == tool["name"]:
            bot.send_message(message.chat.id, f"You selected: {tool['name']}\nLink: {tool['link']}")
    send_main_menu(message.chat.id)  # Send back to main menu after handling tool selection

# Handle course buttons
@bot.message_handler(func=lambda message: any(message.text == course["name"] for course in COURSE_SOURCES))
def handle_course_selection(message):
    for course in COURSE_SOURCES:
        if message.text == course["name"]:
            bot.send_message(message.chat.id, f"You selected: {course['name']}\nLink: {course['link']}")
    send_main_menu(message.chat.id)  # Send back to main menu after handling course selection

# Start the bot polling
bot.polling()
