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

def c2process(l):
	while len(l)>1:
		l=sorted(l,key=key01)
		x=([l[0][0]]+[l[1][0]],l[0][1]+l[1][1])
		del l[0:2]
		l.append(x)
	return l[0][0]

def c3process(l01):	
	pass
	
	
	
			
	


if __name__=='__main__':
	sl01=readFiles(sys.argv[1:])
	sl01=sorted(sl01,key=key01)
	sl02=c2process(sl01)
	print sl02

	





