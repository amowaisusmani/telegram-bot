from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters as Filters, CallbackContext
from dotenv import load_dotenv
import os

load_dotenv(r"personal_projects\telegram_bot\api_key.env")
api_key=os.getenv("api_key")

# Initialize the Application
application = Application.builder().token(api_key).build()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello sir, Welcome to the Bot. Please write /help to see the commands available.")

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("""Available Commands :-
    /linkedin - To get my LinkedIn profile URL
    /github - To get my github profile URL
    /telegram - To get my telegram profile URL
    /email = To get my email id                   
    """)

async def linkedIn_url(update: Update, context: CallbackContext):
    await update.message.reply_text("LinkedIn URL => https://www.linkedin.com/in/owais-usmani-03763327a/")

async def github_url(update: Update, context: CallbackContext):
    await update.message.reply_text("Github Link => https://github.com/amowaisusmani")

async def telegram_url(update: Update, context: CallbackContext):
    await update.message.reply_text("Telegram URL => https://t.me/amowaisusmani")

async def email_url(update: Update, context: CallbackContext):
    await update.message.reply_text("owaisusmani8@gmail.com")

async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

async def unknown_text(update: Update, context: CallbackContext):
    await update.message.reply_text("Sorry I can't recognize you, you said '%s'" % update.message.text)

# Adding handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('linkedin', linkedIn_url))
application.add_handler(CommandHandler('github', github_url))
application.add_handler(CommandHandler('email', email_url))
application.add_handler(CommandHandler('telegram', telegram_url))
application.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, unknown_text))
application.add_handler(MessageHandler(Filters.COMMAND, unknown))

# Start polling for updates
application.run_polling()
