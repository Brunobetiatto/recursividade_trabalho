def pertence_S(s):
    if s == "a" or s == "b":
        return True
    elif s[0] == "a":
        return pertence_S(s[1:])
    elif s[0] == "b":
        return pertence_S(s[1:])
    else:
        return False

# Lista de cadeias para verificar
cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]

for cadeia in cadeias:
    if pertence_S(cadeia):
        print(f'A cadeia "{cadeia}" pertence a S.')
    else:
        print(f'A cadeia "{cadeia}" NÃO pertence a S.')
