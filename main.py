import os
import random
import requests

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = '@kopilka_sowetov'
OWNER_ID = int(os.environ['YOUR_CHAT_ID'])

# АКТУАЛЬНЫЕ ПОСТЫ (добавляйте или меняйте, я обновлю по запросу)
POSTS = [
    "🔥 **Только сегодня: AliExpress дарит купоны на 500 ₽!**\nЗабери свой: 👉 https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/\nУспей, предложение ограничено!",
    "💸 **Кэшбэк 15% на всё на Joom**\nАктивируй промокод `CASH15` по ссылке:\n👉 https://aflink.ru/g/18vhi6r5cvd1af961d8379deb39b46/?erid=5jtCeReNwxHpfQTFuc3CS5J\nЭкономить легко!",
    "⚡ **Обменник BestChange: самый выгодный курс BTC и USDT**\n👉 https://www.bestchange.ru/?p=1342724\nПроверь сам и не потеряй на комиссиях.",
    "🎁 **Секретная распродажа на AliExpress: скидки до 90%**\nПереходи и забирай товары за копейки:\n👉 https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/\nЧто купили? Жду в комментариях!",
    "📱 **Смартфоны Xiaomi за полцены на Joom**\n👉 https://aflink.ru/g/18vhi6r5cvd1af961d8379deb39b46/?erid=5jtCeReNwxHpfQTFuc3CS5J\nПромокод `XIAOMI50` на дополнительную скидку.",
    "🏆 **Лучшие кэшбэк-сервисы: где выгодно покупать?**\nСравнил для вас: AliExpress и Joom дают максимум. Мои ссылки:\nAliExpress: https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/\nJoom: https://aflink.ru/g/18vhi6r5cvd1af961d8379deb39b46/",
    "💰 **Как экономить на связи?**\nПока нет, но зато крипту менять выгодно на BestChange:\n👉 https://www.bestchange.ru/?p=1342724",
    "🧧 **Покупали что-то по моим ссылкам?**\nНапишите в комментариях, что удалось заказать дёшево. А тут новые купоны:\nAliExpress: https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/",
    "🚀 **AliExpress: электроника по ценам 2020 года**\nНоутбуки, смартфоны, наушники – всё со скидкой 70% по моей ссылке:\n👉 https://aflink.ru/g/1e8d114494d1af961d8316525dc3e8/",
    "✨ **Joom: первые 100 покупателей получат подарок**\nПереходите быстрее: https://aflink.ru/g/18vhi6r5cvd1af961d8379deb39b46/?erid=5jtCeReNwxHpfQTFuc3CS5J\nКод автоматически применится.",
]

def send(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}, timeout=10)
        return r.ok
    except:
        return False

def main():
    send(OWNER_ID, "✅ Автопостер обновлён. Новые посты в канале каждые 6 часов.")
    post = random.choice(POSTS)
    if send(CHANNEL_ID, post):
        send(OWNER_ID, f"📌 Опубликован свежий пост:\n{post[:80]}...")
    else:
        send(OWNER_ID, "❌ Ошибка публикации. Проверьте права бота @K_Admin_Bot в канале.")

if __name__ == '__main__':
    main()
