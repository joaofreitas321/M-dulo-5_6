"""Calcular quantos carros de cada marca existem num array guardando num 
dicionário a marca e nº de carros
p.e.:
    {'bmw':2,
    'tesla':2,
    'peugeot':1,
    ...}
"""
import numpy as np

carros = np.array(["tesla","volvo","bmw","peugeot","tesla","mercedes","ford","bmw"])
marcas = {}

#ciclo para percorrer o array das marcas
for carro in carros:
    #verificar se a marca já existe no dicionário
    #if carro in marcas:
    #    marcas[carro] = marcas[carro] + 1
    #else:
    #    marcas[carro] = 1
    marcas[carro] = marcas.get(carro,0) + 1

print(marcas)    