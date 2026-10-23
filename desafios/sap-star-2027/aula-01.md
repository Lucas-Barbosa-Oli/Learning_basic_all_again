# Aula 1 Contar valores positivos

Objetivo: acompanhar uma variável ao percorrer uma lista e distinguir `print` de `return`. Faça a previsão antes de executar.

```python
def contar_positivos(numeros):
    total = 0
    for numero in numeros:
        if numero > 0:
            total += 1
    return total
```

`def` define a função. `numeros` é o parâmetro que receberá a lista. Os dois-pontos abrem um bloco e os espaços à esquerda delimitam os blocos. `total` começa em zero. `for` entrega um número de cada vez. `if` só executa a soma quando o valor é maior que zero. `+= 1` aumenta o contador. `return` entrega o resultado a quem chamou, depois de terminar o laço; não fica dentro do `if`.

Na entrada `[2, -1, 0, 5]`, os valores do contador após cada item são 1, 1, 1 e 2. Zero não é positivo. A lista vazia devolve 0 porque o laço não executa e o contador permanece zero.

`print(total)` só mostra algo na tela. Uma função que apenas imprime, sem `return`, devolve `None`. Nossos testes verificam o retorno.

## Sua vez

Sem executar: qual seria o retorno para `[3, 0, -2, 7, 7]`? Escreva o valor de `total` após cada item. Depois feche o exemplo, implemente `contar_positivos` em `exercicios.py` e rode `python conferir.py 01`.

Variação: conte negativos. Depois explique o que mudaria para contar valores maiores ou iguais a zero. Traga sua tentativa ao chat, inclusive se incompleta; peça esclarecimento sobre qualquer símbolo.

## Primeiro contato com Big O

Se a lista tem n números, o laço visita n números. Duplicar o tamanho dobra aproximadamente o número de visitas: tempo O(n). O contador ocupa uma quantidade fixa de variáveis: espaço auxiliar O(1), sem contar a entrada. Big O descreve crescimento; não prevê segundos.

Leitura principal: [Funções e controle de fluxo no Python](https://docs.python.org/3/tutorial/controlflow.html). Próxima aula: [estruturas e Big O](big-o.md).
