from typing import Text
import telebot
from telebot import types
import random



TOKEN = '2015141283:AAFpPXJS64eJ72WsS5lDdM0hXpLGw-Aif_4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #Это сами кнопки бота в телеграмм
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_1 = types.KeyboardButton('🔸Рандомное число')
    item_2 = types.KeyboardButton('📈Курсы валют')
    item_3 = types.KeyboardButton('📚Информация')
    item_4 = types.KeyboardButton('➡️Другое')

    markup.add(item_1, item_2, item_3, item_4)  #Эта строчка кода добавляет кнопки.

    # В этой строчке при нажатии /start, происходит привествие с тем кто ввел эту команду и открывает клавиатуру.
    bot.send_message(message.chat.id, 'Доброго времени суток, {0.first_name}! \nМеня зовут S.U.N.D.A.Y Я ваш асистент!'.format(message.from_user), reply_markup = markup) 

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🔸Рандомное число':
            bot.send_message(message.chat.id, 'Твое число: ' + str(random.randint(0,1000))) 
        elif message.text == '📈Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item_1 = types.KeyboardButton('💵Курс Доллара')
            item_2 = types.KeyboardButton('💶Курс Евро')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item_1, item_2, back,)

            bot.send_message(message.chat.id, '📈Курсы валют', reply_markup = markup)

        elif message.text == '💵Курс Доллара':
            bot.send_message(message.chat.id, 'Курс Доллара равен 71,13 руб.')   
        elif message.text == '💶Курс Евро':
            bot.send_message(message.chat.id, 'Курс Евро равен 82,72 руб.') 


        elif message.text == '📚Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item_1 = types.KeyboardButton('💾О боте') 
            item_2 = types.KeyboardButton('📦Что в коробке?')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item_1, item_2, back,)
            bot.send_message(message.chat.id, '📚Информация', reply_markup = markup)

        elif message.text == '💾О боте':
            bot.send_message(message.chat.id, '📌Это тестовый бот, который называется S.U.N.D.A.Y \
                \n📜 Этот бот в будующем должен стать ботом "Асистентом"\
                \n🤖 Version: tg_bot 0.1')

        elif message.text == '📦Что в коробке?':
            bot.send_message(message.chat.id, 'Здесь находится мое механическое сердце 🖤')
            #bot.send_document(message.chat.id, open(r'C:\Users\Admin\Desktop\WorkCase/obj_t1,rb'))
            doc = open('/home/david/Рабочий стол/WorkCase/object_sunday_ver: 1.0(stable).py', 'rb')
            bot.send_document(message.chat.id, doc,)
                
        
        elif message.text == '➡️Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item_1 = types.KeyboardButton('🛠Настройки') 
            item_2 = types.KeyboardButton('📩Подписка')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item_1, item_2, back,)
            bot.send_message(message.chat.id, '➡️Другое', reply_markup = markup)

        elif message.text == ('📩Подписка'):
            bot.send_message(message.chat.id, 'Мой создатель: \
                \n 💌 @vitkov_sky')

        elif message.text == '🔙Назад':
           #Это сами кнопки бота в телеграмм
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item_1 = types.KeyboardButton('🔸Рандомное число')
            item_2 = types.KeyboardButton('📈Курсы валют')
            item_3 = types.KeyboardButton('📚Информация')
            item_4 = types.KeyboardButton('➡️Другое')

            markup.add(item_1, item_2, item_3, item_4)  

            bot.send_message(message.chat.id, '🔙Назад', reply_markup = markup) 

        



            
bot.polling(none_stop = True) # Эта строка кода необходима для того, чтобы бот работал нон-стоп, пока мы его не выключим