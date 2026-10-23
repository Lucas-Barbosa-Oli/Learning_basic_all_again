# Estruturas de dados e Big O com exemplos

Big O descreve um limite de crescimento conforme a entrada aumenta. Sempre diga se analisa pior caso, caso médio ou custo amortizado; a notação por si só não significa obrigatoriamente pior caso. Identifique n e o custo das operações internas. Tempo e espaço auxiliar são análises separadas.

| Custo | Exemplo | Se n dobra |
|---|---|---|
| O(1) | Acessar um índice válido de lista | Quantidade de passos não cresce com n |
| O(log n) | Busca binária em lista já ordenada | Acrescenta aproximadamente uma divisão ao meio |
| O(n) | Percorrer uma lista | Visitas aproximadamente dobram |
| O(n log n) | Ordenação eficiente por comparações | Cresce um pouco mais que o dobro |
| O(n²) | Comparar cada item com todos os posteriores | Comparações aproximadamente quadruplicam |

Dois laços consecutivos de n iterações fazem 2n passos: O(n). Dois laços aninhados que percorrem n itens cada fazem n²: O(n²). Mas aninhamento sozinho não determina o custo: se o laço interno sempre executa três vezes, continua O(n). `x in lista` dentro de um laço pode tornar a solução quadrática mesmo que só um `for` esteja visível.

## Escolher uma estrutura

`list`: sequência com índice; leitura por índice O(1), busca por valor O(n), append O(1) amortizado e inserção no início O(n) na implementação usual do CPython.

`set`: coleção sem duplicatas, útil para “já vi?”. Busca e inserção têm custo médio/esperado O(1), podendo degradar no pior caso. Não guarda o índice de cada ocorrência.

`dict`: associa chave a valor, útil para frequências e número → índice no Two Sum. Mesma ressalva de custo médio das tabelas hash. Não diga que o algoritmo tem garantia de pior caso O(n) apenas porque usa dict.

Pilha: use append e pop no fim de uma lista. Fila: use deque e popleft para retirar do início sem deslocar toda a lista. Comece com essas quatro estruturas antes de árvores e grafos.

## Ajustes das anotações antigas

Em `algoritmos/README.md`, “log²n” na descrição inicial da busca binária deve ser lido como log₂(n), e seu custo é O(log n), não O((log n)²). Em 1024 itens, são cerca de 10 reduções até uma região de tamanho 1; a contagem exata de comparações depende da implementação.

Quicksort costuma ter tempo médio O(n log n), mas o pior caso é O(n²). Não o use como exemplo de garantia universal O(n log n).

Inserir em lista encadeada é O(1) quando você já tem o nó e os ponteiros necessários. Procurar o nó pelo valor pode levar O(n); o método `inserir_apos` das anotações faz essa procura. Lista encadeada não é automaticamente melhor sempre que há ordem.

A enumeração de rotas do caixeiro-viajante pode ter crescimento fatorial, mas “não existem outros algoritmos” é incorreto: há algoritmos exatos melhores que enumerar todas as permutações, heurísticas e aproximações em versões específicas. Isso fica fora da prioridade atual.

## Perguntas para praticar

Qual o custo de `for x in numeros: if x in outra_lista: ...` se ambas têm n itens? E se outra_lista virar um set previamente construído? Inclua o custo e a memória de construir o conjunto. Por que ordenar antes de fazer uma única busca pode custar mais que procurar linearmente? Por que `texto[::-1]` cria espaço O(n)?

Fontes: [estruturas Python](https://docs.python.org/3/tutorial/datastructures.html), [busca e inserção com bisect](https://docs.python.org/3/library/bisect.html), [deque](https://docs.python.org/3/library/collections.html#collections.deque), [algoritmos MIT](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/). As operações descritas pressupõem objetos com comparação/hash de custo constante para simplificar os exercícios.
