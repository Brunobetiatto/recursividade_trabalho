def S(n):
    if n == 1:
        return 1
    else:
        return 3 * S(n- 1)
    
num = int(input('digite uma posição na sequencia: '))
print(S(num))