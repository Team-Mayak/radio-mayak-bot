from bs4 import BeautifulSoup
import re
from  urllib.request import*
print(ord("А"))
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
    slovar_sound.append(b['data-url'])
sound = second_soup.find_all(class_= "b-podcast__records-url")
name_audio = ''
namesau = []
sc = 0
for c in sound:
    if len(c['title']) != 0:
        name_audio = c['title']
    else:
        c = str(c)
        for i in range(1, len(c)):
            if c[i] == '>':
                sc= 1

            if (1072 <= ord(c[i]) <= 1104 or 1040 <= ord(c[i]) <= 1072) and sc == 0:
                name_audio += c[i]
            if (1072 <= ord(c[i-1]) <= 1104 or 1040 <= ord(c[i]) <= 1072) and sc == 0 and (c[i] == '.' or c[i] == '"'):
                name_audio += ' '
            if (1072 <= ord(c[i-1]) <= 1104 or 1040 <= ord(c[i]) <= 1072) and sc == 0 and c[i] =='=':
                name_audio += ' '
    namesau.append(name_audio)
    name_audio = ''
    sc = 0

vibor_audio = int(input('напишите номер аудиозаписи, которыю хотите открыть'))
print(namesau[vibor_audio], slovar_sound[vibor_audio])
