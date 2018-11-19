# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:42:26 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from functools import reduce

l1 = [ x for x in range(0,99)]

#max
reduce(lambda a,b: a+b,  l1)
#min
reduce(lambda a,b: b-a,  l1)