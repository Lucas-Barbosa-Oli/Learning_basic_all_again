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

# Capítulo2

Arrays: espaços na memória para salvar informações, só que é dependente de um espaço correto na memória, se precisar de mais espaços do que foi disponibilizado, terá de se realocar.
Lista encadeada: usa espaços na memória referenciando sempre ao próximo, ou seja, mais disponibilidades para listas e menos dores de cabeça.

Arrays são ótimos se você deseja ler elementos aleatórios, pois pode encontrar qualquer elemento instantaneamente em um array.
Na lista aleatória, como os números são referenciados aleatoriamente, tem que ir de um em um para saber onde cada um se encontra para daí sim, achar o item de escolha.

Tempo de execução de arrays e lista
            leitura   O(1)  |  O(n)
            inserção  O(n)  |  O(1)

O que seria melhor para usar em um algoritmo de finanças onde você coloca os itens e depois quer vê-los?
Um array pode ser usado para isso se não quiser deixar ordenado, pois vai ser adicionado um item após o outro na questão do uso mas,
Caso queira usar um to do list por exemplo, onde as coisas devem ter ordem, o melhor seria usar uma linked list, pois assim é só mudar o ponteiro
Para uma outra etapa e assim seguir, caso fosse usado o array, aí teria que ser inserido no meio do array, os índices deveriam ser alterados e caso não
Haja espaço na memória, teria que realocá-lo de lugar para assim caber todo o array

"""
Comparativo: Array (lista dinâmica) x Lista Encadeada (Linked List)

Cenário 1: Extrato financeiro usando ARRAY
- Itens são sempre adicionados no final (append).
- Não precisa reordenar nada, só cresce a lista.
- Se a capacidade interna acabar, o Python realoca automaticamente
  (isso também acontece em outras linguagens, como ArrayList em Java).
"""

class ExtratoFinanceiro:
    def __init__(self):
        self.transacoes = []  # implementado como array dinâmico

    def adicionar_transacao(self, descricao, valor):
        # Inserção no final: O(1) amortizado, sem precisar mexer em outros índices
        self.transacoes.append({"descricao": descricao, "valor": valor})

    def exibir(self):
        for i, t in enumerate(self.transacoes):
            print(f"[{i}] {t['descricao']}: R$ {t['valor']:.2f}")


"""
Cenário 2: To-do list usando LISTA ENCADEADA
- Os itens têm uma ORDEM (etapas de uma tarefa, por exemplo).
- Inserir no meio da lista só exige alterar os ponteiros dos nós vizinhos,
  não há necessidade de deslocar índices nem realocar memória.
"""

class No:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        self.proximo = None  # ponteiro para o próximo nó


class ToDoList:
    def __init__(self):
        self.cabeca = None  # primeiro nó da lista

    def adicionar_no_fim(self, tarefa):
        novo_no = No(tarefa)
        if self.cabeca is None:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def inserir_apos(self, tarefa_referencia, nova_tarefa):
        """
        Insere uma nova tarefa logo depois de uma tarefa existente.
        Repare: só mexemos em DOIS ponteiros, independente do tamanho da lista.
        Não há deslocamento de índices nem realocação de memória.
        """
        atual = self.cabeca
        while atual and atual.tarefa != tarefa_referencia:
            atual = atual.proximo

        if atual is None:
            print(f"Tarefa '{tarefa_referencia}' não encontrada.")
            return

        novo_no = No(nova_tarefa)
        novo_no.proximo = atual.proximo  # o novo nó aponta para quem vinha depois
        atual.proximo = novo_no          # a tarefa de referência aponta para o novo nó

    def exibir(self):
        atual = self.cabeca
        posicao = 0
        while atual:
            print(f"[{posicao}] {atual.tarefa}")
            atual = atual.proximo
            posicao += 1


if __name__ == "__main__":
    print("=== Extrato financeiro (Array) ===")
    extrato = ExtratoFinanceiro()
    extrato.adicionar_transacao("Salário", 3000.00)
    extrato.adicionar_transacao("Aluguel", -1200.00)
    extrato.adicionar_transacao("Mercado", -450.00)
    extrato.exibir()

    print("\n=== To-do list (Lista Encadeada) ===")
    lista = ToDoList()
    lista.adicionar_no_fim("Levantar requisitos")
    lista.adicionar_no_fim("Codificar")
    lista.adicionar_no_fim("Publicar")

    print("Antes de inserir 'Testar':")
    lista.exibir()

    # Inserindo "Testar" entre "Codificar" e "Publicar" -> só muda ponteiro
    lista.inserir_apos("Codificar", "Testar")

    print("\nDepois de inserir 'Testar' (sem deslocar nada, só mudou o ponteiro):")
    lista.exibir()