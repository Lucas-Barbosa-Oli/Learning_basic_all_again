"""Verificação por contrato. Rode python conferir.py 01 nesta pasta."""
import copy
import importlib
import sys

CASOS = {
 '01': ('contar_positivos', [(([2,-1,0,5],),2), (([],),0), (([3,0,-2,7,7],),3), (([-1,-2],),0)]),
 '02': ('tem_duplicado', [(([3,1,3],),True), (([1,2],),False), (([],),False), (([0,0],),True)]),
 '03': ('frequencias', [(('aAb a',),{'a':2,'A':1,'b':1,' ':1}), (('',),{}), (('aaa',),{'a':3})]),
 '04': ('duas_somas', [(([2,7,11,15],9),True), (([3,3],6),True), (([3],6),False), (([],0),False), (([-2,4,1],2),True), (([1,2,3],100),False), (([1,2,3,4],5),True)]),
 '05': ('busca_binaria', [(([1,4,8],4),1), (([],4),-1), (([1],1),0), (([1,4,8],8),2), (([1,4,8],1),0), (([1,4,8],3),-1)]),
 '06': ('parenteses_validos', [(('(())',),True), ((')(',),False), (('',),True), (('(()',),False), (('()()',),True)]),
 '07': ('pares_maiuscula_minuscula', [(('bCcCbBce',),3), (('Aa',),1), (('aA',),0), (('AAaa',),4), (('AaAa',),3), (('AbBa',),1), (('ABab',),2), (('aabbAABB',),0), (('',),0), ((None,),-1), (('Aa1',),-1), (('1Aa',),-1), (('Aaé',),-1), (('A a',),-1), (('A'*100+'a'*100,),10000)]),
 '08': ('cache_precisa_buscar', [((999,0,1000),False), ((1000,0,1000),True), ((0,None,1000),True), ((1,0,1000,True),True), ((0,0,0),True), ((0,0,1000),False)]),
}

def par_valido(resultado, argumentos, existe):
    if not existe:
        return resultado is None
    if not isinstance(resultado, (list,tuple)) or len(resultado) != 2:
        return False
    i,j = resultado
    numeros,alvo = argumentos
    return (type(i) is int and type(j) is int and i != j and
            0 <= i < len(numeros) and 0 <= j < len(numeros) and
            numeros[i] + numeros[j] == alvo)

def verificar(modulo, codigo):
    nome, casos = CASOS[codigo]
    funcao = getattr(modulo,nome)
    for argumentos, esperado in casos:
        entrada = copy.deepcopy(argumentos)
        obtido = funcao(*entrada)
        assert entrada == argumentos, 'A funcao modificou a entrada'
        if codigo == '04':
            correto = par_valido(obtido,argumentos,esperado)
        else:
            correto = type(obtido) is type(esperado) and obtido == esperado
        assert correto, f'{nome}{argumentos!r}: recebido {obtido!r}; esperado {esperado!r}'
    return len(casos)

def main():
    validar = sys.argv[1:] == ['--validar-material']
    codigos = list(CASOS) if validar or sys.argv[1:] == ['todos'] else sys.argv[1:]
    if not codigos or any(c not in CASOS for c in codigos):
        print('Uso: python conferir.py 01 | todos | --validar-material')
        return 2
    modulo = importlib.import_module('gabarito' if validar else 'exercicios')
    falhas = 0
    for codigo in codigos:
        try:
            quantidade = verificar(modulo,codigo)
            print(f'{codigo}: OK ({quantidade} casos)')
        except NotImplementedError:
            print(f'{codigo}: INCOMPLETO - escreva sua tentativa em exercicios.py')
            falhas += 1
        except (AssertionError,Exception) as erro:
            print(f'{codigo}: REVISAR - {type(erro).__name__}: {erro}')
            falhas += 1
    if validar:
        print('Validacao das referencias do material; nao mede dominio do aluno.')
    return 1 if falhas else 0

if __name__ == '__main__':
    sys.exit(main())
