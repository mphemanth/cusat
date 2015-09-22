# application to do huffman coding and decoding.
import sys
from collections import Counter

def extract(fname):
  global pString
  for words in open(fname,'r'):
    pString=pString+words.split() #create a list of words from a given file

def readFiles(flist):
	for file  in flist: # loop through files and process
		extract(file)	
		
def mkNL(list):
	x01=list[:2]
	list=[(x01,x01[0][1]+x01[1][1])]+list[2:]
	return list

def mkNested(list):
	for i in range(len(list)-1):
		list=sorted(mkNL(list),key=getKEY)
	return list
	

# for assisting in sort operations
def getKEY(item):
	return item[1]
	
	
	
if __name__=='__main__':
	global pString # process string holder
	pString=[] # initialize process string
	readFiles(sys.argv[1:])
	sortedList=sorted(Counter(pString).most_common(),reverse=True)
	sortedList=mkNested(sortedList)
	print sortedList
	