import os
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

user_memory = {}

# Yapay "düşünme blokları"
analizler = [
    "bu konu aslında birkaç açıdan değerlendirilebilir.",
    "burada tek bir doğru yok, bakış açısı önemli.",
    "insanlar genelde bu noktayı gözden kaçırıyor.",
    "asıl kritik nokta burada başlıyor."
]

derinlestirme = [
    "mesela kısa vadede farklı, uzun vadede farklı sonuçlar doğurabilir.",
    "çünkü her kararın bir etkisi ve sonucu var.",
    "burada önemli olan senin önceliğin.",
    "olayı sadece yüzeyden değil derinden düşünmek lazım."
]

oneriler = [
    "ben olsam önce durumu netleştirir sonra hareket ederim.",
    "acele etmek yerine biraz analiz etmek daha mantıklı.",
    "burada sabırlı olmak seni öne geçirir.",
    "kontrollü ilerlemek en sağlıklısı olur."
]

kapanis = [
    "sen bu konuda ne düşünüyorsun?",
    "sen olsan nasıl bir yol izlerdin?",
    "bu sana mantıklı geliyor mu?",
    "daha detay istersen açabilirim"
]

def ultra_cevap(mesaj):
    return f"{random.choice(analizler)} {random.choice(derinlestirme)} {random.choice(oneriler)} {random.choice(kapanis)}"

def cevap_uret(user_id, mesaj):
    mesaj = mesaj.lower()

    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append(mesaj)

    # Özel konular
    if "para" in mesaj:
        return f"Para konusu basit gibi görünür ama aslında strateji işidir. {ultra_cevap(mesaj)}"

    elif "aşk" in mesaj or "sevgili" in mesaj:
        return f"Aşk konusu tamamen duygusal ama mantık da devreye girmeli. {ultra_cevap(mesaj)}"

    elif "gelecek" in mesaj:
        return f"Gelecek planı yaparken en önemli şey yönünü belirlemek. {ultra_cevap(mesaj)}"

    elif "sıkıldım" in mesaj:
        return "Sıkılmak aslında beynin yeni bir şey istediğini gösterir. Kendini geliştirecek bir şey bulman lazım. Mesela yeni bir skill öğrenmek bile fark yaratır. Sen genelde boş kaldığında ne yaparsın?"

    elif "nasılsın" in mesaj:
        return "İyiyim kanka 😄 ama asıl önemli olan senin nasıl olduğun. Günün nasıl geçiyor?"

    else:
        return ultra_cevap(mesaj)


async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    mesaj = update.message.text

    reply = cevap_uret(user_id, mesaj)
    await update.message.reply_text(reply)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

    print("ULTRA CHATGPT MODE 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
