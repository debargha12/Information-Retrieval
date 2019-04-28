
README FILE for HOMEWORK 1 ASSIGNMENT cs 6322 spring 2019-------

==Debargha Ghosh ==== dxg170014====2021345775


version of python3 used : Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
	COMPATIBLE WITH : Python 3.4.1 (default, Jul 14 2014, 16:29:09)[GCC 4.4.7 20120313 (Red Hat 4.4.7-4)] on linux on csgrads1
==INSTRUCTIONS==
If NLTK not installed follow steps 1-5
to run programs follow steps 6 and 7
Some of the questions have been answered after step 7
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
use command: nltk.download('punkt')

STEP 5
On python3 terminal
use command: exit()
to exit python3 terminal

STEP 6
On terminal 
use command : python3 ./Question1.py file_path_Cranfield
	example :python3 ./Question1.py /people/cs/s/sanda/cs6322/Cranfield
provide  the filepath of the cranfield collection as the first argument
to run the program
--- The directory path in Question1.py is  /people/cs/s/sanda/cs6322/Cranfield/ as provided in the HOMEWORK 1 pdf and it is the first argument.
output image on csgrads1 machine is Question1_solution.jpg

STEP 7
On terminal 
use command : python3 ./Question2.py file_path_Cranfield
	example :python3 ./Question2.py /people/cs/s/sanda/cs6322/Cranfield
provide  the filepath of the cranfield collection as the first argument
to run the program
--- The directory path in Question2.py is  /people/cs/s/sanda/cs6322/Cranfield/ as provided in the HOMEWORK 1 pdf and it is the first argument.
output image on csgrads1 machine is Question2_solution.jpg


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. How long the program took to acquire the text characteristics: 
------The first program is taking 2 seconds on average
2. How the program handles:
A. Upper and lower case words (e.g. "People", "people", "Apple", "apple"):--- The program converts every letter to lower case. So "Apple" becomes "apple"
B. Words with dashes (e.g. "1996-97", "middle-class", "30-year", "tean-ager"):--- "-" is replaced by "". So "1996-97" becomes "199697"
C. Possessives (e.g. "sheriff's", "university's"): The "'s" is replaced by "s".:---- So "university's" becomes "universitys"
D. Acronyms (e.g., "U.S.", "U.N."):--- The "." is removed and "U.S." becomes "us"

3. Briefly discuss your major algorithms and data structures.

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