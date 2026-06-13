def pesquisa_binaria(lista, item):
    baixo = 0 # índice do primeiro elemento
    alto = len(lista) - 1 # índice do último elemento, onde pega len = tamanho da lista e subtrai 1 pra pegar o índice do último elemento

    while baixo <= alto:
        meio = (baixo + alto) // 2 # precisa usar //2 e não /2 porque o resultado precisa ser um número inteiro, e o // é a divisão inteira
        # enquanto /2 cria um float que não roda o código
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))