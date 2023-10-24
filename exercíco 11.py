def Rotina(L, j):
  global count
  if j == 1:
      return L
  max_index = L.index(max(L[:j]))
  L[max_index], L[j - 1] = L[j - 1], L[max_index]
  count += 1
  return Rotina(L, j - 1)


L = [3, 7, 4, 2, 6]
count = 0


resultado = Rotina(L, 5)

print("Lista final:", resultado)
print("Total de chamadas realizadas à função:", count)

