"""Crie um tuple com os nomes dos meses do ano."""

meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho", \
         "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
print(meses)

"""Mostrar o terceiro mês do ano"""

print(meses[2])

"""Obtenha o tuple dos meses de verão (junho,julho,agosto,setembro)."""

verao = meses[5:9]
print(verao)

"""Verifique se "Junho está presente no tuplo de meses de verão."""

if "Junho" in verao:
    print("Junho faz parte de verão")
else:
    print("Junho não faz parte do verão")

"""Listar os meses por ordem alfabética"""

meses_ordenados = sorted(meses)
print(meses_ordenados)

"""Mostrar os meses cujo nome começa por J"""

for mes in meses:
    if mes[0] == "J":
        print(mes)

"""Mostrar o mês(es) com o maior nome"""

maior = meses[0]

for mes in meses:
    if len(maior) < len(mes):
        maior = mes
print(maior)