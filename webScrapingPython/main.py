import requests
from bs4 import BeautifulSoup
import urllib.request

def run():
    for i in range(155,161):
        response = requests.get(f'http://xkcd.com/{i}')
        
        #Parseamos el contendio de la respuesta
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        #<img src="//imgs.xkcd.com/comics/barrel_cropped_(1).jpg" [-1] = barrel_cropped_(1).jpg
        image_name = image_url.split('/')[-1]
        directorio='images'
        print(f'Descargando la imagen {image_name}')
        try:
            urllib.request.urlretrieve(f'https:{image_url}', f'{directorio}/{image_name}')
        except Exception as error_e:
            print('Fallo al recuperar la imagen ' + error_e)

if __name__ == "__main__":
    run()