# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:40:52 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from functools import reduce

# 1.26a
f = [(1, 10), ('a', 'b'), ([1], [2])]

[ val for tupl in f for val in tupl   ]