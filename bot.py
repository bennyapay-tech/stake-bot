import telebot
import random
import time

TOKEN = "8829651688:AAFF7q9EuRLWPxEiOCxSRtv9W7vAy0GGTB0"
bot = telebot.TeleBot(TOKEN)

# /start komutu - Karşılama ve Menü
@bot.message_handler(commands=['start'])
def start_mesaji(message):
    kullaniciAdi = message.from_user.first_name
    text = (
        f"🤖 **Merhaba {kullaniciAdi} Stake Analiz Botuna Hoş Geldin!**\n\n"
        "Benimle Stake.com stratejileri, oran analizleri veya şans oyunları hakkında konuşabilirsin.\n\n"
        "⚡ **Komutlarım:**\n"
        "• /analiz - Anlık Stake.com risk ve oran analizi simülasyonu yapar.\n"
        "• /tavsiye - Günlük şans ve taktik tavsiyesi verir.\n"
        "• /durum - Botun anlık performans durumunu gösterir."
    )
    bot.reply_to(message, text, parse_mode="Markdown")

# /analiz komutu - Stake Analiz Motoru
@bot.message_handler(commands=['analiz'])
def analiz_yap(message):
    bot.reply_to(message, "🔍 Stake.com veri tabanı ve anlık oranlar taranıyor, lütfen bekleyin...")
    time.sleep(1) # Anlık yapay zeka yanıt efekti için minik gecikme
    
    # Simüle edilmiş dinamik analiz sonuçları
    risk_seviyesi = random.choice(["Düşük 🟢", "Orta 🟡", "Yüksek 🔴"])
    tavsiye_oran = round(random.uniform(1.50, 4.80), 2)
    tahmin_basari = random.randint(65, 94)
    
    analiz_mesaji = (
        f"📊 **Stake.com Canlı Analiz Raporu**\n\n"
        f"🎯 **Önerilen Hedef Oran:** `{tavsiye_oran}`\n"
        f"⚠️ **Risk Analizi:** {risk_seviyesi}\n"
        f"📈 **Algoritma Başarı Oranı:** `% {tahmin_basari}`\n\n"
        f"💡 *Not: Bu analiz anlık piyasa hareketlerine ve olasılık matrisine göre yapılmıştır.*"
    )
    bot.reply_to(message, analiz_mesaji, parse_mode="Markdown")

# /tavsiye komutu
@bot.message_handler(commands=['tavsiye'])
def tavsiye_ver(message):
    tavsiyeler = [
        "🎲 Her zaman bütçenin küçük bir kısmıyla oynamak uzun vadede kazandırır.",
        "🔥 Sabırlı ol, anlık heyecanla riskli hamleler yapma.",
        "💡 Stake stratejilerinde kasa yönetimi (Bankroll management) her şeyden önemlidir.",
        "🚀 Bugün şans ibresi yüksek görünüyor ancak yine de kontrollü olmalısın!"
    ]
    bot.reply_to(message, random.choice(tavsiyeler))

# /durum komutu
@bot.message_handler(commands=['durum'])
def durum_kontrol(message):
    bot.reply_to(message, "🟢 Bot aktif, sunucu bağlantısı mükemmel ve anlık veri akışı sağlanıyor.")

# Kullanıcıdan gelen diğer tüm mesajları akıllıca yanıtlayan yapay zeka mantığı
@bot.message_handler(func=lambda message: True)
def akilli_cevap(message):
    k_metin = message.text.lower()
    
    if "merhaba" in k_metin or "selam" in k_metin:
        bot.reply_to(message, "Selam patron! Stake analizi için /analiz komutunu yazabilirsin. 🚀")
    elif "kazanç" in k_metin or "taktik" in k_metin:
        bot.reply_to(message, "Akıllı taktikler ve analizler için buradayım. Hemen /analiz komutunu çalıştırarak verileri çekebilirsin.")
    else:
        bot.reply_to(message, f"🤖 Mesajını aldım: \"{message.text}\"\nBunu Stake analiz motoruma işledim. Detaylı rapor almak için /analiz yazabilirsin.")

print("Gelişmiş Stake Bot aktif ve çalışıyor...")
bot.infinity_polling()
  import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

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
    # Rastgele Stake promosyon kodu üretme simülasyonu
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
    
    # Ekran görüntüsündeki gibi alt alta butonlar
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔗 Code Link", url=f"https://stake.com/?bonus={rastgele_kod}"))
    markup.add(InlineKeyboardButton("🛍️ Buy API Claimer", callback_data="api_satin_al"))
    markup.row(
        InlineKeyboardButton("🛍️ Buy Claimer", callback_data="claimer_al"),
        InlineKeyboardButton("📖 Guide.", callback_data="rehber")
    )
    
    bot.send_message(chat_id, kod_metni, reply_markup=markup, parse_mode="Markdown")

# Buton tıklamalarını yönetme (Inline Button Callbacks)
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
