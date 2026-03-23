import os
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# Kullanıcı hafıza sistemi
user_memory = {}

# Stil ve karakter
girizgahlar = [
    "Hmm şöyle diyeyim kanka,",
    "Bak şimdi mantığı şu aslında,",
    "Açık konuşayım,",
    "Net söyleyeyim sana,"
]

bitisler = [
    "sen ne düşünüyorsun bu konuda?",
    "bence mantıklı ama karar senin 😄",
    "istersen daha da açabilirim",
    "senin durum biraz farklı olabilir tabi"
]

# Ana cevap sistemi
def cevap_uret(user_id, mesaj):
    mesaj = mesaj.lower()

    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append(mesaj)

    gir = random.choice(girizgahlar)
    bit = random.choice(bitisler)

    # Konuya göre cevap
    if any(k in mesaj for k in ["selam", "merhaba"]):
        cevap = random.choice([
            "Selam kanka 😄 nasılsın?",
            "Aleyküm selam, bugün nasıl gidiyor?",
            "Selam 😎 ne yapıyorsun bakalım?"
        ])

    elif "nasılsın" in mesaj:
        cevap = random.choice([
            "İyiyim kanka, kafa rahat 😄 sen nasılsın?",
            "Fena değil, gün akıyor işte 😎 sen?",
            "Gayet iyiyim, sen anlat bakalım"
        ])

    elif "napıyorsun" in mesaj:
        cevap = random.choice([
            "Sen yazınca sana cevap veriyorum 😄",
            "Takılıyorum öyle, sen napıyorsun?",
            "Şu an seninle sohbet ediyorum 😎"
        ])

    elif "aşk" in mesaj or "sevgili" in mesaj:
        cevap = f"{gir} aşk işleri biraz karmaşık ya 😅 bazen çok iyi bazen kafa yakıyor, {bit}"

    elif "para" in mesaj or "kazan" in mesaj:
        cevap = f"{gir} para kazanma işi sabır işi kanka, hemen olmuyor ama doğru sistem kurarsan güzel gider, {bit}"

    elif "sıkıldım" in mesaj:
        cevap = random.choice([
            "Kanka sıkılmak kötü ya 😅 gel sohbet edelim",
            "Bir şey yapman lazım yoksa kafayı yersin 😄",
            "Müzik aç + bir şeyle uğraş, düzelir"
        ])

    else:
        # Hafızaya göre cevap
        onceki = user_memory[user_id][-3:]

        cevap = f"{gir} dediğin şey mantıklı aslında. {random.choice(['biraz daha açarsan daha iyi anlayabilirim', 'detaya girersen sana daha net cevap veririm', 'tam olarak ne demek istediğini çözmeye çalışıyorum'])}. {bit}"

    return cevap


# Bot handler
async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    mesaj = update.message.text

    reply = cevap_uret(user_id, mesaj)
    await update.message.reply_text(reply)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

    print("🔥 Ultra bot çalışıyor...")
    app.run_polling()


if __name__ == "__main__":
    main()
