from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Ton token Telegram
TOKEN = "7758491482:AAFQzibt7OJihibojbWkqQWGMDhpdOGrL54"

# Liens d'affiliation par langue
AFFILIATE_LINKS = {
    'fr': {
        '1xBet': 'https://reffpa.com/L?tag=d_2548883m_97c_&site=2548883&ad=97&r=registration/',
        'MelBet': 'https://refpa3665.com/L?tag=d_2549581m_45415c_&site=2549581&ad=45415&r=registration/',
        'Betwinner': 'https://bw-prm.com/welcome-pack-jp/?extid=https://casinoparc.com/&p=%2Fregistration%2F&id=20p0',
        'Megapari': 'https://refpazitag.top/L?tag=d_1329825m_25437c_&site=1329825&ad=25437&r=registration/'
    },
    'en': {
        '1xBet': 'https://reffpa.com/L?tag=d_2548883m_97c_&site=2548883&ad=97&r=registration/',
        'MelBet': 'https://refpa3665.com/L?tag=d_2549581m_45415c_&site=2549581&ad=45415&r=registration/',
        'Betwinner': 'https://bw-prm.com/welcome-pack-jp/?extid=https://casinoparc.com/&p=%2Fregistration%2F&id=20p0',
        'Megapari': 'https://refpazitag.top/L?tag=d_1329825m_25437c_&site=1329825&ad=25437&r=registration/'
    },
    'ar': {
        '1xBet': 'https://reffpa.com/L?tag=d_2548883m_97c_&site=2548883&ad=97&r=registration/',
        'MelBet': 'https://refpa3665.com/L?tag=d_2549581m_45415c_&site=2549581&ad=45415&r=registration/',
        'Betwinner': 'https://bw-prm.com/welcome-pack-jp/?extid=https://casinoparc.com/&p=%2Fregistration%2F&id=20p0',
        'Megapari': 'https://refpazitag.top/L?tag=d_1329825m_25437c_&site=1329825&ad=25437&r=registration/'
    },
}

# Langues disponibles
LANGUAGES = {
    'fr': "🇫🇷 Français",
    'en': "🇬🇧 English",
    'ar': "🇸🇦 العربية"
}

# Messages traduits
START_MESSAGES = {
    'fr': "Bienvenue ! Tapez /bonus pour voir les offres.",
    'en': "Welcome! Type /bonus to see the offers.",
    'ar': "مرحبًا! اكتب /bonus لرؤية العروض المتاحة."
}

BONUS_TEXTS = {
    'fr': "Voici les offres de bonus :",
    'en': "Here are the bonus offers:",
    'ar': "إليك عروض البونص المتاحة:"
}

user_languages = {}

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton(name, callback_data=code)] for code, name in LANGUAGES.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choisissez votre langue / Choose your language / اختر لغتك:", reply_markup=reply_markup)

def language_selected(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = query.data
    user_languages[query.from_user.id] = lang
    query.edit_message_text(START_MESSAGES[lang])

def bonus(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, 'fr')
    links = AFFILIATE_LINKS[lang]
    buttons = [[InlineKeyboardButton(name, url=url)] for name, url in links.items()]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(BONUS_TEXTS[lang], reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("bonus", bonus))
    dp.add_handler(CallbackQueryHandler(language_selected))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
