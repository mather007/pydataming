'''
Created on 2016年6月16日

@author: CloudCross
'''
from functools import reduce
sa = "ADELINE"
print(list(map(lambda y: y-64,list(map(ord,sa)))))
print(reduce(lambda x,y: x*y,list(map(lambda y: y-64,list(map(ord,sa))))))
print(1*4*5*12*9*14*5)
import numpy as np
#print(np.array(map(lambda y: y-64,np.array(map(ord,sa)))))
print(np.array(list(map(ord,sa))))
print(np.array(list(map(lambda y: y-64,list(map(ord,sa))))).cumprod())