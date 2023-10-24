def gerar(n): 
    if n == 0: 
        return[''] 
    elif n == 1: 
        return ['0', '1'] 
    else: 
        odd_zero_strings = [] 
        for s in gerar(n-2): 
            odd_zero_strings.append('0' + s) 
            odd_zero_strings.append('1' + s)
            return odd_zero_strings 
num_zeros = 5 
odd_zero_string  = gerar(num_zeros) 

for s in odd_zero_string: 
    print(s)