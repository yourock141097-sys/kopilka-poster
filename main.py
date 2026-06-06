import os
import random
import requests

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = '@kopilka_sowetov'
OWNER_ID = int(os.environ['YOUR_CHAT_ID'])

POSTS = [
    "🛍 **AliExpress: весенняя распродажа до 80%!**\nСсылка с кешбэком 10%:\n👉 https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/\nТовары до 100 ₽, быстрая доставка в РФ.",
    "💱 **BestChange: выгодный обмен крипты без комиссии**\n👉 https://www.bestchange.ru/?p=1342724\nСравните курсы и не переплачивайте.",
    "📱 **Joom: купоны на скидку 50%**\nПромокод: JOOM50\n👉 https://aflink.ru/g/18vhi6r5cvd1af961d8379deb39b46/?erid=5jtCeReNwxHpfQTFuc3CS5J",
    "💡 **Совет: как копить деньги**\nОткладывайте 10% с каждой зарплаты. А с нашими ссылками вы ещё и экономите на покупках!",
    "🎧 **Беспроводные наушники за 500 ₽ на AliExpress**\n👉 https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/"
]

def send(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}, timeout=10)
        return r.ok
    except:
        return False

def main():
    send(OWNER_ID, "✅ GitHub Actions запущен. Канал будет получать посты по расписанию.")
    post = random.choice(POSTS)
    if send(CHANNEL_ID, post):
        send(OWNER_ID, f"📌 Опубликован пост:\n{post[:80]}...")
    else:
        send(OWNER_ID, "❌ Ошибка публикации. Проверьте права бота.")

if __name__ == '__main__':
    main()
