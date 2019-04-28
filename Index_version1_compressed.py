import glob
import re
import time
import math
import sys
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
import collections
global readDoc,token_count, word_once
def gamma(x):
    b = int(bin(x)[2:])
    digit = int(math.log10(b))
    offset = ((bin(x)[3:]).zfill(digit))
    
    digits = len(offset)
    
    length= 0
    for i in range(1,digits+1):
        length= length+ (10**i)
        
        
    gammacode= int(str(length)+offset)
    return gammacode
def ver():
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
    readDoc = 0
    dir_path= sys.argv[1]+"/*"
    #dir_path ='C:/Users/Debargha/Desktop/ir hw 2/a/*'
    #dir_path ='C:/Users/Debargha/Desktop/ir hw 2_ final/Cranfields/cranfieldsDoc/*'
    #dir_path ='C:/Users/Debargha/Desktop/ir hw 2_ final/cranfieldsDoc/*'
    #dir_path ='/people/cs/s/sanda/cs6322/Cranfield/*'
    files = glob.glob(dir_path)
    files2 = glob.glob(dir_path)
    d2=  defaultdict(int)
    d3=  defaultdict(int)
    for file1 in files2:
            doclen=0
            
            dictionary1 = defaultdict(int)
            sorted_dictionary1= defaultdict(int)
            readDoc= readDoc+1
            txt = (open(file1,"r")).read().lower()
            rem_tags = re.compile('<.*?>')#removing html tags
            text_one =re.sub(rem_tags, '', txt)
            text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
            list_new = word_tokenize(text_two)
            for i1 in list_new:
                doclen=doclen+1
                if i1 not in stop_words:
                    i1 = lemmatizer.lemmatize(i1)
                    if i1.isalpha():
                        dictionary1[i1]= dictionary1[i1] + 1
            sorted_dictionary1 = sorted(dictionary1.items(), key=lambda x: x[1],reverse = True)
            
            d2[readDoc]=sorted_dictionary1[0][1]# This dictionary has the document ids and the maxterms
            d3[readDoc] = doclen #This dictionary has the document ids and the document lengths including the stopwords
            
    
    readDoc1 = 0
    row2=[]
    row3=[]
    for file in files:
        
        dictionary = dict()
        row= ()
        row1=()    
        readDoc1 = readDoc1+1
        
        txt = (open(file,"r")).read().lower()
        rem_tags = re.compile('<.*?>')#removing html tags
        text_one =re.sub(rem_tags, '', txt)
        text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
        list_new = word_tokenize(text_two)
        for i2 in list_new:
            
            if i2 not in stop_words:
                i2 = lemmatizer.lemmatize(i2)
                if i2.isalpha():
                    if i2 not in dictionary:
                        dictionary[i2] = 1
                    else:
                        dictionary[i2]= dictionary[i2]+1
        for i3 in dictionary:
            l= list(row)
            l.append(i3)
            l.append(dictionary[i3])
            row2.append(tuple(l))
        for i4 in dictionary:
            l1= list(row1)
            l1.append(i4)
            l1.append(readDoc1)
            row3.append(tuple(l1))
            
        
    
    so = 0
    d= defaultdict(list)
    s= defaultdict(list)
    for k,v in row2:
        d[k].append(v)
    d1= defaultdict(list)
    s1= defaultdict(list)
    for k1,v1 in row3:
        d1[k1].append(v1)
    od = collections.OrderedDict(sorted(d.items()))
    od1 = collections.OrderedDict(sorted(d1.items()))
    fh.write('Dictionary\t\t\t\t\tPostings\n')
    fh.write('Terms\tN docs\tTotalFreq\tLength\tTerm Pointer\n')
    for k,v in od.items():
        a=0
        for i5 in range(len(v)):
            a= a+ v[i5]
        so =so+1
        fh.write(str(k)+'\t'+str(len(v))+'\t'+str(a)+'\t'+ str(len(k))+'\t'+ str(so+8)+'     ---------->')
        
        for j in range(len(v)):
            if j==0 and len(v)==1:
                fh.write(' ('+ str(gamma(od1[k][j])) + ')\n\n')
            elif j==0:
                fh.write(' ('+ str(gamma(od1[k][j])) + ')')
            elif j== len(v)-1:
                
                fh.write(' ('+ str(gamma(od1[k][j]-od1[k][j-1])) + ')\n\n')
            else:
                fh.write(' ('+ str(gamma(od1[k][j]-od1[k][j-1])) + ')')
                        
    
        


        

fh=open("Index_version1_compressed.txt",'w')
start= time.time()
print(ver(),file = fh)
end= time.time()
print("The time taken in seconds is {0:.4f}".format(round(end-start,2)))
fh.close()
     
        
