# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:30:48 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

#1.21a
def teiler(zahl): return [ x for x in range(1,zahl) if zahl%x==0 ]

#1.21b
[ zahl  for zahl in range(1,1000) if len(teiler(zahl))==5 ]

#1.21c
 max(
     list(
         map(
             lambda  x: 
                 [len(teiler(x)), x], 
                 [ zahl for zahl in range(1,1000) ] 
            )
        )
    )[1]