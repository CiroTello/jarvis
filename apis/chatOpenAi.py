
# * =================================================================================================================================================================
# *                     OPEN IA
# * =================================================================================================================================================================

import requests
from database.database import *
from utils.formats import *
import openai

global api_key
global org_key

def chat(lista, message):
    global org_key
    global api_key

    consultOpenKey(message)
    consultOrgKey(message)
    
    openai.organization = org_key
    openai.api_key = api_key
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= lista
    )

    return response['choices'][0]['message']['content']

# Connect to the API of OpenAI to use the GPT-3 model
def pregunta(msj, model, temperature, tokens, message):
    consultOpenKey(message)

    # Define paramters for the request (requests library)
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Check if the parameters are empty
    if temperature == 0:
        temperature = 0.1
    if tokens == 0:
        tokens = 30

    # Define the data to send
    data = f'{{"model": "{model}", "prompt": "{msj}", "temperature": {temperature}, "max_tokens": {tokens}, "top_p": 1, "frequency_penalty": 0.0, "presence_penalty": 0.6}}'

    # Send the request
    response = requests.post(url, headers=headers, data=data)

        # Check the response
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["text"]

    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return "Please submit your Open AI key, or check if you sent it correctly --> /help"


# Connect to the API of OpenAI to use the DALL-E model
def generar(imageDescription, size, message):
    consultOpenKey(message)

    imageDescription = formatText(imageDescription)

    # Define paramters for the request (requests library)
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Default config for the model
    if size == "":
        size = "256x256"

    # Define the data to send
    data = f'{{"prompt": "{imageDescription}", "n": 1, "size": "{size}"}}'

    # Send the request
    response = requests.post(url, headers=headers, data=data)
    print(response.json())

    # Check the response
    if response.status_code == 200:
        date = response.json()

        return date["data"][0]["url"]

    else:
        print(f"Error: {response.status_code}")


# Go to database to check if you alredy have a key
def consultOpenKey(message):
    global api_key

    print("1")
    
    api_key = consultarDB(message.chat.id)
    print("2")
    if api_key is None:
        print("You don't have OpenAI key yet")

    else:
        api_key = api_key[2]
        print("Your Open AI key is: ", api_key)

def consultOrgKey(message):
    global org_key

    org_key = consultarDB(message.chat.id)

    if org_key is None:
        print("You don't have organization key yet")

    else:
        org_key = org_key[4]
        print("Your organization key is: ", org_key)


# Update the key in the database
def actualizarOpenKey(message):
    global api_key

    message.text = removeSpace(message.text)
    api_key = message.text

    actualizarDB_openAI(message.chat.id, api_key)

    return "Open AI key succesfully update"

def actualizarOrgKey(message):
    global org_key

    message.text = formatText(message.text)
    org_key = message.text

    actualizarDB_OrgKey(message.chat.id, org_key)

    return "Organization key succesfully update"