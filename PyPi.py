#  Python Tashqi kutubxonasi PyPi.org


# pip install googletrans==3.1.0a0

from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)

matn_uz = 'Python - dunyodagi eng masxur dasturlash tili'

# Istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz
tarjima = tarjimon.translate(matn_uz)
# original matn
print(tarjima.origin)
# Tarjima
print(tarjima.text)
# Original matn
print(tarjima.src)

# Boshqa tilga tarjima qilish uchun dest parametridan foydalanamiz
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru)

# Ingliz tilidan tarjima
tarjima_en = 'Toshkent is the capital of Uzbekistan'
tarjima_uz = tarjimon.translate(tarjima_en, dest='uz')
print(tarjima_uz.text)

msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun q deb yozib keting) :"
while True:
    text = input(msg)
    if msg == 'q':
        break
    else:
        tarjima = tarjimon.translate(text, src='uz', dest='en')
        print(tarjima.text)
        
        
import requests
from pprint import pprint

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
pprint(r.text)


import requests

# restcoutries API
country = "Uzbekistan"
url = f"https://restcountries.com/v3.1/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json.keys())
print(r_json['capital'])


import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest='uz')
print(tarjima.text)

# # BeautifulSoup moduli
# Bu modul yordamida bironta sahifani ichida kerakli malumotlarni sug'urib olishimiz mumkin

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')API
print(soup.prettify())
news = soup.find_all(class_=news-title)
print(news[0].text)


from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

# ikki so'z o'rtasidagi o'xshashlik foizini topish
print(fuzz.ratio("salom",'assalom'))
print(fuzz.ratio('salom','salim'))

# Matnlar orasidan 3 ta eng o'xshashlarini ajratib olish
text = 'салом'
matches = process.extract(text, words, limit=3)
print(matches)

# matn orasidan eng o'xshashini topish
text = 'талба'
match = process.extractOne(text,words)
print(match)