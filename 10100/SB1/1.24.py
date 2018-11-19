# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:39:25 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

#1.24a
 [ (len(x),x) for x in dir(str) ]
#1.24b
 max([ len(x) for x in dir(str) ])
#1.25c
 max([ [len(x),x] for x in dir(str) ])