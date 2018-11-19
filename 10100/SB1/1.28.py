# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:43:02 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from os import listdir

# 1.28a
 [  (len(fil),fil ) for fil in listdir('.') ]
 
 #1.28b
 [  fil  for fil in listdir('.') if fil.split('.')[-1]=='js' ]
 
 #1.28c
 
 # diese Variante liefert den Dateinamen mit den meisten Wörtern
 max(
    list(
        map(
            lambda x: (len(open(x).read().split()),x), 
            [ fil  for fil in listdir('.') if fil.split('.')[-1]=='js' ]
            )
        )
    )
        
# Alternative Variante (Andrej) 
# -> liefert die Anzahl der Wörter der längsten Zeile, die Zeile selbst und die Datei, in der die Zeile sich befindet
max(
    list(
        map(
            lambda x: ( max([(len(z.split()), z) for z in open(x, mode='r+b').read().splitlines()]), x ), 
            [ fil for fil in listdir('.') if isfile(f) ]
            )
        )
    )

# oder über List Comprehension (Andrej)

max(
    [
    ( max([(len(z.split()), z) for z in open(fil, mode='r+b').read().splitlines()]), fil ) 
     for fil in listdir('.') if isfile(fil)
    ]
    )

  
# 1.28d
max(
    list(
        map(
            lambda x: (x,len(list(filter(
                lambda y: y if len(y)>10 else False,
                open(x).read().split()
                )))),
            [ fil  for fil in listdir('.') if fil.split('.')[-1]=='js' ]
            )
        )
    )[0]

# In der Variante oben hat sich ein "Dreher" eingeschlichen. 
# Die max-Funktion wird zuerst lexikographisch auf den Dateinamen angewandt (auf das x im lambda-Ausdruck im Code) 
# und liefert deshalb nicht das korrekte Ergebnis. => Alternative (Andrej):

max(
    list(
        map(
            lambda x: (len(list(filter(
                lambda y: y if len(y)>10 else False, 
                open(x, mode='r+b').read().split() 
                ))), x),
            [ fil for fil in listdir('.') if isfile(fil) ]
            )
        )
    )[1]

# Oder über eine List Comprehension (Andrej):

max(
    [
    ( len([_ for w in open(fil, mode='r+b').read().split() if len(w)>10]), fil ) 
    for fil in listdir('.') if isfile(fil)
    ]
)[1]
