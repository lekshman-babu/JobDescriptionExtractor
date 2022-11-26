from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import string

#reading old file 
f1=open("demo.txt",'r')

#writing a new file
f2=open("demo2.txt","w+")
text=f1.read()

#makeing tokenized sententence
token=sent_tokenize(text)

#removing puntuations 
for i in range(len(token)):
    for alpha in string.punctuation:
        token[i]=token[i].replace(alpha,'')
a=[]

#removing stop words
for word in token:
    b=""
    for i in word.split():
        if i not in stopwords.words("english"):
            b=b+" "+i
    a.append(b)

#writing the new contents into a new file
for i in a:
    f2.write(i+"\n")
f1.close()
f2.close()
