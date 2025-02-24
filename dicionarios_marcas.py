"""
Uma família tem 3 pessoas. Pretende um programa que utiliza um dicionário para registar
o nome de cada um e a marca do respetivo telemóvel e computador.
O programa deve indicar qual a marca mais comum e se algum membro da família tem somente
uma marca.
"""
dados = {}

for i in range(3):
    nome = input("Introduza o nome:")
    marca_telemovel = input("Introduza a marca do telemovel:")
    marca_computador = input("Introduza a marca do computador")
    print(dados)
    dados['nome'] = [nome]
    dados['marca_telemovel'] = [marca_telemovel]
    dados['marca_computador'] = [marca_computador]
    