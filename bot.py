import telebot
import random
"import os"

"from telebot.types import Message"
"from telebot import apihelper"

TOKEN = '795191972:AAEu6KR0CknC6GXBN2znA3DItqYd9dGCVdQ'
"PROXY = os.environ.get('PROXY')"

"apihelper.proxy={'https': PROXY}"

bot = telebot.TeleBot(TOKEN)

bot.send_message(443890938, "/mem - show mem")

mem_list = ['https://pp.userapi.com/c850616/v850616599/cc098/tGTdT6FfQLU.jpg','https://pp.userapi.com/c849120/v849120357/132802/y3-ciTPrjEU.jpg','https://sun6-5.userapi.com/c850624/v850624434/caeb9/Sg_9hLY10Uk.jpg','https://pp.userapi.com/c850124/v850124716/dd1cd/Td9dSlaAWuY.jpg','https://pp.userapi.com/c845219/v845219310/1a5ee6/2S1RuTZ-LXE.jpg']

@bot.message_handler(commands=['mem'])
def lession(message):
    bot.send_photo(chat_id=443890938, photo=mem_list[random.randrange(1, 4, 1)])
    bot.send_photo(443890938, "Faild")

@bot.message_handler(func=lambda message: True)
def mes(message):
    bot.send_message("/mem - вызывает мемы")

bot.polling()