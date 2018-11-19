# Aufgabe 1.9 (a & b)
# Sergej Schweizer
# https://matrixcalc.org/ zum gegenprüfen


from operator import mul


m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[3,4,5],[5,6,7]]


def v_x_v(v1,v2): return list(map(mul, v1,v2 ))
def m_x_v(m,v): return list( map(lambda m_as_v : sum(v_x_v(m_as_v,v))   , m) )
def m_x_m(m1,m2): return list(map(lambda spalte: m_x_v(m1, spalte),list(map(list, zip(*m2))) ))



m_x_m(m1,m2)
[[22, 49, 76], [28, 64, 100], [34, 79, 124]]