def S(n):
    a = 'a'
    b = 'b'
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return a + "+" + b
    else:
        r = S(n -1) + S(n -2)
        p = S(n -1) + S(n -2)
        x = r.find("a",1)
        y = p.find("b",1)
        return x
        
         


num = int(input('digite uma posição: '))
print(S(num))