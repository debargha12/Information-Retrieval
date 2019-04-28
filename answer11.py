import glob
import re
import time
import sys
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def ver():

    ps= PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    #stop_words = set(stopwords.words('english'))
    stop_words =['a',
'all'
,'an'
,'and'
,'any'
,'are'
,'as'
,'be'
,'been'
,'but'
,'by' 
,'few'
,'for'
,'have'
,'he'
,'her'
,'here'
,'him'
,'his'
,'how'
,'i'
,'in'
,'is'
,'it'
,'its'
,'many'
,'me'
,'my'
,'none'
,'of'
,'on' 
,'or'
,'our'
,'she'
,'some'
,'the'
,'their'
,'them'
,'there'
,'they'
,'that' 
,'this'
,'us'
,'was'
,'what'
,'when'
,'where'
,'which'
,'who'
,'why'
,'will'
,'with'
'you','your']
    global readDoc,token_count, word_once
    dir_path= sys.argv[1]+"/*"
    #dir_path ='C:/Users/Debargha/Desktop/ir hw 2_ final/a/*'
    #dir_path ='C:/Users/Debargha/Desktop/ir hw 2_ final/Cranfields/cranfieldsDoc/*'
    #dir_path ='/people/cs/s/sanda/cs6322/Cranfield/*'
    files = glob.glob(dir_path)
    readDoc = 0
    token_count=0


    maxdoc = 0
    maxtf = 0
    start= time.time()
    for file in files:
        doclen=0
        dictionary = defaultdict(int)
        sorted_dictionary= defaultdict(int)
        readDoc= readDoc+1
        txt = (open(file,"r")).read().lower()
        rem_tags = re.compile('<.*?>')#removing html tags
        text_one =re.sub(rem_tags, '', txt)
        text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
        list_new = word_tokenize(text_two)
        for i in list_new:
            if i.isalpha():
                doclen=doclen+1
                if i not in stop_words:
                    i = lemmatizer.lemmatize(i)
                    dictionary[i]= dictionary[i] + 1
        sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1],reverse = True)
        '''print("Document: ", file),
        print("-- max_tf: ",sorted_dictionary[0])'''
        if sorted_dictionary[0][1]>maxtf:
            maxtf = sorted_dictionary[0][1]
            tfdoc = file
        #print("-- doclen: ",doclen)
        if doclen>maxdoc:
            maxdoc = doclen
            lendoc =file
        #fh.write("Document:%d\r\n"%(readDoc))
        '''fh.write("Document:%s\r\n"%(file))
        fh.write("-- max_tf:%s"%sorted_dictionary[0][0])
        fh.write("-- frequency:%d\n"%sorted_dictionary[0][1])
        fh.write("-- doclen:%d\n"%doclen)'''
    with open("answers.txt", "a") as f:
        f.write("\n--Maximum term frequency is in: %s\n" %(tfdoc))
        f.write("--Maximum document length is in: %s\n"%(lendoc))
    print("Maximum term frequency is in: " , tfdoc)
    print("Maximum document length is in: ",lendoc)
fh=open("answer11.txt",'w')
print(ver(),file = fh)
fh.close()
