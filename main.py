import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TOKEN = os.getenv("BOT_TOKEN")

# Mesaj cevaplama
async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_message = update.message.text

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen Türkçe konuşan yardımcı bir asistansın."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content
        await update.message.reply_text(reply)

    except Exception as e:
        print("HATA:", e)
        await update.message.reply_text("Bir hata oluştu.")

# Bot başlat
app = ApplicationBuilder().token(TOKEN).build()

# Handler
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

print("Bot çalışıyor...")
app.run_polling()
