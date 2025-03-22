import telebot
from bot_logic import get_section_info  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7800432693:AAH2ZWh27JoUBAPvmkTSxlje0bjSN6a7nKo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для решения проблемы глобального потепления. Напиши команду /prichin, /predotwrashenie, /posledstvija, /o_poteplenii или /info  ")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Привет! Я бот который поможет решить проблему глобального потепления я могу: 1.рассказать причины глобального потепления 2: как его предотвратить и 3: его последствия")

@bot.message_handler(commands=['o_poteplenii'])
def send_bye(message):
    bot.reply_to(message, get_section_info("Общие сведения"))

@bot.message_handler(commands=['predotwrashenie'])
def send_password(message):
    bot.reply_to(message, get_section_info("Предотвращение и адаптация"))

@bot.message_handler(commands=['posledstvija'])
def send_emodji(message):
    bot.reply_to(message, get_section_info("Климатические последствия"))

@bot.message_handler(commands=['prichin'])
def send_coin(message):
    bot.reply_to(message, get_section_info("Причины потепления (внешние воздействия)"))

# Запускаем бота
bot.polling()