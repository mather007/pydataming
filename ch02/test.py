'''
Created on 2016年5月31日

@author: baby
'''
import json

path = '/home/baby/workplace/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(seq):
    counts = {}
    for tz in time_zones:
        if tz in counts:
            counts[tz] += 1
        else:
            counts[tz] = 1
    return counts

print(get_counts(time_zones))