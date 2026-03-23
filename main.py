import os
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# cevaplar
selamlar = ["Selam kanka 😄", "Merhaba 😎", "Selam nasılsın?"]
nasilsin = ["İyiyim kanka sen?", "Gayet iyiyim 😄", "Fena değil"]
bilinmeyen = ["Anlamadım 😅", "Biraz açsana", "Tekrar söyler misin"]

def cevap_uret(mesaj):
    mesaj = mesaj.lower()

    if "selam" in mesaj or "merhaba" in mesaj:
        return random.choice(selamlar)
    elif "nasılsın" in mesaj:
        return random.choice(nasilsin)
    else:
        return random.choice(bilinmeyen)

async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = update.message.text
    reply = cevap_uret(mesaj)
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))
    print("Bot çalışıyor 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
