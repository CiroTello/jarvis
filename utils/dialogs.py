import random  # Library to use random.choice() function
from datetime import datetime

#! Function of the Jarvis and Viernes dialogs ==========================================================================================================================================
def commonDialog():
    manyDialogs = [
        "Don't forget that I'm a virtual assistant, sir. Not an slave.",
        "Creating a flight plan for Tennessee.",
        "At your service, sir.",
        "Oh, hello sir.",
        "Processing.",
        "Sir, Agent Coulson of S.H.I.E.L.D. is on the line.",
        "As always sir, a great pleasure watching you work.",
        "Welcome home, sir.",
        "Test complete. Preparing to power down and begin diagnostics.",
    ]

    horaActual = datetime.now()
    hora = horaActual.hour

    if 6 <= hora <= 13:
        manyDialogs.insert(8, "Boss, wake up!")
    elif 13 < hora <= 20:
        manyDialogs.insert(8, "Good afternoon, sir.")
    else:
        manyDialogs.insert(8, "Good evening, boss.")

    dialog = random.choice(manyDialogs)

    return "<i>" + dialog + "</i>"

def negativeDialog():
    manyDialogs = [
        "Sir, there are still terabytes of calculations required before an actual flight is..."
        + "\n-Pulse /help for more info",
        "You are not authorized to access this area." + "\n-Click /help for more info",
        "Sorry sir, the armor is not available¿." + "\n-Click /help for more info",
        "Sr. Stark, I can't let you do this. The situation is too dangerous."
        + "\n-Pulse /help for more info",
        "I don't have access to this information, sir."
        + "\n-Click /help for more info",
        "Nick Fury doesn't trust in me to do this." + "\n-Click /help for more info",
        "SHIELD want to know your location, sir." + "\n-Click /help for more info",
    ]
    dialog = random.choice(manyDialogs)
    return dialog


#! Commands dialogs ==========================================================================================================================================
def helpDialog():
    defaultConfigs = (
        "<b>============================================ J.A.R.V.I.S. 🤖</b>"
        + "\n"
        + "\n"
    )
    defaultConfigs += "<b>📌 Pre-configuration require</b>" + "\n"
    defaultConfigs += "<b>Open AI:</b> To ask and generate image with IA" + "\n"
    defaultConfigs += (
        "     a- Register in the next <a href='https://openai.com/api/'>link</a>" + "\n"
    )
    defaultConfigs += (
        "     b- Go to <i>'Personal'</i> at the top right of the page" + "\n"
    )
    defaultConfigs += "     c- Go to <i>'View API keys'</i>" + "\n"
    defaultConfigs += (
        "     d- Copy your complete api key (sth like this:        <b>sk-123abcde456fghi7jkl</b>) and paste here on Jarvis chat"
        + "\n"
    )
    defaultConfigs +=  "    e- Go to open Ai again, on <i>'Settings'</i> at the left of the personal page" + "\n"
    defaultConfigs += (
        "     f-Copy your complete organization id (sth like this:      <b>org-123abcde456fghi7jkl</b>)" 
        + "\n"
    )
    defaultConfigs += "     g- Back to Jarvis chat, write: 'ok-' followed by the org id copied" "\n"
    defaultConfigs += "     h - Done!" + "\n"
    defaultConfigs += "<b>Open Weather:</b> To consult the weather" + "\n"
    defaultConfigs += (
        "     a- Register in the next <a href='https://openweathermap.org'>link</a>"
        + "\n"
    )
    defaultConfigs += (
        "     b- Go to <i>'API keys'</i> at the top right of the page" + "\n"
    )
    defaultConfigs += (
        "     c- Copy your complete apy key (sth like this: 123abcde456fghi789jkl)"
        + "\n"
    )
    defaultConfigs += (
        "     d- Write 'wk-' before paste key (sth like this: <b>wk-qwed123qwed123</b>), send"
        + "\n"
    )
    defaultConfigs += "     e- Done!" + "\n" + "\n"
    defaultConfigs += (
        "<b>PD:</b> open weather is free, but not open AI. However, open AI give us 18usd to prove, that is really many questions!. Also, you can consult your use on the page of Open AI -> account -> usage."
        + "\n"
    )
    defaultConfigs += (
        "You will can update the key anytime you need, following the steps mentioned above"
        + "\n"
        + "\n"
    )
    defaultConfigs += "<b>⚙ Default settings</b>" + "\n"
    defaultConfigs += "Model ⋯⋯⋯⋯⋯→ <i>text-davinci-003</i>" + "\n"
    defaultConfigs += "Temperature ⋯⋯→ <i>0.1</i>" + "\n"
    defaultConfigs += "Tokens ⋯⋯⋯⋯⋯→ <i>30</i>" + "\n"
    defaultConfigs += "Image size ⋯⋯→ <i>256x256</i>" + "\n" + "\n"
    defaultConfigs += "<b>🤖 Operating instruction to talk to Jarvis</b>" + "\n"
    defaultConfigs += "<b>1-</b> To talk to IA, just write!" + "\n"
    defaultConfigs += (
        "<b>2-</b> To generate an image, send message starting with '#'" + "\n"
    )
    defaultConfigs += "------------- Ej:  <b># Iron Man red armor</b>" + "\n"
    defaultConfigs += (
        "<b>3-</b> To consult the weather, send message starting with '!' following 'City, Country alphaCode'"
        + "\n"
    )
    defaultConfigs += "------------- Ej:  <b>!Buenos Aires, AR</b>" + "\n"
    defaultConfigs += "<b>4-</b> To change the settings, use commands:" + "\n"
    defaultConfigs += (
        "------------- /model"
        + "     /temperature"
        + "       /token"
        + "        /size"
        + "\n"
        + "\n"
    )
    defaultConfigs += (
        "= <b>¡Pay attention to ',' and example'spaces!</b> =" + "\n" + "\n"
    )
    defaultConfigs += (
        "⭐ Developed by: <a href='https://www.instagram.com/ciro_tello/'>ciro_tello</a>"
        + "\n"
    )

    return defaultConfigs

def imageDialog():
    msj = "To generate an image, send message starting with '#'" + "\n" + "\n"
    msj += "------------- Ej: <b>'# Iron Man red armor'</b>"

    return msj

def weatherDialog():
    msj = "To consult the weather, send message starting with '!' and following "
    msj += "<b> (City, Country alphaCode)</b>" + "\n" + "\n"
    msj += "------------- Ej: <b>'!Buenos Aires, AR'</b>"

    return msj

def modelDialog(msj):
    return f"You chose {msj} model"

def temperatureDialog(msj):
    return f"You chose temperature of '{msj}'"

def tokenDialog(msj):
    return f"You chose amount of '{msj}' tokens"

def sizeDialog(msj):
    return f"You chose size of '{msj}'"