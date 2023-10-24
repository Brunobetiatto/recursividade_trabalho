def numero_triangular(n): 
    if n == 0: 
        return 0
    else: 
        return n + numero_triangular(n-1) 

n = int(input("digite o valor de n: ")) 

numerotriangulo = numero_triangular(n) 

print(f'O {n}-enimo numero tringular é: {numerotriangulo}')