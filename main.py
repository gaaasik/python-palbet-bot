import telebot
#import config
TOKEN = "2146992283:AAG0QT_Hxm85KR65Z7y-HYLiFE4bg2QvcTE"
TELEGRAM_VIP_CHAT_ID = "-1001590001267"
bot = telebot.TeleBot(TOKEN)
path="all_message_bot.csv"
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать в мир ботов, долбоеб")
    bot.send_message(message.chat.id, "Отправь мне сообщение, и я перешлю это в твою випку")

@bot.message_handler(content_types=['text'])
def lalala(message):
    #работает без кнопок
    bot.send_message(message.chat.id, message.text)
    #bot.send_message(TELEGRAM_VIP_CHAT_ID, message.text)
    if message.text == None:
         bot.send_message(message.chat.id, "Умею только текст, осел")
    print(message.text,message.chat.id, message.id)

bot.polling(none_stop=True)
