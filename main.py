from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))

TOKEN = os.getenv("8763267719:AAEVN8goeeGZK03yW0ecEFcUnlz_1Z8In20")

async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, cevap))

app.run_polling()
