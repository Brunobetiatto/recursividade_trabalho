def pertence_W(s): 
    if s == "a" or s == "b" or s == "c": 
        return True 
    elif s[0] == 'a' and s[-1] == "c": 
        return pertence_W(s[1:-1]) 
    else: 
        return False 
cadeias = [ "a(b)c" , "a(a(b)c)c" , "a(abc)c" , "a(a(a(a)c)c)c" ,
"a(aacc)c"]  

for cadeia in cadeias: 
    if pertence_W(cadeia): 
        print(f'{cadeia} pertence a W') 
    else: 
        print(f'{cadeia} não pertence a W')