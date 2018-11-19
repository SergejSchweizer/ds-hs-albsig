# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 23:38:12 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

mat1 = [[24, 33, 97], [105, 52, 36], [140, 105, 123]]
mat2 = [[1, 3, 5], [6, 6, 7], [7, 1, 14]]


print(
    list(map(lambda x,y: 
        sum(list(map(lambda x,y: x*y ,x,y))),    
        [ col for col in mat1],
        [list(i) for i in zip(*mat2) ]
           ) 
        )
    )