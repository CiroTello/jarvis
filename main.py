
# * =================================================================================================================================================================
# *                     TELEGRAM
# * =================================================================================================================================================================

import time  # Library to use time.sleep() function
import telebot  # No oficial library for Telegram Bot API
from keys.config import *  # Import the bot token from configuracion.py
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
from utils.dialogs import *  # Import the dialogs from dialogs.py
from apis.chatOpenAi import *  # Import the function from chatOpenAi.py
from apis.weather import *  # Import the weather function from weather.py
from database.database import *
 
from flask import Flask, request
from pyngrok import ngrok, conf
from waitress import serve

#! Global vars =====================================================================================================================================================
# Default values
model = "gpt-3.5-turbo"
temperature = 0 
tokens = 0
size = ""
lista = []

#! Bot configs =====================================================================================================================================================
# Create the bot
bot = telebot.TeleBot(bot_token)

# Starting web service of Flask
web_server = Flask(__name__)

# Manage post request sent to web  server
@web_server.route('/', methods=['POST'])
def webhook():
    # Check if post receive is a json type
    if request.headers.get("content-type") == 'application/json':
        json_string = request.stream.read().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)

        bot.process_new_updates([update])
        return 'OK', 200


#! General commands ================================================================================================================================================
@bot.message_handler(commands=["start"])
def start(message):
    dialog = commonDialog()    

    print(dialog)
    
    # Jarvis dialogue and help message at start the bot
    bot.send_message(message.chat.id, dialog, parse_mode="HTML")
    time.sleep(2)

    help(message)


@bot.message_handler(commands=["image"])
def image(message):
    
    botMessage = bot.send_message(message.chat.id, imageDialog(), parse_mode="HTML")

    time.sleep(10)
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, botMessage.message_id)


@bot.message_handler(commands=["weather"])
def weather(message):

    botMessage1 = bot.send_message(message.chat.id, weatherDialog(), parse_mode="HTML")

    markup = InlineKeyboardMarkup(row_width=1)  # Nro de botones por fila
    mendoza = InlineKeyboardButton("Mendoza", callback_data="mendoza")
    markup.add(mendoza)

    botMessage2 = bot.send_message(
        message.chat.id,
        "----------------------------------------------------------------------------- 📌",
        reply_markup=markup,
    )

    time.sleep(15)
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, botMessage1.message_id)
    bot.delete_message(message.chat.id, botMessage2.message_id)


@bot.message_handler(commands=["help"])
def help(message):

    msj = helpDialog()

    bot.send_message(
        message.chat.id,
        msj,
        parse_mode="HTML",
        disable_web_page_preview=True,
        
    )

    return 0


#! Config commands =================================================================================================================================================
@bot.message_handler(commands=["model"])
def models(message):
    markup = InlineKeyboardMarkup(row_width=1)  # Nro de botones por fila

    mGPT = InlineKeyboardButton("GPT", callback_data="GPT")
    mDavinci = InlineKeyboardButton("Davici", callback_data="davinci")
    mCodeDavincii = InlineKeyboardButton("Codex", callback_data="codex")

    markup.add(mGPT, mDavinci, mCodeDavincii)
    botMessage = bot.send_message(
        message.chat.id, "Choose a prossesing model of IA 👇", reply_markup=markup
    )

    time.sleep(10)
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, botMessage.message_id)

@bot.message_handler(commands=["history"])
def models(message):
    # Crear un objeto ReplyKeyboardMarkup con las opciones de respuesta limitadas
    markup = InlineKeyboardMarkup(row_width=2)  # Nro de botones por fila

    opcion1 = InlineKeyboardButton("Si", callback_data="SI")
    opcion2 = InlineKeyboardButton("No", callback_data="NO")
    
    markup.add(opcion1, opcion2)
    
    # Enviar el mensaje con la pregunta y las opciones de respuesta
    bot.send_message(message.chat.id, 'Do you want to clear the history?', reply_markup=markup)

@bot.message_handler(commands=["temperature"])
def configTemperature(message):

    markup = InlineKeyboardMarkup(row_width=3)  # Nro de botones por fila

    t1 = InlineKeyboardButton("0.1", callback_data="t1")
    t2 = InlineKeyboardButton("0.2", callback_data="t2")
    t3 = InlineKeyboardButton("0.3", callback_data="t3")
    t4 = InlineKeyboardButton("0.4", callback_data="t4")
    t5 = InlineKeyboardButton("0.5", callback_data="t5")
    t6 = InlineKeyboardButton("0.6", callback_data="t6")
    t7 = InlineKeyboardButton("0.7", callback_data="t7")
    t8 = InlineKeyboardButton("0.8", callback_data="t8")
    t9 = InlineKeyboardButton("0.9", callback_data="t9")
    t10 = InlineKeyboardButton("1.0", callback_data="t10")

    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
    botMessage = bot.send_message(message.chat.id, "Friendly 👇", reply_markup=markup)

    time.sleep(10)
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, botMessage.message_id)


@bot.message_handler(commands=["token"])
def configTokens(message):

    markup = InlineKeyboardMarkup(row_width=3)  # Nro de botones por fila

    k1 = InlineKeyboardButton("15", callback_data="k1")
    k2 = InlineKeyboardButton("30", callback_data="k2")
    k3 = InlineKeyboardButton("50", callback_data="k3")
    k4 = InlineKeyboardButton("100", callback_data="k4")
    k5 = InlineKeyboardButton("200", callback_data="k5")
    k6 = InlineKeyboardButton("500", callback_data="k6")
    k7 = InlineKeyboardButton("1000", callback_data="k7")

    markup.add(k1, k2, k3, k4, k5, k6, k7)
    botMessage = bot.send_message(
        message.chat.id, "Amount of tokens 👇", reply_markup=markup
    )

    time.sleep(10)
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, botMessage.message_id)


@bot.message_handler(commands=["size"])
def configSize(message):
    markup = InlineKeyboardMarkup(row_width=3)

    s1 = InlineKeyboardButton("256x256", callback_data="s1")
    s2 = InlineKeyboardButton("512x512", callback_data="s2")
    s3 = InlineKeyboardButton("1024x1024", callback_data="s3")

    markup.add(s1, s2, s3)
    botMessage = bot.send_message(
        message.chat.id, "Size of the image 👇", reply_markup=markup
    )

    time.sleep(10)
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, botMessage.message_id)


#! Callbacks ======================================================================================================================================================
@bot.callback_query_handler(func=lambda x: True)
def callback_query_model(call):
    cid = call.message.chat.id

    global model
    
    if call.data == "GPT":
        model = "gpt-3.5-turbo"
        bot.send_message(cid, modelDialog(model))
    elif call.data == "davinci":
        model = "text-davinci-003"
        bot.send_message(cid, modelDialog(model))
    elif call.data == "codex":
        model = "code-davinci-002"
        bot.send_message(cid, modelDialog(model))
    
    global lista

    if call.data == "SI":
        lista=[{"role": "system", "content": "You are a helpful assistant."}]
        bot.send_message(cid, "Ok sr")
    elif call.data == "NO":
        bot.send_message(cid, "Ok sr, no problem")

    global temperature

    if call.data == "t1":
        temperature = 0.1
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t2":
        temperature = 0.2
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t3":
        temperature = 0.3
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t4":
        temperature = 0.4
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t5":
        temperature = 0.5
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t6":
        temperature = 0.6
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t7":
        temperature = 0.7
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t8":
        temperature = 0.8
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t9":
        temperature = 0.9
        bot.send_message(cid, temperatureDialog(temperature))
    elif call.data == "t10":
        temperature = 1.0
        bot.send_message(cid, temperatureDialog(temperature))

    global tokens

    if call.data == "k1":
        tokens = 15
        bot.send_message(cid, tokenDialog(tokens))
    elif call.data == "k2":
        tokens = 30
        bot.send_message(cid, tokenDialog(tokens))
    elif call.data == "k3":
        tokens = 50
        bot.send_message(cid, tokenDialog(tokens))
    elif call.data == "k4":
        tokens = 100
        bot.send_message(cid, tokenDialog(tokens))
    elif call.data == "k5":
        tokens = 200
        bot.send_message(cid, tokenDialog(tokens))
    elif call.data == "k6":
        tokens = 500
        bot.send_message(cid, tokenDialog(tokens))
    elif call.data == "k7":
        tokens = 1000
        bot.send_message(cid, tokenDialog(tokens))

    global size

    if call.data == "s1":
        size = "256x256"
        bot.send_message(cid, sizeDialog(size))
    elif call.data == "s2":
        size = "512x512"
        bot.send_message(cid, sizeDialog(size))
    elif call.data == "s3":
        size = "1024x1024"
        bot.send_message(cid, sizeDialog(size))

    if call.data == "mendoza":
        response = getWeather("Mendoza, AR", call.message)
        weather = weatherView(response, call.message)

        bot.send_message(call.message.chat.id, weather[0], parse_mode="HTML")
        bot.send_photo(call.message.chat.id, weather[1])


# ! Commands about content types ===================================================================================================================================
@bot.message_handler(content_types=["text"])
def send_text(message):
 
    global model
    global size
    global temperature
    global tokens
    global history
    global lista
    
    msj = latinCharRemove(message.text)
    dialog = "<i>" + negativeDialog() + "</i>"

    try:
        if message.text.startswith("/"):
            bot.send_message(message.chat.id, dialog, parse_mode="HTML")

        elif message.text.startswith("#"):
            response = generar(msj, size, message)
            bot.send_photo(message.chat.id, response)

        elif message.text.startswith("!"):
            response = getWeather(msj, message)

            weather = weatherView(response, message)

            bot.send_message(message.chat.id, weather[0], parse_mode="HTML")
            bot.send_photo(message.chat.id, weather[1])

        elif message.text.startswith("sk-"):
            response = actualizarOpenKey(message)
            bot.send_message(message.chat.id, response)

        elif message.text.startswith("wk-"):
            response = actualizarWeatherKey(message)
            bot.send_message(message.chat.id, response)

        elif message.text.startswith("ok-"):
            response = actualizarOrgKey(message)
            bot.send_message(message.chat.id, response)
        
        else:
            
            if model == "gpt-3.5-turbo":    
                msjLista = {"role": "user", "content": "{}".format(msj)}                 
                lista.append(msjLista) 

                response = chat(lista, message)

                rptaLista = {"role": "assistant", "content": "{}".format(response)}
                lista.append(rptaLista)
                
            else:
                response = pregunta(msj, model, temperature, tokens, message)
                
            bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, dialog, parse_mode="HTML")
        

    response = ""


#! main ============================================================================================================================================================
if __name__ == "__main__":

    bot.set_my_commands(
        [
            telebot.types.BotCommand("start", "Start bot"),
            telebot.types.BotCommand("model", "Models of IA"),
            telebot.types.BotCommand("history", "History"),
            telebot.types.BotCommand("image", "Image with DALLE"),
            telebot.types.BotCommand("temperature", "Friendly level"),
            telebot.types.BotCommand("token", "Tokens"),
            telebot.types.BotCommand("size", "Image size"),
            telebot.types.BotCommand("weather", "Weather"),
            telebot.types.BotCommand("help", "More info"),
        ]
    )

    ## Start the bot in infinity polling mode ---------------------------------------------
    ## Remove a previus webhook by doubts
    # bot.remove_webhook()
    ## Wait a second 
    # time.sleep(1)
    # bot.infinity_polling()

    # Start the bot in webhook mode -------------------------------------------------------
    # Ngrok configs
    conf.get_default().config_path = "/Keys/config_ngrok.yml"
    conf.get_default().region = "sa"
    ngrok.set_auth_token(ngrok_token)

    # Create a tunnel https on port 5000
    ngrok_tunnel = ngrok.connect(5000, bind_tls=True)
    ngrok_url = ngrok_tunnel.public_url
    # Show the route in the internet
    print("URL NGROK:", ngrok_url)
    # Remove a previus webhook by doubts
    bot.remove_webhook()
    # Wait a second 
    time.sleep(1)
    # Set the webhook
    bot.set_webhook(url=ngrok_url)
    # Start the server on production enviroment
    serve(web_server, host="0.0.0.0", port=5000)

    # Start the server on devlopment enviroment (warning) ---------------------------------
    # web_server.run(host="0.0.0.0", port=5000)


