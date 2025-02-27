"""
Programa para sugerir uma aposta no euromilhões
Deve sortear 5 nº entre 1 e 50 sem repetições
e 2 nº entre 1 e 12 também sem repetir
"""
import random

numeros = []
estrelas = []

def sortear(numeros,quantos,maximo):
    while len(numeros) != quantos:
        numero = random.randint(1,maximo)
        if numero not in numeros:
            numeros.append(numero)
numeros.sort()

sortear(numeros,5,50)
sortear(estrelas,2,12)
print(numeros)
print(estrelas)