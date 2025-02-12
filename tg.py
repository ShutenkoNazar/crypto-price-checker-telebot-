import telebot 
from telebot import types
import requests
import json



bot = telebot.TeleBot('BOT_TOKEN')


#start bot
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnbtc =  types.KeyboardButton("BTC")
    btneth = types.KeyboardButton("ETH")
    markup.add(btneth)
    markup.add(btnbtc)
    bot.send_message(message.from_user.id,"Я допоможу вам дізнаватись курс криптовалют", reply_markup=markup)
    bot.send_message(message.from_user.id,"Ціну якої валюти ви хочете дізнатись")


#reply for BTC
@bot.message_handler(func=lambda message: message.text == "BTC")
def btc(message):
    reqch = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT")
    txtch = reqch.text
    datach = json.loads(txtch)
    change = float(datach["priceChange"])
    changeper = datach["priceChangePercent"]
    change = round(change, 2)
    change = str(change)
    req = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    txt = req.text
    data = json.loads(txt)
    bpi = float(data["price"])
    bpi = round(bpi, 2)
    price = "1 BTC = " + str(bpi) + " USD"
    changemes = str("За останні 24 години ціна BTC змінилася на " + change + " USD " + " що дорівнює " + changeper + " %")
    bot.send_message(message.from_user.id, price)
    bot.send_message(message.from_user.id, changemes)

#reply for ETH
@bot.message_handler(func=lambda message: message.text == "ETH")
def eth(message):
    #reqest to API
    reqch = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT")
    txtch = reqch.text
    #formatting json
    datach = json.loads(txtch)
    #select the required value (current price)
    change = float(datach["priceChange"])
    #select percent change
    changeper = datach["priceChangePercent"]
    #formatting 
    change = round(change, 2)
    change = str(change)
    req = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
    txt = req.text
    data = json.loads(txt)
    bpi = float(data["price"])
    bpi = round(bpi, 2)
    price = "1 ETH = " + str(bpi) + " USD"
    changemes = str("За останні 24 години ціна ETH змінилася на " + change + " USD " + " що дорівнює " + changeper + " %")
    bot.send_message(message.from_user.id, price)
    bot.send_message(message.from_user.id, changemes)


#bot infinity works
bot.polling(none_stop=True, interval=0)
