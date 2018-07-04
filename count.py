import nltk, csv, itertools, requests
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import Request
from bs4.element import Comment
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

#load the corpus into the script for use
corpusdir = 'LTcorpus/' # Directory of corpus.
ltcorpus = PlaintextCorpusReader(corpusdir, '.*')

def lambda_unpack(f):
    return lambda args: f(*args)

#reads the whole html file using BeautifulSoup/lee el html usando BeautifulSoup  
url = "https://www.logitravel.co.uk/cruises/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = requests.get(url, headers=hdr)

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

#removes all text that isn't found in the corpus
tokens = [thing for thing in tokens if thing in ltcorpus.words("cruises.txt")]

chunker = nltk.chunk.regexp.RegexpParser(r'KT: {<JJ>* <NN.*>+ <IN>?}')
#phrase counter counts the number of times a phrase shows up
tagged_sents = nltk.pos_tag_sents(tokens for sent in tokens)
all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))
                                                    for tagged_sent in tagged_sents))
# join constituent chunk words into a single chunked phrase
candidates = [' '.join(word for word, pos, chunk in group).lower()
for key, group in
itertools.groupby(all_chunks, lambda_unpack(lambda word, pos, chunk: chunk != 'O')) if key]

nouns = [] #empty to array to hold all nouns

for word, pos in nltk.pos_tag(tokens):
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        nouns.append(word)

phrases = []

for cand in candidates:
    if " " in cand:
        phrases.append(cand)

step = list(set(phrases))
print(step)
nouns = list(set(nouns))

string = ""
myFile = open('duplicate cruises.csv', 'w')
with myFile:
    myFields = ['#', 'frases']
    writer = csv.DictWriter(myFile, lineterminator='\n', delimiter=';', quoting = csv.QUOTE_ALL, fieldnames=myFields)
    writer.writeheader()

    for cand in step:
        print(str(raw.count(cand)) + " "+ cand)
        #writes the content into the file
        n= str(raw.count(cand))
        n.encode('utf-8')
        myString = ",".join(cand)
        myString.encode('utf-8')
        writer.writerow({'#' : n, 'frases': cand})
        #removes the phrase from the raw text
        raw = raw.replace(cand, " ")

    for cand in nouns:
        print(str(raw.count(cand)) + " "+ cand)
        #writes the content into the file
        n= str(raw.count(cand))
        n.encode('utf-8')
        myString = ",".join(cand)
        myString.encode('utf-8')
        writer.writerow({'#' : n, 'frases': cand})
        raw = raw.replace(cand, " ")
