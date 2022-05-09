import requests
from lxml import html
from bs4 import BeautifulSoup
encabezados = {
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
}

url = "https://stackoverflow.com/questions"

resp = requests.get(url)


soup = BeautifulSoup(resp.text, 'lxml')
contenedor_preguntas = soup.find_all(class_="s-post-summary--content")
print(contenedor_preguntas)
for pregunta in contenedor_preguntas:
    texto_pregunta = pregunta.find(class_='s-post-summary--content-title').text
    description = pregunta.find(
        class_='s-post-summary--content-excerpt').text.replace('\n', '').replace('\r', '').strip()
    print(texto_pregunta)
    print(description)
