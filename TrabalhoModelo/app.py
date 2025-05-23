"""
Trabalho Modelo - Módulo 6
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requisitos funcionais:
    - Gestão livros (CRUD)
    - Gestão leitores (CRUD)
    - Empréstimos e devoluções
    - Estatísticas (empréstimos em atraso, top livros, top mês, top leitores, ...)
"""
import utils, livros, leitores, emprestimos, estatisticas
import os

#Deve estar True quando em teses e False quando em produção
DEBUG = True

def MenuPrincipal():
    if DEBUG:
        livros.Configurar()
        leitores.Configurar()
    op = 0
    while op != 5:
        os.system("cls")
        op = utils.Menu(["Livros","Leitores","Empréstimos/Devoluções","Estatísticas","Sair"],"Menu principal")
        if op == 5:
            break
        if op == 1:
            livros.MenuLivros()
        if op == 2:
            leitores.MenuLeitores()
        if op == 3:
            emprestimos.MenuEmprestimos()
        if op == 4:
            estatisticas.MenuEstatisticas()

if __name__=='__main__':
    MenuPrincipal()