"""
Um programa que implementa as funcionalidades de um dicionário de termos 
técnicos (palavra e definição)
Menu de opções (1.Adicionar definição;2.Listar todas as definições;3.Pesquisar a palavra
;4.Apagar;5.Terminar)
"""
from dicionario import configurar,Adicionar,Listar,Pesquisar,Apagar,em_teste

def menu():
    dicionario = {}
    if em_teste:
        configurar(dicionario)
    op = 0
    while op != 5:
        op = input("1.Adicionar\2.Listar\3.Pesquisar\4.Apagar\5.Terminar")
        if op == "1":
            Adicionar(dicionario)
        elif op == "2":
            Listar(dicionario)
        elif op == "3":
            Pesquisar(dicionario)
        elif op == "4":
            Apagar(dicionario)
        elif op == "5":
            print("Obrigado por utilizar o nosso programa.")
        else:
            print("Opção inválida")

if __name__=="__main__":
    menu()    