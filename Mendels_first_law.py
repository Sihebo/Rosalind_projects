a = 28
b = 21
c = 28

def probability(k, m, n):
    S = k + m + n
    Pk = k/S * (m/(S-1) + n/(S-1) + ((k-1)/(S-1)))
    Pm = m/S * (k/(S-1) + (n/(S-1)*1/2) + ((m-1)/(S-1)*3/4)) 
    Pn = n/S * (k/(S-1) + (m/(S-1)*1/2))
    Probab = Pk + Pm + Pn
    return Probab

print(probability(a, b, c))
