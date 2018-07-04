# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:05:05 2018

@author: Noelle Rivera

The purpose of this code is to get the website the user wants to get 
information about and the file they want to use
and save the number of times the most common phrases show up
"""

import nltk, csv
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import Request
from nltk import ngrams
import requests
from bs4.element import Comment
from collections import Counter


url = ""

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

#reads the whole html file using BeautifulSoup/lee el html usando BeautifulSoup  
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = requests.get(url, headers=hdr)
yay = BeautifulSoup(page.content, 'html.parser')

#shows content that is visible to the user, gets rid of scripts, style, and document text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body.content, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

#variable of text to be tokenized
raw = text_from_html(page)

#tokenizes the text
tokens = word_tokenize(raw)

#removes all text that aren´t relevant to the task
tokens = [word.lower() for word in tokens if word.isalpha()]
tokens = [thing for thing in tokens if len(thing) > 1]

text = nltk.Text(tokens)


#phrase counter counts the number of times a phrase shows up
phrase_counter = Counter()

#finds the most common phrase in ngrams with value between 2 -4
i = 2
while i <= 5:
    for phrase in ngrams(tokens, i):
        phrase_counter[phrase] += 1
    i += 1
    
na = ""
while True:
    na = input("Por favor, anotar el nombre del archivo CSV (incluir '.csv') " + " \n ")
    data =input("¿Es el nombre correcto? S o N" + " \n " + str(na)+ " \n ")
    if data.lower() not in ('s', 'n'):
        print("Tu no anotaste un respuesta correcta ")
    else:
        if data.lower() == 'n':
            print("Repite, por favor")
        else:
            break

myFile = open(na, 'w')
with myFile:
    myFields = ['#', 'frases']
    writer = csv.DictWriter(myFile, lineterminator='\n', delimiter=';', quoting = csv.QUOTE_ALL, fieldnames=myFields)
    writer.writeheader()

#prints the 50 most common phrases and how many times it shows up in the text
    most_common_phrases = phrase_counter.most_common(50)
    for k,v in most_common_phrases:
        print('{0: <5}'.format(v), k)
        #writes the content into the file
        n= '{0: <5}'.format(v)
        n.encode('utf-8')
        myString = ",".join(k)
        myString.encode('utf-8')
        writer.writerow({'#' : n, 'frases': k})
