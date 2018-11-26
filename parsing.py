from bs4 import BeautifulSoup
import re
from  urllib.request import*
url = "https://radiomayak.ru/podcasts/archive/"
def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
html = get_html(url)
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all(class_="b-podcast__block-link")
slovar_sound =[]
arhiv_podkastov = []
for a in list:

    print(a['title'])
    arhiv_podkastov.append(a['href'])

vibor_podkasta = int(input('напишите номер подкаста, который хотите открыть'))


second_html = get_html('https://radiomayak.ru'+ arhiv_podkastov[vibor_podkasta])
second_soup = BeautifulSoup(second_html, "html.parser")
sound = second_soup.find_all(class_= "b-podcast__records-listen")

for b in sound:
    print(b['data-title'])
    slovar_sound.append(b['data-url'])
vibor_audio = int(input('напишите номер аудиозаписи, которыю хотите открыть'))
print(slovar_sound[vibor_audio])