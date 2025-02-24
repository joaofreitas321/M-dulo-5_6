"""
Um programa que utiliza um dicionário para guardar os professores
responsáveis pelas salas do torneio tecla e o nº de alunos que cada
sala vai ter. As salas são C5, C6, C7, C8 e o dicionário deve guardar
o nome do professor e o nº de alunos de cada uma.
"""

dados = {
        'C5': {'professor': 'p1','n_alunos':10},
        'C6': {'professor': 'p2','n_alunos':14},
        'C7': {'professor': 'p3','n_alunos':12},
        'C8': {'professor': 'p4','n_alunos':9}
        }
#ler os dados dos professores e alunos por sala
for sala in dados:
    professor = input(f"Introduza o nome do professor responsável pela sala {sala}")
    nr_alunos = int(input(f"Introduza o nº de alunos para a sala {sala}"))
    #atualizar o nome do professor
    dados[sala]['professor'] = professor
    #atualizar o nº de alunos
    dados[sala]['n_alunos'] = nr_alunos
#listar os dados
for sala in dados:
    print(f"Sala:{sala} -> Professor responsáve: {dados[sala]['professor']} Nº de alunos: {dados[sala]['n_alunos']}")
#adicionar uma sala, um professor e o nº de alunos introduzidos pelo utilizador
nova_sala = input("Introduza a nova sala:")
novo_professor = input("Introduza o nome do novo professor responsável:")
novos_alunos = input("Introduza quantos alunos vão para a nova sala:")
dados[nova_sala] = {'professor':novo_professor,'n_alunos':novos_alunos}
#remover a sala C5 do dicionário
del dados['C5']
print(dados)