# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:03:02 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

 f = open("Bibel.txt").read()

# 1.17.a
 [ lines.split()[0] 
     for lines in f.splitlines() 
         if len(lines) > 0 
 ]
 
 # 1.17.b
 [ lines for lines in f.splitlines() 
     if len(lines) > 0 and lines[0].islower() 
 ]
 
 # 1.17.c
 max(
     [ len(
        [ word for word in words.split() if word.islower() ]
        )  
           for words in f.splitlines() ] 
     )
     
# 1.17.c the ugly one
 max(
     list(
         map(
             lambda x: 
                 len(list(filter(lambda x: x if len(x)>0 and x[0].islower() else None, x.split() )))
                 ,[ lines  for lines in f.splitlines() ] 
             )
         )
    )