import math

n = int(input("Digite um numero para a aquestão 1.c: "))
def B(n):
  if n == 1:
    return 1
    
  elif n >= 2:
    n = B(n -1) + (n**2)
    return n

  else: 
    print("Erro")

print(B(n))


f = int(input("Digite um número para a questão 1.g: "))
def T(f):
  if f == 1:
    return 1

  elif f == 2:
    return 2

  elif f == 3:
    return 3
    
  elif f > 3:
    f = T(f - 1) + 2 * T(f - 2) + 3 * T(f - 3)
    return f
  
  else:
    print("Erro")

print(T(f))





x = int(input("Digite um número para a questão 8 (o numero da figuras, ex: figura 2 tem 3 pontos): "))

def F(x):
  if x == 1:
    return 1
    
  elif x == 2:
    return 3
    
  elif x == 3:
    return 6
    
  elif x == 4:
    return 10
    
  elif x > 4:
    x = (x**2 + x - 2) /2 + 1
    return x

print(F(x))
  

