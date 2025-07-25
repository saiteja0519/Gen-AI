#AIMER Society - Indian Server
!pip install pyTelegramBotAPI

#!pip install openai
!pip install google-generativeai #For Google Gemini #AIMERS
#!pip install anthropic
TelegramBOT_TOKEN = '7673934185:AAG9181hpsunRZJjgjJlku0dSb7rX2lktU8'


#general

#Latest version #Gemini API #AIMER Society #IndianServers
import telebot
import os


"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="  ")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Zenya  AI Powerful BOT, Ask your questions related to Anything")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  response=chat_session.send_message(message.text)
  bot.reply_to(message, response.text)

 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()


#general

#Latest version #Gemini API #AIMER Society #IndianServers
import telebot
import base64
import os
from google import genai
from google.genai import types


client = genai.Client(
        api_key=" ",
    )

model = "gemini-2.0-flash"

fullreply=""

bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Zenya Powerful BOT, Ask your questions related to Anything")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(message)
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=message.text),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )
    fullreply=""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        fullreply+=chunk.text+"\n"
    bot.reply_to(message,fullreply)

bot.polling()


#Latest version
import telebot
import os
import openai
from openai import OpenAI


OPENAI_API_KEY = " "
client = OpenAI(api_key=OPENAI_API_KEY)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from IndianServers")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": message.text},
  ]
    )
  bot.reply_to(message, completion.choices[0].message.content)
 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()



import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=" ",
)

bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from IndianServers")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try :
        print(message)
        message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": message.text
                }
            ]
        }
        ]
        )
        bot.reply_to(message, message.content)
    except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
