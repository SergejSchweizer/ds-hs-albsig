# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:25:54 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""
import numpy as np

#2.1a
c = np.arange(100)**2

#2.1b
 b = np.arange(1000)
 b=b[b%13!=0]
 b=b[b%11!=0]
 
 #2.1c
 o = np.ones(100)
 o[ [ x for x in range(0,len(o)) if x%2==0] ]=0


 b= np.zeros(100)
 b[2::2]=1