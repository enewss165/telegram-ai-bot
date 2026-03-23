import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# Cevap havuzları
selamlar = [
    "Selam kanka 😄 nasılsın?",
    "Aleyküm selam, napıyosun?",
    "Selam 😎 bugün nasıl gidiyor?"
]

nasilsin = [
    "İyiyim kanka sen nasılsın?",
    "Fena değil, takılıyoruz 😄 sen?",
    "Gayet iyiyim, sen anlat bakalım"
]

flort = [
    "Senle konuşmak baya sarıyor 😄",
    "Valla seni sevdim ben",
    "Böyle devam edersen bağlanırım sana 😏"
]

bilinmeyen = [
    "Hmm bunu tam anlamadım ama anlat biraz 😄",
    "Orayı kaçırdım kanka, tekrar söylesene",
    "İlginç 🤔 biraz açsana konuyu"
]

# Cevap sistemi
def cevap_uret(mesaj):
    mesaj = mesaj.lower()

    if "selam" in mesaj or "merhaba" in mesaj:
        return random.choice(selamlar)

    elif "nasılsın" in mesaj:
        return random.choice(nasilsin)

    elif "aşk" in mesaj or "sevgili" in mesaj:
        return random.choice(flort)

    elif "napıyorsun" in mesaj:
        return "Sen yazınca sana cevap veriyorum 😄"

    else:
        return random.choice(bilinmeyen)

# Bot fonksiyonu
async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = cevap_uret(user_message)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

print("Fake AI bot çalışıyor 🤖")
app.run_polling()
