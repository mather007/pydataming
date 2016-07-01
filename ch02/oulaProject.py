'''
Created on 2016年6月16日

@author: CloudCross
'''
path = r'C:\Users\CloudCross\Desktop\names.txt'
textFile = open(path)
try:
     all_the_text = textFile.read()
finally:
     textFile.close()
data = all_the_text.split(',')

import numpy as np #这个包你可能没有

arr = np.array(data)
sortedarr = np.sort(arr)

from functools import reduce
zimuzhi = np.array([reduce(lambda a,b: a*b,list(map(lambda y: y-64,list(map(ord,x))))) for x in sortedarr])
index=np.arange(1,len(sortedarr)+1)
print((index * zimuzhi).sum())
