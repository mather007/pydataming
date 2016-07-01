#!/usr/bin/python
'''
Created on 2016年5月31日

@author: baby
'''
import json

from _collections import defaultdict
from pyspark import SparkContext
from pyspark import SparkConf
from ch02.ch03test import path

sc = SparkContext("")



path = '/home/baby/workplace/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

rddtest = sc.textFile(path)


def get_counts(seq):
    counts = {}
    for tz in time_zones:
        if tz in counts:
            counts[tz] += 1
        else:
            counts[tz] = 1
    return counts

def get_counts2(seq):
    counts = defaultdict(int) #初始化一个字典所有的值都是0

    for x in seq:
        counts[x] += 1
    return counts

def top_counts(count_dict,n=10):
    value_key = [(v,k) for k,v in count_dict.items()]
    value_key.sort()
    return value_key[-n:]

counts = get_counts(time_zones)
print(top_counts(counts, 10))

from pandas import DataFrame,Series
frame = DataFrame(records)

