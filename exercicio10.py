def bacteria(n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 50000 
    else: 
        return bacteria(n - 1) * 3
    
n = 3
resultado = bacteria(n)

print(f'o {n}-numero de bacteria é {resultado}')


    