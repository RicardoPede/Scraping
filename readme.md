### Scraping

#### 1. Web Scraping
- Web scraping es una técnica utilizada mediante programas de software para extraer información de sitios web. Usualmente, estos programas simulan la navegación de un humano en la World Wide Web ya sea utilizando el protocolo HTTP manualmente, o incrustando un navegador en una aplicación.

#### Paquetes que se utilizan en Scraping

### Requests
- Requests es una librería de Python que permite enviar solicitudes HTTP. La librería es muy fácil de usar y permite enviar solicitudes HTTP de una manera muy sencilla.

```bash
pip install requests
```

### BeautifulSoup
- BeautifulSoup es una librería de Python que permite extraer información de contenido HTML y XML. La librería crea un árbol de análisis para páginas web y permite extraer información de las mismas.

```bash
pip install beautifulsoup4
```

#### 2. Web Crawling
- Web crawling es una técnica utilizada para navegar por la World Wide Web de forma automatizada. La técnica se utiliza para recopilar información de sitios web de forma masiva y rápida.


# PRACTICA WEB SCRAPING

El objetivo de este trabajo práctico es implementar un web crawler en Python que pueda
recorrer un sitio web, extraer todas las etiquetas <a> con sus respectivos enlaces y acceder a
cada página enlazada. Por cada enlace encontrado, se deben obtener todas las etiquetas <h1> y
<p> y almacenarlo en un array en un archivo JSON y si no se encuentran dichos elementos
guardar el array como vacío. Por ejemplo, si el crawler encuentra un enlace
https://example.com/pagina1 en una página y accede a ese enlace, debe obtener el contenido
de la página https://example.com/pagina1 y buscar todos los elementos <h1></h1> y
<p></p>, luego almacenarlo en un array en un archivo JSON bajo la clave
"https://example.com/pagina1" con el array de los elementos solicitados de la página como
valor correspondiente y si no se encuentran dichos elementos guardar el array vacío. Ejemplo:

```json
{
"https://example.com/pagina1": ["<h1>Titutulo 1</h1>", "<p>Texto parrafo</p>"],
"https://example.com/pagina2": ["<h1>Titutulo 1</h1>"],
"https://example.com/pagina3": [],
}
```