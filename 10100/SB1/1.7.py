# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:35:27 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com
"""

"""
Suggested solution for the "Kontrolaufgabe 1.7"
"""
l="bla"

def myEnumerate(mylist):
    return [ x for x in map(lambda x,y: (x,y), range(0,len(mylist)), mylist) ]

print(myEnumerate(l))