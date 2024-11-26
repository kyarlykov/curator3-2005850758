from telebot import TeleBot
bot = TeleBot('7794506940:AAH_g_JwSQeCbyk2DCpbUIiDCTHpvPMr3LU')
# обработка новой команды
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'hello')
 
@bot.message_handler(commands=['помоги мне'])
def main(message):
    bot.send_message(message.chat.id, '*что вас беспокоит?*')
    
@bot.message_handler(commands=['мне грустно'])
def main(message):
    bot.send_message(message.chat.id, '[не грусти](https://images.app.goo.gl/j4vzQjiLh7SxxGp68')
    
@bot.message_handler(commands=['спасибо'])
def main(message):
    bot.send_message(message.chat.id, '*всегда пожалуйста!*')
    
    
bot.infinity_polling()
