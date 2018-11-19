# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:46:04 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from random import randint

# 1.25a
[ randint(1,6) for x in range(0,10) ]

# 1.25b
len(
    list(
        filter(
            lambda x: False if 1 in x else True,
            [[ randint(1,6) for x in range(0,10) ]  for i in range(0,100000) ] 
            )
        )
    )/100000
        
# 1.25c
len(
    list(
        filter(
            lambda x: True if x.count(1)==3 else False,
            [[ randint(1,6) for x in range(0,10) ]  for i in range(0,100000) ] 
            )
        )
    )/100000