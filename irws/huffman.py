# application to do huffman coding and decoding.
import sys
from collections import Counter

def extract(fname):
  global pString
  for words in open(fname,'r'):
    pString=pString+words.split() #create a list of words from a given file

if __name__=='__main__':
	global pString # process string holder
	pString=[] # initialize process string
	for fIndex  in range(len(sys.argv)): # loop through files and process
		if fIndex>0:extract(sys.argv[fIndex])
	print Counter(pString)
