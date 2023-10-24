#A(1) = 2
#A(n) = A(n – 1)-1 , para n > 2  

def a(n): 
   if n == 2 : 
        return 2
   elif n >= 2: 
        return a(n - 1)**2   
    
num = int(input("digite um numero: ")) 

print(a(num))








