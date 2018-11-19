# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:19:07 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from os import walk

# 1.29a
list(max([[ (file, len(file)) for file in  files ] for cur,dirs,files in walk('.') ]))

# 1.29b
list(max([[ (file, file.count('e')) for file in  files ] for cur,dirs,files in walk('.') ]))


# 1.29c
max(max(max(list(filter(list, [ [ [ (len(l),l,f) for l in open(d+'/'+f, mode='rb').read().splitlines() ]  for f in  fs if f.endswith('txt')  ] for d,ds,fs in walk('.') ])))))

max(max(list(filter(list, [ [ (len(open(d+'/'+f, mode='rb').read().splitlines()),d+'/'+f) for f in fs if f.endswith('txt') ] for d,ds,fs in walk('.') ]))))
