def pertence_T(num): 
    if num == 2: 
        return True 
    elif num < 2: 
        return False 
    else: 
        return pertence_T(num - 3) or pertence_T(num / 2) 
    
numeros = [6 , 7 , 19 , 12] 

for numero in numeros: 
    if pertence_T(numero): 
        print(f'O numero {numero} pertence a t') 
    else: 
        print(f'o numero{numero} não percente a t')
