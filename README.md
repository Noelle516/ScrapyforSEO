# Scrapy por SEO

Esto es un proyecto Scrapy para raspar los sitios web y seperarlos por etiquetas. El "spider" en el proyecto necesita una entrada de usario en el símbolo del sistema. También, hay un interfaz sencilla que puedes utilizar. El nombre de este archivo es: user.py

## Para Empezar

Los instrucciones puede ayudarte obtener una copia del proyecto para su ordenador

### Los requisitos indispensables

Necesita instalar estos antes de empieza:

* [Python](https://www.python.org/downloads/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/)


### Instalar Scrapy

1. Abre el "Anaconda Prompt" (puede buscarlo por buscando "Anaconda" en el menú de Incio de Windows)
2. Crea un virtual env
```
conda create -n yourenvname python=x.x anaconda
```
3. Instalar Scrapy (conda-forge es el canal)
```
conda install -n yourenvname -c conda-forge scrapy
```

## Ejecución del "Spider" en la carpeta "Scrapy"

Puede ejecutar el "spider" usando el comando "scrapy crawl":
```
scrapy crawl user
```
**Asegurarte usar el símbolo del sistema, activar tu virtualenv, y elegir el directorio de nivel superior del proyecto**
* Por esto proyecto el directorio de nivel superior: scrapy

## Ejecución del GUI en la carpeta "gui"

## Referenciass
Por mas informacion: [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
