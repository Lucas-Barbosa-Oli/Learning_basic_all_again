# Algoritmos e Estruturas de Dados

Conteúdo transversal — resolva o mesmo problema em diferentes linguagens quando fizer sentido.

## Tópicos

- [ ] Complexidade (Big O)
- [ ] Arrays e strings
- [ ] Linked lists
- [ ] Stacks e queues
- [ ] Hash maps / hash tables
- [ ] Árvores (BST, traversals)
- [ ] Grafos (BFS, DFS)
- [ ] Ordenação e busca
- [ ] Recursão e backtracking
- [ ] Programação dinâmica

## Organização sugerida

```
algoritmos/
├── 01-complexidade/
├── 02-arrays-strings/
├── 03-linked-lists/
└── ...
```

## Status

⬜ Não iniciado

# Anotações livro: Entendendo Algoritmos

# Capítulo 1

Busca Binária:

Forma rápida de achar números/ids dentro de um algoritmo "quebrando" a lista ao meio todas as vezes para achar o que procura, precisa de log²n.
Busca binária só funciona em listas ordenadas!!! Seja por ordem alfabética ou crescente/decrescente.

Notação Big O:

A notação Big O refere-se e estabelecee sempre o tempo de execução para a pior hipótese em um algoritmo, em muitos casos sendo o tempo de O(n), notação Big O acaba por metrificar esse tempo por execuções.
Alguns exemplos comuns de tempo de execução Big O:

O(log n), também conhecido como tempo logarítmico. Exemplo: pesquisa binária (rápido)
O(n), conhecido como tempo linear. Exemplo: pesquisa simples (pode ser rápido se a pesquisa feita for o primeiro index mas, pode ser também super demorado caso seja uma lista extensa e a procura seja no último item)
O(n * log n). Exemplo: um algoritmo rápido de ordenação, como a ordenação quicksort
O(n²). Exemplo: um algoritmo lento de ordenação, como a ordenação por seleção
O(n!). Exemplo: um algoritmo bastante lento, como o do caixeiro-viajante

Algoritmo do caixeiro-viajante é um algoritmo lento, que usa a notação O(n!), funciona bem com poucos números, mas muito mal com muitos mas,
não existem maneiras de se utilizar nenhum outro algoritmo e notação nesse caso, então é um caso que não tem solução

- Recapitulação:
    - A pesquisa binária é muito mais rápida do que a pesquisa simples.
    - O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rápido conforme os itens das listas aumentam.
    - A rapidez de um algoritmo não é medida em segundos!
    - O tempo de execução de um algoritmo é medido por meio de seu crescimento.
    - O tempo de execução dos algoritmos é expresso na notação Big O