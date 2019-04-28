import glob
import re
import time
import sys
from math import log
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
import collections
global readDoc,token_count, word_once
lemmatizer = WordNetLemmatizer()
dictionaryq = defaultdict(int)
odd= defaultdict(int)
odd1= defaultdict(int)
stop_words =['a','all','an','and','any','are','as','be','been','but','by' ,'few','for','have','he','her','here','him','his','how','i','in','is','it','its','many','me','my','none','of','on' ,'or','our','she','some','the','their','them','there','they','that' ,'this','us','was','what','when','where','which','who','why','will','with''you','your']


def var(odd,q):
    qp=defaultdict(list)
    qr=defaultdict(list)
    t= defaultdict(list)
    if q=="q1":
        f=f=open("Top_documents.txt",'w')
    else:
        f=open("Top_documents.txt",'a')
    if q=="q1":
        fh=open("Index_version1_uncompressed.txt",'w')
    else:
        fh=open("Index_version1_uncompressed.txt",'a')
    lemmatizer = WordNetLemmatizer()
    score1i = [0 for x in range(1400*2)]
    score1ii = [0 for x in range(1400*2)]
    score2i = [0 for x in range(1400*2)]
    score2ii = [0 for x in range(1400*2)]
    
    readDoc = 0
    dir_path= sys.argv[1]+"/*"
    #dir_path ='C:/Users/Debargha/Desktop/irhw3/a/*'
    #dir_path ='C:/Users/Debargha/Desktop/ir hw 2_ final/Cranfields/cranfieldsDoc/*'
    #dir_path ='/people/cs/s/sanda/cs6322/Cranfield/*'
    files = glob.glob(dir_path)
    files2 = glob.glob(dir_path)
    d2=  defaultdict(int)
    d3=  defaultdict(int)
    d4=  defaultdict(int)
    for file1 in files2:
            doclen=0
            doclen2=0
            dictionary1 = defaultdict(int)
            sorted_dictionary1= defaultdict(int)
            readDoc= readDoc+1
            txt = (open(file1,"r")).read().lower()
            a= txt.replace('\n',' ')
            
            b=re.search(r'<title>(.*?)</title>',a).group(1)
            t[readDoc]= b
            rem_tags = re.compile('<.*?>')#removing html tags
            text_one =re.sub(rem_tags, '', txt)
            text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
            list_new = word_tokenize(text_two)
            for i1 in list_new:
                doclen = doclen +1
                if i1 not in stop_words:
                    doclen2=doclen2+1
                    i1 = lemmatizer.lemmatize(i1)
                    if i1.isalpha():
                        dictionary1[i1]= dictionary1[i1] + 1
            sorted_dictionary1 = sorted(dictionary1.items(), key=lambda x: x[1],reverse = True)
            
            d2[readDoc]=sorted_dictionary1[0][1]# This dictionary has the document ids and the maxterms
            d3[readDoc] = doclen #This dictionary has the document ids and the document lengths including the stopwords
            d4[readDoc] = doclen2
    sum1=0
    
    for i in d4:
        sum1=sum1+d4[i]
    avgdoclen= sum1/readDoc
    
    so=0
    readDoc1 = 0
    row2=[]
    row3=[]
    low= []
    
    max = 0
    
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
    
    fh.write('Term\tN docs\tTotal Frequency\t\t(Doc ID, In Document Frequency, Max_tf, doclen,Weights W1,W2) \n')
    f.write('------For '+q+'\n')
    for k,v in od.items():
        df= len(v)
        w1=0
        w2=0
        if k in odd:
            a=0
               
            for i5 in range(len(v)):
                a= a+ v[i5]
            so = so +1  
            fh.write(str(k)+'\t'+str(len(v))+'\t'+str(a)+'     ---------->')

            for j in range(len(v)):
                
                W1i= 0.4 + 0.6 * (log(float(v[j]) + 0.5) / log (float(d2[od1[k][j]]) + 1.0))
                W1ii=log(readDoc / float(df))/ log(readDoc)

                W1= W1i*W1ii
                score1i[od1[k][j]]=score1i[od1[k][j]]+W1
                score1ii[od1[k][j]]=score1ii[od1[k][j]]+W1
                qp[k].append(W1)
               
                W2i =  0.4 + 0.6 * (v[j] / (v[j] + 0.5 + 1.5 *(d3[od1[k][j]] / avgdoclen)))
                W2ii=   log (readDoc / df)/log (readDoc)
                
                W2=W2i*W2ii
                qr[k].append(W2)
                
                score2i[od1[k][j]]=score1i[od1[k][j]]+W2
                score2ii[od1[k][j]]=score1ii[od1[k][j]]+W2
                if j== len(v)-1:    
                    fh.write('( '+str(od1[k][j]) + ', '+ str(v[j]) + ', '+str(d2[od1[k][j]])+', '+str(d3[od1[k][j]])+','+str(W1)+','+str(W2)+')\n\n')
                else:
                    fh.write('( '+str(od1[k][j]) + ', '+ str(v[j]) + ', '+str(d2[od1[k][j]])+ ', '+str(d3[od1[k][j]])+','+str(W1)+','+str(W2)+'),')
    f.write('---Vector representation of the query--\n')   
    for ab,ac in qp.items():
        f.write(ab +' --> W1: '+ str(qp[ab])+'\n')
    for ab,ac in qr.items():
        f.write(ab +' --> W2: '+ str(qr[ab])+'\n')
    
    
    score1i.sort(reverse = True)
    #print("Using W1----")
    
    f.write('Using W1 top 5 documents-----\n')
    for i in range(5):
        for j in range(len(score1ii)):
            if score1i[i]== score1ii[j]:
                #print(j,score1i[i])
                f.write('Document: '+ str(j)+ '\tScore: '+ str(score1i[i])+'\tTitle:'+t[j]+'\n')
    score2i.sort(reverse = True)
    #print("Using W2----")
    
    f.write('Using W2 top 5 documents-----\n')
    for i in range(5):
        for j in range(len(score2ii)):
            if score2i[i]== score2ii[j]:
                #print(j,score2i[i])
                f.write('Document: '+ str(j)+ '\tScore: '+ str(score2i[i])+'\tTitle:'+t[j]+'\n')


def clean(q):
    rem_tags = re.compile('<.*?>')#removing html tags
    text_one =re.sub(rem_tags, '', q)
    text_two = re.sub(r'[^\w\s]','',text_one)#removing punctuations
    list_new = word_tokenize(text_two)
    dictionaryq = defaultdict(int)
    for i in list_new:
        if i not in stop_words:
            i=lemmatizer.lemmatize(i)
            dictionaryq[i]=dictionaryq[i]+1
    odd = collections.OrderedDict(sorted(dictionaryq.items()))
    return odd
    
    
#q1="the cat bat"
q1 = "what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft"
odd = clean(q1)
#print("Top 5 documents for query 1 are :")
var(odd,"q1")
q2= "what are the structural and aeroelastic problems associated with flight of high speed aircraft"
odd = clean(q2)
#print("Top 5 documents for query 2 are :")
var(odd,"q2")
q3 = "what problems of heat conduction in composite slabs have been solved so far"
odd = clean(q3)
#print("Top 5 documents for query 3 are :")
var(odd,"q3")
q4= "can a criterion be developed to show empirically the validity of flow solutions for chemically reacting gas mixtures based on the simplifying assumption of instantaneous local chemical equilibrium"
odd = clean(q4)
#print("Top 5 documents for query 4 are :")
var(odd,"q4")
q5 = "what chemical kinetic system is applicable to hypersonic aerodynamic problems"
odd = clean(q5)
#print("Top 5 documents for query 5 are :")
var(odd,"q5")
q6= "what theoretical and experimental guides do we have as to turbulentcouette flow behaviour"
odd = clean(q6)
#print("Top 5 documents for query 2 are :")
var(odd,"q6")
q7 = "is it possible to relate the available pressure distributions for an ogive forebody at zero angle of attack to the lower surface pressures of an equivalent ogive forebody at angle of attack"
odd = clean(q7)
#print("Top 5 documents for query 7 are :")
var(odd,"q7")
q8= "what methods -dash exact or approximate -dash are presently available for predicting body pressures at angle of attack"
odd = clean(q8)
#print("Top 5 documents for query 8 are :")
var(odd,"q8")
q9 = "papers on internal /slip flow/ heat transfer studies"
odd = clean(q9)
#print("Top 5 documents for query 9 are :")
var(odd,"q9")
q10= "are real-gas transport properties for air available over a wide range of enthalpies and densities"
odd = clean(q10)
#print("Top 5 documents for query 10 are :")
var(odd,"q10")
q11 = "is it possible to find an analytical,  similar solution of the strong blast wave problem in the newtonian approximation"
odd = clean(q11)
#print("Top 5 documents for query 11 are :")
var(odd,"q11")
q12= "how can the aerodynamic performance of channel flow ground effect machines be calculated"
odd = clean(q12)
#print("Top 5 documents for query 12 are :")
var(odd,"q12")
q13 = "what is the basic mechanism of the transonic aileron buzz"
odd = clean(q13)
#print("Top 5 documents for query 13 are :")
var(odd,"q13")
q14= "papers on shock-sound wave interaction"
odd = clean(q14)
#print("Top 5 documents for query 14 are :")
var(odd,"q14")
q15 = "material properties of photoelastic materials"
odd = clean(q15)
#print("Top 5 documents for query 15 are :")
var(odd,"q15")
q16= "can the transverse potential flow about a body of revolution be calculated efficiently by an electronic computer"
odd = clean(q16)
#print("Top 5 documents for query 16 are :")
var(odd,"q16")
q17 = "can the three-dimensional problem of a transverse potential flow about a body of revolution be reduced to a two-dimensional problem"
odd = clean(q17)
#print("Top 5 documents for query 17 are :")
var(odd,"q17")
q18= "are experimental pressure distributions on bodies of revolution at angle of attack available"
odd = clean(q18)
#print("Top 5 documents for query 18 are :")
var(odd,"q18")
q19 = "does there exist a good basic treatment of the dynamics of re-entry combining consideration of realistic effects with relative simplicity of result"
odd = clean(q19)
#print("Top 5 documents for query 19 are :")
var(odd,"q19")
q20= "has anyone formally determined the influence of joule heating,  produced by the induced current,  in magnetohydrodynamic free convection flows under general conditions"
odd = clean(q20)
#print("Top 5 documents for query 20 are :")
var(odd,"q20")
