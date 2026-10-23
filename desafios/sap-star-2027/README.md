# Preparação prática em Python

Trilha de estudo com fundamentos, estruturas de dados, complexidade, revisão de código de IA, colaboração e pitch em inglês. Os exercícios são autorais de treino; não representam questões oficiais de uma seleção.

## Comece aqui

1. Leia [o roteiro de 21 sessões](plano.md) e [a primeira aula](aula-01.md).
2. Abra [os desafios](desafios.md), faça uma simulação no papel e escreva sua tentativa em `exercicios.py`.
3. Nesta pasta, execute `python conferir.py 01` para verificar o exercício 01; troque pelo número desejado. Só é necessário Python 3 e a biblioteca padrão.
4. Registre sua tentativa, o erro e a próxima revisão em [progresso.md](progresso.md). Passe em uma variação sem consulta antes de marcar autonomia.
5. Leia [Big O e correções conceituais](big-o.md), pratique [revisão de IA](ia-e-colaboracao.md) e [pitch](pitch.md).

As funções iniciais estão intencionalmente incompletas. `INCOMPLETO` não é defeito do verificador: indica o que você ainda vai implementar. `python conferir.py --validar-material` verifica o gabarito do material, não o seu aprendizado. As respostas de referência ficam separadas em `gabarito.py`; abra depois da tentativa e da correção por pistas.

## Relação com o restante do repositório

Já há exercícios em `desafios/semana 1/` para soma, duplicados, duas somas e palíndromos, além de exemplos em `python/01-fundamentos/exemplos/`. Refaça-os sem copiar e compare com esta trilha. A presença do arquivo não comprova domínio. `duas_somas.py` contém várias versões entre aspas triplas: são textos comentados, não funções ativas. `containsDupli.py` usa `List`, que exige importação se executado isoladamente nas versões em que a anotação é avaliada.

O foco imediato é Python. JavaScript permanece como leitura dos exercícios anteriores. Frameworks, árvores, grafos e programação dinâmica ficam para depois da base e dos simulados, salvo nova necessidade concreta.

## Fontes

- [Tutorial Python](https://docs.python.org/3/tutorial/) — sintaxe e funções.
- [Estruturas de dados](https://docs.python.org/3/tutorial/datastructures.html) — listas, conjuntos e dicionários.
- [deque](https://docs.python.org/3/library/collections.html#collections.deque) — fila com operações nas extremidades.
- [bisect](https://docs.python.org/3/library/bisect.html) — busca em sequência ordenada e custo de inserção.
- [HackerRank Python](https://www.hackerrank.com/domains/python) e [LeetCode](https://leetcode.com/problemset/) — variações externas, selecionadas no plano.

Não copie e-mails, dados de recrutadores ou instruções privadas de avaliações para este repositório público. Os detalhes pessoais ficam no caderno privado de preparação.
