
import requests



def get_value():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return int(data['Valute']['USD']['Value'])

def outPriceRus(discount = 1):
    price = int(get_value())
    with_discount = int(price*discount)
    price_text_rus = f"""
    🌟 Наши цены 🌟
Текущий курс доллара: {int(price)}

💲 30 дней - $4 - {4*with_discount} руб
💲 90 дней - $8 - {8*with_discount} руб
💲 180 дней - $15 - {15*with_discount} руб
💲 360 дней - $25 - {25*with_discount} руб
    """
    return price_text_rus

about_vpn_rus = """
Суть нашего платного сервиса заключается в том, что
Вы получаете неограниченный трафик во время работы под VPN, 
неограниченная скорость. Если обобщая - VPN-туннель лично ваш.
только у Вас к нему доступ, в отличие от общих VPN-туннелей.
Это обеспечивает лучшую защиту от кражи данных.
"""


how_working_rus = """
Вы получите файл .config, который будет являться вашим приватным туннелем 😊
Далее нужно будет скачать приложение, в которое вы будете загружать этот .config 😉
Нажимая кнопку activate в интерфейсе, будет происходить подключение к серверу. 🔌
На этом все. Файл будет работать ровно столько, на сколько вы покупали подписку ⏰😄


"""

how_working_eng = """

You will receive a .config file, which will serve as your private tunnel. 😊
Next, you will need to download an application where you will upload this .config file. 😉
By clicking the "activate" button in the interface, a connection to the server will be established. 🔌
That's it. The file will work for the duration of your subscription. ⏰😄
"""
token = '5860009431:AAF8s4lcHOsWPlSRjVKN0YITYVxI1pXB5-0'

hello_message_rus= """
🌟 Добро пожаловать в Sky VPN! Мы рады приветствовать вас в нашем сервисе 🌟
Теперь без РЕКЛАМЫ
Sky VPN предлагает надежное и безопасное подключение к интернету 🛡️
Наша VPN-сеть обеспечивает защиту вашей конфиденциальности, обходит географические ограничения и обеспечивает высокую скорость соединения 💨

Мы предлагаем широкий выбор серверов в разных странах, чтобы вы могли насладиться свободой и анонимностью в сети 🌍
Присоединяйтесь к Sky VPN и ощутите преимущества безопасного и свободного интернета! 🚀

"""

price_text_eng = """
🌟 Price List 🌟

💲 30 days - $4
💲 90 days - $8
💲 180 days - $15
💲 360 days - $25
"""

about_vpn_eng = """
The essence of our paid service is that
you get unlimited traffic while working under VPN,
unlimited speed. In general terms, the VPN tunnel is personally yours,
only you have access to it, unlike shared VPN tunnels.
This provides better protection against data theft.
"""


hello_message_eng = """
🌟 Welcome to Sky VPN! We are delighted to greet you in our service 🌟

Sky VPN offers reliable and secure internet connection 🛡️
NO AD!
Our VPN network ensures the protection of your privacy, bypasses geographical restrictions, and provides high-speed connection 💨

We offer a wide selection of servers in different countries, so you can enjoy freedom and anonymity on the internet 🌍
Join Sky VPN and experience the benefits of a safe and unrestricted internet! 🚀
"""
