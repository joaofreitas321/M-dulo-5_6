dicionario1 = {'a': 1,'b': 2,'c': 3}
dicionario2 = {'c': 4,'d': 5}

#juntar dois dicionários
dicionario1.update(dicionario2) #adicionar as chaves novas e atualiza o valor das chaves que já existem
print(dicionario1)
print(dicionario2)

dicionarioA = {'a': 1,'b': 2,'c': 3}
dicionarioB = {'c': 4,'d': 5}
# O operador | só existe a partir da versão 3.9 do Python
juntar = dicionarioA | dicionarioB
print(juntar)
print(dicionarioA)
print(dicionarioB)