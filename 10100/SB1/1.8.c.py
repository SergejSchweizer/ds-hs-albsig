# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:00:07 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""
from operator import mul


l1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2=[26, 2, 99, 65, 78, 34, 83, 70, 23, 66]

print(
    list(
        reversed(
            list(
                map(
                    lambda a,b,c,d: mul(a,b)-mul(c,d),\
                        l1,l2[1:]+[l2[0]],\
                        l1[1:]+[l1[0]],l2\
                    )
                )
            )
        )
    )