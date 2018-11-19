#1.11 4

max(list(map(lambda satz:  (satz,sum(list(map(len, satz.split()))) / len(satz.split()) if len(satz)!=0 else 0),     b.splitlines() )))