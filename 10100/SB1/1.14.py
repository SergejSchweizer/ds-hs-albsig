# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:23:34 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

 f = open("Bibel.txt").read()

 print(

     any(map(
             lambda zeile: 
                 list(map(
                         lambda zeile2: zeile2 if (len(zeile2)>2 and zeile2[1].isupper()) else False,
                         zeile.split()
                        )   
                    ) 
        ,f.splitlines() )
      )
    )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    