# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:29:49 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com
"""

"""
Suggested solution for the "Kontrolaufgabe 1.8 a"
"""
l1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2=[26, 2, 99, 65, 78, 34, 83, 70, 23, 66]

def factorOfLists(l1,l2):
    ans=[None]*len(l1)
    for c in range(0,len(l1)):
        cc = (0 if c == len(l1)-1 else c+1)
        #print(l1[c]*l2[cc]-l1[cc]*l2[c], c, cc)
        ans[c]=l1[c]*l2[cc]-l1[cc]*l2[c]
    return list(reversed(ans))

print(factorOfLists(a,r))