"""
Ler do utilizador uma frase e contar quantas palavras únicas tem a frase
"""
#ler o texto do utlizador
texto = input("Introduza uma frase:")
#lista das palavras
palavras = texto.split(" ")
#converter a lista em set
palavras_unicas = set(palavras)
#len para contar
print(f"A frase tem {len(palavras_unicas)} palavras únicas")