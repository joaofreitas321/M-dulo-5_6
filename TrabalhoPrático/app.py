"""
Trabalho Prático - Módulo 5 e 6
--------------------------
Um programa para gerir um Jardim Zoológico
Requisitos funcionais:
    - Gestão dos animais (CRUD)
    - Gestão de funcionários (CRUD)
    - Estatísticas (animal mais velho, mais novo, funcionário mais velho e mais novo)
"""

import utils, animais, funcionarios


def MenuPrincipal():
    op = 0
    while op != 3:
        op = utils.Menu(["Animais","Funcionários","Sair"],"Menu principal")
        if op == 3:
            break
        if op == 1:
            animais.MenuAnimais()
        if op == 2:
            funcionarios.MenuFuncionarios()
        
if __name__=='__main__':
    MenuPrincipal()