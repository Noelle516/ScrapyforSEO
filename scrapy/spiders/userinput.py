# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:11:05 2018

@author: ORD-PORTATIL-ASUS

The purpose of this code is to get the website the user wants to get 
information about and the file they want to use
and save the text in tags to the file
"""


import scrapy, csv
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
# useful if you have settings.py 
settings = get_project_settings()

class UserSpider(scrapy.Spider):
    name = "user"
    url = ""
    
    #has the user input the URL they want to scrape
    while True:
        url = input("Por favor, anotar el URL " + " \n ")
        data =input("¿Es el URL correcto? S o N " + " \n " + str(url)+ " \n ")
        if data.lower() not in ('s', 'n'):
            print("Tu no anotaste un respuesta correcta ")
        else:
            if data.lower() == 'n':
                print("Repite, por favor")
            else:
                break
    start_urls = [
            url
            ]     
    
    def parse(self, response):
        
        #Extracting the information
        title = response.css("title::text").extract()
        metadescription = response.xpath('//meta[@name="description"]/@content').extract()
        h = response.css("h1::text").extract()
        images = response.xpath('//img/@alt').extract()
        p = response.css("p::text").extract()
        span = response.css("span::text").extract()
        a = response.css("a::text").extract()
        li = response.css("li::text").extract()
        
        #has the user enter the name of the file that they want to save the info in
        na = ""
        while True:
            na = input("Por favor, anotar el nomre del archivo CSV (incluir '.csv') " + " \n ")
            data =input("¿Es el nombre correcto? S o N" + " \n " + str(na)+ " \n ")
            if data.lower() not in ('s', 'n'):
                print("Tu no anotaste un respuesta correcta ")
            else:
                if data.lower() == 'n':
                    print("Repite, por favor")
                else:
                    break
       
        #opening the file and how to write in it
        myFile = open(na, 'w')  
        with myFile:  
           myFields = ['textos', 'tag']
           writer = csv.DictWriter(myFile, lineterminator='\n', delimiter=';', quoting = csv.QUOTE_ALL, fieldnames=myFields)
           writer.writeheader()
           
           #Escribiendo en la fila
           for titulo in title:
               titulo.encode('utf-8'),
               writer.writerow({'textos': titulo,  'tag' : 'title'})
           for md in metadescription:
               md.encode('utf-8'),
               writer.writerow({'textos': md, 'tag': 'meta'})
           for head in h:
               head.encode('utf-8'),
               writer.writerow({'textos': head, 'tag': 'hx'})
           for img in images:
               img.encode('utf-8'),
               writer.writerow({'textos': img, 'tag': 'img-alt'})
           for pa in p:
               pa.encode('utf-8'),
               writer.writerow({'textos': pa, 'tag': 'p'})
           for l in li:
               l.encode('utf-8'),
               writer.writerow({'textos': l, 'tag': 'li'})
           for ad in a:
               ad.encode('utf-8'),
               writer.writerow({'textos': ad, 'tag': 'a'})
           for sp in span:
               sp.encode('utf-8'),
               writer.writerow({'textos': sp, 'tag': 'span'})

# Create a process
process = CrawlerProcess( settings )
process.crawl(UserSpider)
process.start()