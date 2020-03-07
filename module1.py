# -*- coding: utf-8 -*-
import codecs
import sys
import re
import nltk
from nltk import word_tokenize
from nltk.stem.isri import ISRIStemmer
st = ISRIStemmer()




file1= codecs.open('text.txt','r','utf-8')
content=file1.read()
file2= codecs.open('outputx.txt','w+','utf-8')

contentlist = content.split("\n")

l=[]
lw=[]
text=''
for x in contentlist:

    words=x.split(" ")
    text=text+"\n"+ " ".join(lw)
    lw=[]
    for xx in words:
            print (st.stem(xx) )
            lw.append(st.stem(xx))

file2.write(text)
print ("done")
file2.close()
