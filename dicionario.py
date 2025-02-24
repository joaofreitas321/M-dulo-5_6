def Adicionar(dicionario):
    palavra = input("Introduza a chave que pretende adicionar:")
    if palavra in dicionario:
        op = input("Essa palavra já existe no dicionário. Pretende alterar?")
        if op == 'n':
            return
    definicao = input("Introduza a definição da palavra indicada?")
    dicionario[palavra] = definicao
    print("Palavra adicionada/atualizado com sucesso")

def Listar(dicionario):
    op = input("Pretende visualizar por ordem alfabética?")
    if op != 's':
        for chave, valor in dicionario.items():
            print(f"{chave} -> {valor}")
    else:
        #ordenar as chaves
        chaves = dicionario.keys()
        chaves = sorted(chaves)
        #percorrer as chaves ordenadas e mostrar o valor correspondente
        for chave in chaves:
            print(f"{chave} -> {dicionario[chave]}")        

def Pesquisar(dicionario):
    #ler a palavra a pesquisar
    chave_pesquisar = input("Introduza a palavra, ou parte da palavra, a pesquisar?")
    #percorrer o dicionário
    for chave, valor in dicionario.items():
        #se a palavra existir no início da chave mostrar o valor
        if chave_pesquisar == chave[:len(chave_pesquisar)]:    #slicing para só comparar o início da chave
            print(f"{chave} -> {valor}")

def Apagar(dicionario):
    #ler a palavra a pesquisar
    chave_apagar = input("Introduza a palavra, ou parte da palavra, a apagar?")
    #percorrer o dicionário
    for chave, valor in dicionario.items():
        #se a palavra existir no início da chave mostrar o valor
        if chave_apagar == chave[:len(chave_apagar)]:    #slicing para só comparar o início da chave
            print(f"{chave} -> {valor}")
            op = input("Pretende remover esta palavra do dicionário?")
            if op == 's':
                del dicionario[chave]
                return #uma vez que o dicionário foi alterado não podemos continuar a ciclo


def configurar(dicionario):
    dicionario['pera'] = 'fruta'
    dicionario['pc'] = 'computador pessoal'
    dicionario['bicicleta'] = 'meio de transporte'
#se o programa está em desenvolvimento dever ser True
#se está terminado (em produção) deve ser False
em_teste = True