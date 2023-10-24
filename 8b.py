def S(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return 1 / (2* S(n - 1))
num = int(input('digite uma posição na sequencia: '))
print(S(num))