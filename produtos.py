"""
Referências entre dicionários e dicionários com arrays
"""
marca1 = {"nome":"nike","tipo":"calçado","país":"americano"}
marca2 = {"nome":"adidas","tipo":"roupa e calçado","país":"alemão"}
marca3 = {"nome":"mimosa","tipo":"leite","país":"portugal"}

produto1 = {"nome":"sapatilhas","preco":85.45,"marca":marca2}
#mostrar o país da marca
print(produto1["marca"]["país"])
marca2["país"] = "japão"
print(produto1)
produto2 = {"nome":"casaco","preco":100,"marca":marca2}
marca2 = {}   #cria um dicionário novo mas a informação dos produto1 e 2 continua a ser referanciada
print(produto1)
print(produto2)