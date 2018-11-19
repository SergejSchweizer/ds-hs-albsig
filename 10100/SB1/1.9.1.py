# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:11:12 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

mat = [[24, 33, 97], [105, 52, 36], [140, 105, 123]]
vec = [147, 49, 117]


print(
    list(map(lambda y: 
        sum(list(map(lambda x,y: x*y ,vec,y))),    
        map(list ,mat)    
           ) 
        )
    )