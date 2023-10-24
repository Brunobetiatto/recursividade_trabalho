#W(1) = 2
#W(2) = 5
#W(n) = W(n – 1)*W(n – 2), para n > 2 


def w(n):
    if n == 1: 
        return 2 
    elif n == 2: 
        return 5  
    else: 
        return w(n - 1) * w(n - 2) 

num = int(input("digite um numero: ")) 

print(w(num))
    
     
    