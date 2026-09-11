from flask import Flask
import threading
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# --- RENDER WEB SERVİSİ İÇİN MİNİ SUNUCU ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()
# -------------------------------------------

TOKEN = "8829651688:AAFF7q9EuRLWPxEiOCxSRtv9W7vAy0GGTB0"
bot = telebot.TeleBot(TOKEN)

# /start komutu ve ana menü butonları
@bot.message_handler(commands=['start'])
def start_mesaji(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("🎁 Günlük Kod Üret", callback_data="kod_uret"),
        InlineKeyboardButton("🔗 Stake.com Giriş", url="https://stake.com")
    )
    markup.add(
        InlineKeyboardButton("🛒 Buy API Claimer", callback_data="api_satin_al"),
        InlineKeyboardButton("📖 Rehber (Guide)", callback_data="rehber")
    )
    
    text = (
        "🔥 **Drop Codes - Stake Kanalına Hoş Geldin!**\n\n"
        "Anlık Stake.com promosyon kodları, bonus limitleri ve hızlı claim sistemleri için doğru yerdesin.\n\n"
        "Aşağıdaki butonları kullanarak test kodları üretebilir veya rehbere göz atabilirsin."
    )
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")

# /kod komutu ile ekrana doğrudan Stake kodu fırlatma
@bot.message_handler(commands=['kod'])
def kod_gonder(message):
    kod_dagit(message.chat.id)

def kod_dagit(chat_id):
    rastgele_kod = "stakecom" + ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=12))
    deger = random.choice([1, 5, 10, 20])
    limit = random.choice([1000, 2000, 5000])
    req = random.choice(["$1,000 last 7 days", "$4,000 last 7 days", "Hiçbir şart yok (Public)"])
    
    kod_metni = (
        f"🎁 **Daily Code - {random.choice(['AG7', 'VIP99', 'STAKEPRO', 'BONUS2026'])}**\n\n"
        f"🔑 **Code:** `{rastgele_kod}`\n"
        f"💵 **Value:** `${deger}`\n"
        f"🎯 **Requirement:** `{req}`\n"
        f"👥 **Claim limit:** `{limit} users`\n\n"
        f"⭐ 💬 🚀"
    )
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔗 Code Link", url=f"https://stake.com/?bonus={rastgele_kod}"))
    markup.add(InlineKeyboardButton("🛍️ Buy API Claimer", callback_data="api_satin_al"))
    markup.row(
        InlineKeyboardButton("🛍️ Buy Claimer", callback_data="claimer_al"),
        InlineKeyboardButton("📖 Guide.", callback_data="rehber")
    )
    
    bot.send_message(chat_id, kod_metni, reply_markup=markup, parse_mode="Markdown")

# Buton tıklamalarını yönetme
@bot.callback_query_handler(func=lambda call: True)
def callback_yonet(call):
    if call.data == "kod_uret":
        bot.answer_callback_query(call.id, "Yeni Stake kodu üretiliyor...")
        kod_dagit(call.message.chat.id)
    elif call.data == "api_satin_al":
        bot.answer_callback_query(call.id, "API Claimer satış paneli")
        bot.send_message(call.message.chat.id, "🛒 **API Claimer Satın Alınması**\nFiyat: $50 / Ay\nİletişim için yöneticiye yazın.")
    elif call.data == "claimer_al":
        bot.answer_callback_query(call.id, "Claimer seçildi")
        bot.send_message(call.message.chat.id, "📦 Standart Claimer botu aktif, otomatik çekim için API anahtarınızı bağlayın.")
    elif call.data == "rehber":
        bot.answer_callback_query(call.id, "Rehber açılıyor")
        bot.send_message(call.message.chat.id, "📖 **Stake Kod Kullanım Rehberi:**\n1. Kod linkine tıkla.\n2. Stake hesabına giriş yap.\n3. Bonus bölümünden kodu aktif et.")

print("Stake Drop Codes Bot aktif ve çalışıyor...")
bot.infinity_polling()
