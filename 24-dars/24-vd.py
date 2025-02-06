# 03.02.2025
# 24 -dars
# Mavzu: Kiril lotin transletirate bot
from Transletirate import to_latin,to_cyrillic
import  telebot
Token="7807024289:AAGWwnDQd__dh4zPkSqjDu5f5yYImE3lC94"
bot=telebot.TeleBot(Token,parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum, Xush kelibsiz!"
    javob+="\nMatnni kiriting:"
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob=to_cyrillic(msg)
    # else:
    #     javob=to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()

# matn=input("Matnni kiriting: ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))