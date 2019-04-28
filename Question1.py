#dxg170014,Debargha Ghosh
import glob
import re
import time
import sys
from nltk.tokenize import word_tokenize
from collections import defaultdict

global readDoc,token_count, word_once
#dir_path ='C:/Users/Debargha/Desktop/Cranfields/cranfieldsDoc/*'
#dir_path ='/people/cs/s/sanda/cs6322/Cranfield/*'
dir_path= sys.argv[1]+"/*"
files = glob.glob(dir_path)
readDoc = 0
token_count=0
word_once = 0
dictionary = defaultdict(int)
sorted_dictionary= defaultdict(int)
start= time.time()
for file in files:
    readDoc= readDoc+1
    txt = (open(file,"r")).read().lower()
    rem_tags = re.compile('<.*?>')#removing html tags
    text_one =re.sub(rem_tags, '', txt)
    text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
    list_new = word_tokenize(text_two)
    for i in list_new:
        dictionary[i]= dictionary[i] + 1
        token_count = token_count + 1
end= time.time()
print("Solution to problem 1")
print("1.The number of tokens in the Cranfield text collection: ",token_count)
print("2.The number of unique words in the Cranfield text collection: ",len(dictionary))
for j in dictionary:
    if(dictionary[j]==1):
        word_once= word_once +1
print("3.The number of words that occure only once: ", word_once)
print("4.The 30 most frequent words in the Cranfield text collection:")
sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1],reverse = True)#sorting
for i in range(30):
    print(sorted_dictionary[i])
avg_words= token_count/readDoc
print("5.The average number of word tokens per document: ",avg_words)
print("The time taken in seconds is {0:.4f}".format(round(end-start,2)))
