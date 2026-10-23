"""Referência para corrigir depois da tentativa; não representa código do aluno."""

def contar_positivos(numeros):
    total = 0
    for numero in numeros:
        if numero > 0:
            total += 1
    return total

def tem_duplicado(numeros):
    vistos = set()
    for numero in numeros:
        if numero in vistos:
            return True
        vistos.add(numero)
    return False

def frequencias(texto):
    contagem = {}
    for letra in texto:
        contagem[letra] = contagem.get(letra, 0) + 1
    return contagem

def duas_somas(numeros, alvo):
    vistos = {}
    for indice, numero in enumerate(numeros):
        complemento = alvo - numero
        if complemento in vistos:
            return [vistos[complemento], indice]
        vistos[numero] = indice
    return None

def busca_binaria(numeros, alvo):
    esquerda, direita = 0, len(numeros) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if numeros[meio] == alvo:
            return meio
        if numeros[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def parenteses_validos(texto):
    saldo = 0
    for caractere in texto:
        saldo += 1 if caractere == '(' else -1
        if saldo < 0:
            return False
    return saldo == 0

def pares_maiuscula_minuscula(texto):
    if not isinstance(texto, str):
        return -1
    contagem = {}
    total = 0
    for letra in texto:
        if 'A' <= letra <= 'Z':
            contagem[letra] = contagem.get(letra, 0) + 1
        elif 'a' <= letra <= 'z':
            total += contagem.get(letra.upper(), 0)
        else:
            return -1
    return total

def cache_precisa_buscar(agora, salvo_em, ttl, forcar=False):
    return salvo_em is None or agora - salvo_em >= ttl or forcar is True
