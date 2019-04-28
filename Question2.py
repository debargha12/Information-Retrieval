#dxg170014, Debargha Ghosh
import glob
import re
import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import defaultdict

global readDoc,stem_count, stem_once
#dir_path ='C:/Users/Debargha/Desktop/Cranfields/cranfieldsDoc/*'
#dir_path ='/people/cs/s/sanda/cs6322/Cranfield/*'
dir_path= sys.argv[1]+"/*"
files = glob.glob(dir_path)
readDoc = 0
stem_count=0
stem_once = 0
dictionary = defaultdict(int)
sorted_dictionary= defaultdict(int)
ps= PorterStemmer()

for file in files:
    readDoc= readDoc+1
    txt = (open(file,"r")).read().lower()
    rem_tags = re.compile('<.*?>')#removing html tags
    text_one =re.sub(rem_tags, '', txt)
    text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
    list_new = word_tokenize(text_two)
    for i in list_new:
        dictionary[ps.stem(i)]= dictionary[ps.stem(i)] + 1
        stem_count = stem_count + 1

print("Solution to problem 2")
print("1.The number of distinct stems in the Cranfield text collection: ",stem_count)
print("2.The number of unique stems in the Cranfield text collection: ",len(dictionary))
for j in dictionary:
    if(dictionary[j]==1):
        stem_once= stem_once +1
print("3.The number of stems that occur only once in the Cranfield text collection: ", stem_once)
print("4.The 30 most frequent stems in the Cranfield text collection:")
sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1],reverse = True)
for i in range(30):
    print(sorted_dictionary[i])
avg_stems= stem_count/readDoc
print("5.The average number of word-stems per document: ",avg_stems)
