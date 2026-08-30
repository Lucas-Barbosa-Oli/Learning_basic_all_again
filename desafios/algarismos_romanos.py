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

    print(romano_para_inteiro("III"))  # 3
    print(romano_para_inteiro("MCMXCIV"))  # 1994
