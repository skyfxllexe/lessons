import telebot
from telebot import types
from vpnbot.data import *
from time import sleep

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['none'])
def goto_main(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Цены")
        item2 = types.KeyboardButton("Расскажи про VPN")
        item3 = types.KeyboardButton("О нас")
        item4 = types.KeyboardButton("Поддержка")
        reset = types.KeyboardButton("Вернуться к выбору языка")
        payment = types.KeyboardButton("Купить подписку на SkyVPN")
        code_word = types.KeyboardButton("У меня есть кодовое слово")
        markup.add(payment)
        markup.row(item1, item2, code_word)
        markup.row(item3, item4)
        markup.add(reset)
        bot.send_message(message.chat.id, "Возвращаем в главное меню", reply_markup=markup)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rus = types.KeyboardButton("Русский")
    eng = types.KeyboardButton("English")
    markup.row(rus, eng)
    bot.send_message(message.chat.id, "Choose language/Выберите язык", reply_markup=markup)



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Русский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Цены")
        item2 = types.KeyboardButton("Расскажи про VPN")
        item3 = types.KeyboardButton("О нас")
        item4 = types.KeyboardButton("Поддержка")
        reset = types.KeyboardButton("Вернуться к выбору языка")
        payment = types.KeyboardButton("Купить подписку на SkyVPN")
        code_word = types.KeyboardButton("У меня есть кодовое слово")
        markup.add(payment)
        markup.row(item1, item2, code_word)
        markup.row(item3, item4)
        markup.add(reset)
        bot.send_message(message.chat.id, hello_message_rus, reply_markup=markup)
    if message.text == "У меня есть кодовое слово":
        bot.send_message(message.chat.id, "Введите кодовое слово: ")
    if message.text =="sadnez":
        bot.send_message(message.chat.id, "Поздравляю, Вы получили скидку 15%")
        bot.send_message(message.chat.id, "Цены для Вас изменились: ")
        bot.send_message(message.chat.id, outPriceRus(0.85))
        goto_main(message)
    
    elif message.text == "English":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        item1 = types.KeyboardButton("Price list")
        item2 = types.KeyboardButton("About VPN")
        item3 = types.KeyboardButton("About us")
        item4 = types.KeyboardButton("Support")
        reset = types.KeyboardButton("Go back")
        payment = types.KeyboardButton("Buy subscription on SkyVPN")
        markup.add(payment)
        markup.row(item1, item2)
        markup.row(item3, item4)
        markup.row(reset)
        bot.send_message(message.chat.id, hello_message_eng, reply_markup=markup)
    
    elif message.text=="Цены":
        bot.send_message(message.chat.id, outPriceRus())
    elif message.text == "Расскажи про VPN":
        bot.send_message(message.chat.id, about_vpn_rus)
    elif message.text == "О нас":
        bot.send_message(message.chat.id, hello_message_rus)
    elif message.text == "Поддержка":
        bot.send_message(message.chat.id, 'По вопросам писать: @discxnnectedexe')
    elif message.text == "Вернуться к выбору языка":
        start_message(message)
    elif message.text == "Купить подписку на SkyVPN":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buy = types.KeyboardButton("Купить подписку")
        about_buy = types.KeyboardButton("Как работает подписка?")
        reset = types.KeyboardButton("Назад")
        markup.row(buy, about_buy)
        markup.add(reset)
        bot.send_message(message.chat.id, "Выберите опцию: ", reply_markup=markup)
    elif message.text == "Купить подписку":
        bot.send_message(message.chat.id, 'Контакт для оплаты: @discxnnectedexe')
    elif message.text == "Как работает подписка?":
        bot.send_message(message.chat.id, how_working_rus)
    elif message.text == "Назад":
        goto_main(message)


    elif message.text == "Go back":
        start_message(message)
    elif message.text=="Price list":
        bot.send_message(message.chat.id, price_text_eng)
    elif message.text == "About VPN":
        bot.send_message(message.chat.id, about_vpn_eng)
    elif message.text == "About us":
        bot.send_message(message.chat.id, hello_message_eng)
    elif message.text == "Support":
        bot.send_message(message.chat.id, 'Q&A: @discxnnectedexe')
    elif message.text == "Buy subscription on SkyVPN":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buy = types.KeyboardButton("Buy")
        about_buy = types.KeyboardButton("How is it working?")
        reset = types.KeyboardButton("Back")
        markup.row(buy, about_buy)
        markup.add(reset)
        bot.send_message(message.chat.id, "Choose option:", reply_markup=markup)
    if message.text == "Buy":
        bot.send_message(message.chat.id, 'Buy here --> @discxnnectedexe')
    if message.text == "How is it working?":
        bot.send_message(message.chat.id, how_working_eng)
    if message.text == "Back":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Price list")
        item2 = types.KeyboardButton("About VPN")
        item3 = types.KeyboardButton("About us")
        item4 = types.KeyboardButton("Support")
        reset = types.KeyboardButton("Go back")
        payment = types.KeyboardButton("Buy subscription on SkyVPN")
        markup.add(payment)
        markup.row(item1, item2)
        markup.row(item3, item4)
        markup.row(reset)
        bot.send_message(message.chat.id, hello_message_eng, reply_markup=markup)
bot.infinity_polling()
