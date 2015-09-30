# application to do huffman coding and decoding.
import sys
from collections import Counter
import math


# for assisting in sort operations
def key01(item):
	return item[1]

def readFiles(flist):
  pString=[]
  for file01  in flist: # loop through files and process
    pString=pString+open(file01,'r').read().split()
  return sorted(Counter(pString).most_common())

def append(l,b):
	global code
	if type(l[0])==str:code[l[0]].append(b)
	else:	append(l[0],b)
	if type(l[1])==str:code[l[1]].append(b)
	else:	append(l[1],b)

def c2process(l):
	global code
	code={}
	while len(l)>1:
		l=sorted(l,key=key01)
		x=([l[0][0]]+[l[1][0]],l[0][1]+l[1][1])
		if type(l[0][0])==str:	code[l[0][0]]=[0]
		else:	append(l[0][0],0)
		if type(l[1][0])==str:	code[l[1][0]]=[1]
		else:	append(l[1][0],1)
		del l[0:2]
		l.append(x)
	return l[0][0]






	
	
	
			
	


if __name__=='__main__':
	global code
	sl01=readFiles(sys.argv[1:])
	sl01=sorted(sl01,key=key01)
	print sl01
	sl02=c2process(sl01)
	print sl02
	print code
	





