# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:34:39 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""
from functools import reduce

#1.23a
reduce(lambda x,y: x+y, range(0,100))

#1.23b
reduce(lambda x,y: x+y, [ x for x in range(0,100) if x%3==0 ])

#1.23c
[ x for x in range(0,1000) if (not x%11==0 and not x%3==0) ]