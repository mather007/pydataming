'''
Created on 2016年6月16日

@author: CloudCross
'''
from pyspark import SparkContext

logFile = "/home/java18/spark/spark-1.6.0-bin-hadoop2.6/README.md"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: " % (numAs, numBs))