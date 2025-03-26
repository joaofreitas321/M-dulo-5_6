dicionario = {123:{"Nome":"Carlos","Cidade":"Viseu","Visitas":22},
              124:{"Nome":"Paula","Cidade":"Viseu","Visitas":44},
              125:{"Nome":"Filipa","Cidade":"Porto","Visitas":67},
              126:{"Nome":"Rui","Cidade":"Lisboa","Visitas":35},
              127:{"Nome":"Fernando","Cidade":"Porto","Visitas":165}
              }

for cliente in dicionario:
    print(cliente)
    for visitas in dicionario[cliente]:
        print(f"{visitas} - {dicionario[cliente][visitas]}")

codigo = int(input("Código:"))
print(dicionario[codigo]["Visitas"])

maior = 0
cidade_maior = ""

for chave in dicionario:
    temp_cidade = dicionario[chave]['Cidade']
    nr_visitas = dicionario[chave]['Visitas']
    for codigo in dicionario[chave]:
        if temp_cidade == dicionario[codigo]['Cidade']:
            nr_visitas += dicionario[codigo]['Visitas']
    if nr_visitas > maior:
        cidade_maior = temp_cidade
        maior = nr_visitas
print(cidade_maior)