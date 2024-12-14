import telebot

bot = telebot.TeleBot("7540910844:AAFnyQ-d3S2N77NZpo3cOG87ttA4rx4v7s8")

@bot.message_handler(commands=["start", "help"])
def send_message(message):
  bot.send_message(message.chat.id, "Hello Mate !")
  
@bot.message_handler(func=lambda message : True)
def unknown_message(message):
  bot.send_message(message.chat.id, message.text + " Is not a command")
  
bot.infinity_polling()