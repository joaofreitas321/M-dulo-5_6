"""
Programa para gerir os livros de uma biblioteca e os seus empréstimos
"""
livros = ["livro 1","livro 2","livro 3","livro 4"]
emprestimos = []

livro = input("Qual o título do livro a emprestar:")
while livro != "":
    #avisar o utlizador quando o livro já está emprestado ou não existe
    if livro in livros:
        #remover da lista de livros para a lista de empréstimo
        livros.remove(livro)
        emprestimos.append(livro)
    #avisar o utlizador quando o livro já está emprestado ou não existe
    elif livro in emprestimos:
        print("Livro já foi emprestado")
    else:
        print("O livro não está disponível")
    #mostrar os livros e os empréstimos
    print(emprestimos,livro)
    if len(livros) == 0:
        print("Não tem mais livros para emprestar")
        break
    livro = input("Qual o livro a emprestar:")
#o programa deve terminar quando é inserido um título em branco ou quando não há mais livros para emprestar