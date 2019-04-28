
README FILE for HOMEWORK 3 ASSIGNMENT cs 6322 spring 2019-------

==Debargha Ghosh ==== dxg170014====2021345775


version of python3 used : Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
	COMPATIBLE WITH : Python 3.4.1 (default, Jul 14 2014, 16:29:09)[GCC 4.4.7 20120313 (Red Hat 4.4.7-4)] on linux on csgrads1
==INSTRUCTIONS==
If NLTK not installed follow steps 1-5
to run programs follow steps 6-10

----------------------------------------------------------------------STEPS:----------------------------------------------------------------------------------------------------
STEP 1:
On the terminal:
use command: pip3 install nltk --user

STEP 2:
On terminal 
use command : python3

STEP 3
On python3 terminal
use command: import nltk

STEP 4
If no error 
On python3 terminal
use command: nltk.download('all')

STEP 5
On python3 terminal
use command: exit()
to exit python3 terminal

STEP 6
On terminal 
use command : python3 ./hw3.py filepath

	example :python3 ./hw3.py /people/cs/s/sanda/cs6322/Cranfield
Index_version1_uncompressed.txt will be generated which contains the index and doc vectors
Top_documentss.txt contains top 5 documents and query vectors
answer.txt conatins answers to questions



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


defaultdict: It is a dict subclass that calls a factory function to supply missing values. A python dictionary throws a key error if one tries to access an item with a key not currently in the dictionary. Using Defaultdict means that if the key is not in the dictionary it returns a default value instead of throwing an error.
	reference = https://docs.python.org/2/library/collections.html

list: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
	reference = https://docs.python.org/3.6/tutorial/datastructures.html
using nltk :http://www.nltk.org/book/ch03.html for using word_tokenize
		Word_tokenize() is based on TreebankWordTokenizer.It splits tokens based on white space and punctuation
PorterStemmer: Stemming algorithm to shorten lookup and normalize sentences. It is also present in Natural Language Toolkit.
file handeling :https://docs.python.org/3/library/glob.html 
		https://www.pythonforbeginners.com/cheatsheet/python-file-handling
		https://www.youtube.com/watch?v=6fB8-uu6kRA