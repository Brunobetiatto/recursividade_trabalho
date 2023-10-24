
def P(n):
    if n == 1:
        return 1
    else:
        return n**2 * P(n - 1) + n - 1

num = int(input('digite um numero: '))
print(P(num))