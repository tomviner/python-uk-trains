import json
import datetime

from uktrains import *

FROM = 'CHX'

def to_int(s):
    h, m = s.split(':')
    h, m = map(int, (h, m))
    if h < 4:
        h += 24 * 60
    t = 60 * h + m
    return t

data = json.load(open('train_data_{}.json'.format(FROM)))
js = [Journey(*j) for j in data]

now = datetime.datetime.now()  # - datetime.timedelta(minutes=20)
now_time = now.strftime('%H:%M')

print FROM
print
print 'now:', now_time
print

last = max([j for j in js if to_int(j.depart_time) <= to_int(now_time)])
last0 = max([j for j in js if to_int(j.depart_time) < to_int(last.depart_time)])
try:
    next = min([j for j in js if to_int(j.depart_time) > to_int(now_time)], key=lambda j: to_int(j.depart_time))
except ValueError:
    next = type('t', (), {'depart_time': '-', 'arrive_time': '-'})

print 'last 2'
print 'depart:', last0.depart_time
print 'arrive:', last0.arrive_time
print
print 'last 1'
print 'depart:', last.depart_time
print 'arrive:', last.arrive_time
print
print 'next'
print 'depart:', next.depart_time
print 'arrive:', next.arrive_time
