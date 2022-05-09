import requests
from lxml import html

encabezados={
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url)

parser = html.fromstring(respuesta.text)


idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
for i in idiomas:
    print(i)
