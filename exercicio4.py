def pertence_M(num):
    if num == 2 or num == 3: 
        return True 
    elif num % 2 != 0:
        return False 
    else: 
        return pertence_M(num // 2) or pertence_M(num // 3) 
    
numeros = [ 6 , 9 , 16 , 21 , 26 , 54 , 72 , 218] 

for numero in numeros: 
    if pertence_M(numero): 
        print(f'{numero} pertence a M') 
    else: 
        print(f'{numero} não pertence a M')