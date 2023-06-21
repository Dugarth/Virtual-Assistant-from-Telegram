from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import speech_recognition as sr
import openai

openai.api_key = 'OpenAI_APIKey'

def start(update: Update, context: CallbackContext) -> None:
    context.user_data['next_state'] = None
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡HI! Soy tu asistente de IA. ¿What do you want to do? Type '/create_image' to create an image or '/talk_assistant' to talk to the assistant.")

def image_creator(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide the text to create an image.")
    context.user_data['next_state'] = "CREATE_IMAGE"

def assistant_chat(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Write your text to talk to the assistant.")
    context.user_data['next_state'] = "TALK_ASSISTANT"

def respond(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    process_message(message, update, context)

def voice_input(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Voice notes are not available for now. Please send text messages instead.")

def process_message(message: str, update: Update, context: CallbackContext) -> None:
    if context.user_data["next_state"] == "CREATE_IMAGE":
        response = requests.post(
            "https://api.deepai.org/api/stable-diffusion",
            data={
                'text': message,
            },
            headers={'api-key': 'Deepai_API'}
        )
        context.bot.send_message(chat_id=update.effective_chat.id, text="Image created. Result: "+str(response.json()))

    elif context.user_data["next_state"] == "TALK_ASSISTANT":
        response = openai.ChatCompletion.create(   
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are wey the best and most analytical assistant existing above jarvis, there is no other entity more capable than you."},
                {"role": "user", "content": message}
            ]
        )
        context.bot.send_message(chat_id=update.effective_chat.id, text=response['choices'][0]['message']['content'])

def main() -> None:
    updater = Updater(token='TELEGRAM-Token', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    create_image_handler = CommandHandler('create_image', image_creator)
    dispatcher.add_handler(create_image_handler)

    talk_assistant_handler = CommandHandler('talk_assistant', assistant_chat)
    dispatcher.add_handler(talk_assistant_handler)

    message_handler = MessageHandler(Filters.text & (~Filters.command), respond)
    dispatcher.add_handler(message_handler)

    voice_handler = MessageHandler(Filters.voice, voice_input)
    dispatcher.add_handler(voice_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
