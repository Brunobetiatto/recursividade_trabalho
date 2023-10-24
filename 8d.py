def S(n):
    if n == 1:
        return 'p'
    elif n ==2:
        return 'p - q'
    elif n == 3:
        return 'p + q'
    else:
        return S(n - 2) + 'q'
        

        
num = int(input('digite uma posição: '))
print(S(num))