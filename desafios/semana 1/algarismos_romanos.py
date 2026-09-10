"""Desafio: converter uma representação romana para inteiro."""


def romano_para_inteiro(s):
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for i, n in enumerate(s):
        valor_atual = valores[n]
        if i + 1 < len(s) and valor_atual < valores[s[i + 1]]:
            total = total - valor_atual
        else:
            total = total + valor_atual
    return total

print(romano_para_inteiro("III"))       # 3
print(romano_para_inteiro("LVIII"))     # 58
print(romano_para_inteiro("MCMXCIV"))   # 1994