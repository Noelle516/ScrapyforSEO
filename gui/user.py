# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:35:11 2018

@author: ORD-PORTATIL-ASUS

Using Scrapy
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from os import system
import scrapy, csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# useful if you have settings.py 
settings = get_project_settings()

        

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        url = QLabel("URL")
        file = QLabel("Archivo (incluye .csv)")
        
        self.urlEdit = QLineEdit()
        self.fileEdit = QLineEdit()
        
        okButton = QPushButton("OK", self)
        
        okButton.clicked.connect(self.buttonClicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(url, 1, 0)
        grid.addWidget(self.urlEdit, 1, 1)

        grid.addWidget(file, 2, 0)
        grid.addWidget(self.fileEdit, 2, 1)
        
        grid.addWidget(okButton, 4, 1)

        
        self.setLayout(grid) 
           
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Test')    
        self.show()
        
        
    @pyqtSlot()    
    def buttonClicked(self):
        fileEditValue = self.fileEdit.text()
        urlEditValue = self.urlEdit.text()
        buttonReply = QMessageBox.question(
                self, 'You Typed:', 
                "URL: " + urlEditValue + "\nNombre del archivo: " + fileEditValue+ "\n \n¿Es correcta?",
                QMessageBox.Yes | QMessageBox.No)
        print(self.urlEdit.text())
        if buttonReply == QMessageBox.No:
            self.fileEdit.setText("")
            self.urlEdit.setText("")
        else:
            if buttonReply == QMessageBox.Yes:
                print("Yay!")
                
                class GuisSpider(scrapy.Spider):
                    name = "guis"
                    
                    start_urls = [
                            urlEditValue
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
                        
                        
                        #opening the file and how to write in it
                        myFile = open(fileEditValue, 'w')  
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
       
            process = CrawlerProcess( settings )
            process.crawl(GuisSpider)
            process.start()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qt_%s' % locale, path)
    app.installTranslator(translator)
    ex = Example()
    sys.exit(app.exec_())
