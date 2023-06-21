
# Virtual-Assistant-from-Telegram
<<<<<<< HEAD
Prerequisites
Python 3.6 or higher installed on your system.
An internet connection.
Step-by-step Guide

Step 1: Set up your environment

Firstly, you will need to set up a virtual environment. This is good practice for isolating the dependencies for each project. You can do this by using the following commands in your terminal:

bash
Copy code
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Step 2: Install necessary Python packages

This bot requires python-telegram-bot, requests, speech_recognition, and openai packages. Install them with pip:

bash
Copy code
pip install python-telegram-bot requests speech_recognition openai

Step 3: Create a Telegram bot

Next, you'll need to create a bot on Telegram:

Search for the "BotFather" in your Telegram app.
Start a chat and click on the "/newbot" command.
Provide a name for your bot.
Provide a username for your bot. The username has to be unique and end in bot.
Once done, BotFather will give you a token for your bot. Save this token as you will need it later.

Step 4: Get OpenAI API key

You'll need an OpenAI API key for this application:

Visit https://beta.openai.com/signup/ to create an account.
Once you're logged in, go to the API section to get your API key.
Save this key as you will need it later.

Step 5: Get DeepAI API key

You'll also need a DeepAI API key:

Visit https://deepai.org/ and create an account.
Once you're logged in, go to your dashboard and retrieve your API key.
Save this key as you will need it later.

Step 6: Update the Python code

Now, replace the placeholders in your Python code with your actual keys:

Replace 'OpenAI_APIKey' with your OpenAI API key.
Replace 'TELEGRAM-Token' with your Telegram bot token.
Replace 'Deepai_API' with your DeepAI API key.

Step 7: Run the bot

Finally, you can run the bot using the following command:

bash
Copy code
python3 bot.py  # or whatever your Python file is named
Now your bot is live! You can find it on Telegram by its username, and interact with it by sending the /start command.

Usage
Start a chat with the bot on Telegram.
Send /start to start the bot. The bot will greet you and tell you the commands you can use.
Send /create_image to create an image. The bot will ask you for text input. The input you give will be used to generate an image.
Send /talk_assistant to talk with the AI assistant. The bot will ask you for text input. The input you give will be used to generate a conversation with the AI assistant.
Please note that the bot currently does not support voice messages. Please use text messages instead.
=======
This code is a Telegram bot that can perform two tasks: create images based on provided text and have a conversation with the assistant using OpenAI's GPT-3.5-turbo model. It uses the Telegram API, requests library, and speech_recognition library for voice input (not available currently).
>>>>>>> origin/main
