import math
def D(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:   
        return (n-1) * D(n - 1) + (n - 2) * D(n - 2)
        
num = int(input('digite um numero: '))
print(D(num))