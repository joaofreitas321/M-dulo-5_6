notas = {'Aluno1':{'PT':0,'Inglês':0,'Ai':0,'TIC':0,'Média':0},
         'Aluno2':{'PT':0,'Inglês':0,'AI':0,'TIC':0,'Média':0}
         }

for chave in notas:
    soma = 0
    for disciplina in notas[chave]:
        nota = int(input(f"Nota de {disciplina} de {chave}:"))
        notas[chave][disciplina] = nota
        soma = soma + nota
    media = soma / 4
    notas[chave]['Media'] = media
    print(f"A média do aluno {chave} é {media}")

media_total = (notas['Aluno1']['Media'] + notas['Aluno2']['Media']) / 2
print(media_total)

for aluno in notas:
    print(aluno)
    for disciplina in notas[aluno]:
        print(disciplina,notas[aluno][disciplina])