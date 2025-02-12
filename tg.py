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

#request func
def reqprice(symbol, message):
    ch24h_url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}USDT"
    ch24h_req = requests.get(ch24h_url)
    ch24h_txt = ch24h_req.text
    ch24h_data = json.loads(ch24h_txt)
    change = float(ch24h_data["priceChange"])
    change_percent = ch24h_data["priceChangePercent"]
    change = round(change, 2)
    change = str(change)    
    
    price_url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    price_response = requests.get(price_url)
    price_data = price_response.json()
    current_price = float(price_data["price"])
    current_price = round(current_price, 2)

    price_message = f"1 {symbol} = {current_price} USD"
    change_message = f"За останні 24 години ціна {symbol} змінилася на {change} USD, що дорівнює {change_percent} %"
    bot.send_message(message.from_user.id, price_message)
    bot.send_message(message.from_user.id, change_message)


#reply for BTC
@bot.message_handler(func=lambda message: message.text == "BTC")
def btc(message):
    symbol = "BTC"
    reqprice(symbol,message)

#reply for ETH
@bot.message_handler(func=lambda message: message.text == "ETH")
def eth(message):
    symbol = "ETH"
    reqprice(symbol, message)


#bot infinity works
bot.polling(none_stop=True, interval=0)
