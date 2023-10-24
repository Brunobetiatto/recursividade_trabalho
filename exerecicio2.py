#an = a1 . q(n-1) 

def termo_n(a1, r, n): 
    if n == 1: 
        return a1 
    else: 
        return r * termo_n(a1, r, n-1)
a1 = 2 
r = 3 
n = 2

resultado = termo_n(a1, r, n) 


print(resultado)
