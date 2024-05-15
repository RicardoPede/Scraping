import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import json

url = 'https://www.noticiasformosa.com.ar/'

def get_all_labels_a(url): # obtener todas las etiquetas "a" de la pagina
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    labels_a = soup.find_all('a')
    return labels_a

def get_all_links(url): # obtener todos los links de la pagina
    labels_a = get_all_labels_a(url) 
    links = []
    for label_a in labels_a: 
        try:
            link = label_a['href']
            links.append(link)
        except Exception:
            pass
    return links

def get_content(url): # obtener el contenido de la pagina
    try:
        response = requests.get(url)
        response.raise_for_status() # lanzar excepcion si hay un error en la respuesta
    except RequestException as e:
        print(f'Error en la respuesta: {e}')
        return [], []
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1 = soup.find_all('h1')
        p = soup.find_all('p')
    except (AttributeError, TypeError) as e: # lanzar excepcion si hay un error en el contenido
        print(f'Error en el contenido: {e}')
        return [], []
    return h1, p

print('Iniciando scraping...')
limit = 10
data = {}

links = get_all_links(url) # obtener todos los links de la pagina
links = links[:limit] # limitar la cantidad de links a scrapear
for link in links:
    try:
        h1, p = get_content(link)
        # Convertir los objetos Tag a strings
        h1 = [str(tag) for tag in h1]
        p = [str(tag) for tag in p]
        # Almacenar los elementos h1 y p en el mismo array
        data[link] = h1 + p
    except Exception:
        data[link] = []

with open('data.json', 'w') as f:
    json.dump(data, f)

print('Fin del scraping')