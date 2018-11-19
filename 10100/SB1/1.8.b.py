# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:32:43 2018

@author: Sergej Schweizer 
mail:    sergej.schweizer@gmail.com
"""

"""
Suggested solution for the "Kontrolaufgabe 1.8 b"
"""

l1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2=[26, 2, 99, 65, 78, 34, 83, 70, 23, 66]

print(
    list(
        reversed(
            list(
                map(
                    lambda a,b,c,d : ((a*b)-(c*d)), \
                        l1,l2[1:]+[l2[0]],\
                        l1[1:]+[l1[0]],l2\
                    )
                )
                )
        )
    )


# solution 1.8
def mapL(f,*x):
    return list(map(f,*x))
#a
skalProd=lambda v1,v2:sum(map(lambda x,y:x*y,v1,v2))
#b
mat_v_prod=lambda m,v:mapL(lambda zeile: skalProd(zeile, v),m)
#c
mat_v_mat=lambda o,w: mapL(lambda spalte: mat_v_prod(o, spalte),w)
