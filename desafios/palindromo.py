'''def buscapalind(palavra):
    esquerda = 0
    direita = len(palavra) - 1
    while esquerda < direita:
        if palavra[esquerda] != palavra[direita]:
            return False
        esquerda += 1
        direita -= 1
    return True

print(buscapalind("arara"))    # True
print(buscapalind("banana"))   # False
print(buscapalind("a"))        # True (1 letra sozinha é sempre palíndromo)
print(buscapalind(""))         # True (string vazia)
'''
