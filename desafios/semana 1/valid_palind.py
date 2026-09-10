def eh_palind(palavra):
    palavra_limpa = "".join(c for c in palavra if c.isalnum()).lower()
    esquerda = 0
    direita = len(palavra_limpa) - 1
    while esquerda < direita:
        if palavra_limpa[esquerda] != palavra_limpa[direita]:
            return False
        esquerda += 1
        direita -= 1
    return True

print(eh_palind("A man, a plan, a canal: Panama"))   # True
print(eh_palind("race a car"))                        # False
print(eh_palind(" "))                                  # True (string vazia depois de limpar)