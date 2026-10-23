# Exercícios autorais de preparação

Contrato comum: quando não houver regra de validação explícita, as entradas respeitam os tipos descritos. Não modifique as entradas. Retorne valores em vez de apenas imprimir. Primeiro descreva a solução simples; depois justifique a estrutura escolhida.

| ID | Função | Contrato e exemplos | Meta após compreender |
|---|---|---|---|
| 01 | contar_positivos(numeros) | Lista de inteiros. `[2,-1,0,5]` → 2; `[]` → 0. | O(n) tempo, O(1) auxiliar |
| 02 | tem_duplicado(numeros) | Lista de inteiros. `[3,1,3]` → True; `[1,2]` → False. | O(n) esperado, O(n) auxiliar |
| 03 | frequencias(texto) | String; distinguir caixa e contar espaços. `"aAb a"` → `{'a':2,'A':1,'b':1,' ':1}`; vazio → `{}`. | O(n) esperado, O(k) auxiliar |
| 04 | duas_somas(numeros, alvo) | Retorne dois índices distintos cuja soma é alvo, ou None. Qualquer par correto é aceito. `[3,3],6` → `[0,1]`; `[3],6` → None. | O(n) esperado, O(n) auxiliar |
| 05 | busca_binaria(numeros, alvo) | Lista já ordenada em ordem crescente e sem repetição; índice do alvo ou -1. `[1,4,8],4` → 1. Não ordenar dentro da função. | O(log n), O(1) auxiliar |
| 06 | parenteses_validos(texto) | String só com `(` e `)`. `"(())"` → True; `")("` → False; vazio → True. Pode usar contador; como variação, aceite também `[]` e `{}` usando pilha. | O(n), O(1) na versão só parênteses |
| 07 | pares_maiuscula_minuscula(texto) | Conte pares da mesma letra inglesa com maiúscula antes da minúscula. `"AaAa"` → 3; `"AbBa"` → 1; vazio → 0; não string ou caractere fora de A-Z/a-z → -1. `isalpha()` sozinho aceita letras além de ASCII. | O(n), até 26 contadores |
| 08 | cache_precisa_buscar(agora, salvo_em, ttl, forcar=False) | Tempos não negativos na mesma unidade; salvo_em pode ser None; ttl ≥ 0. Buscar se ausente, idade ≥ ttl ou forcar=True. `(1000,0,1000)` → True; `(999,0,1000)` → False. Não usar relógio real. | O(1), O(1) auxiliar |

Depois de cada tarefa, responda: qual é n? Quais casos de borda testei? A entrada muda? Qual o tempo e o espaço auxiliar? Usei IA, pista ou consulta? Consigo resolver uma variação amanhã?

## Mini caso para trabalhar em grupo

Uma equipe recebe chamados de suporte como objetos com `id`, `categoria`, `prioridade` e `criado_em`. Proponha um protótipo que remova IDs repetidos preservando a primeira ocorrência, conte chamados por categoria e selecione os três mais prioritários. Prioridade menor significa maior urgência; desempate pelo menor criado_em e depois id. Categorias são textos, datas são números e IDs são inteiros. Chamado com campo ausente deve ser rejeitado e contado separadamente. Retorne dados estruturados e explique o benefício para quem atende os chamados.

Exemplo: IDs `[1,2,1,3]`, todos válidos, deixam três registros e uma repetição. Se as prioridades de 1,2,3 forem 2,1,3, a ordem será 2,1,3. Decida explicitamente o que acontece com registros incompletos antes de deduplicar: no treino, valide primeiro e deduplique somente válidos.

Sessão de 60 minutos: 5 para perguntas e divisão do trabalho, 10 para modelo e exemplos, 20 para protótipo, 10 para testes e revisão, 10 para pitch e 5 para perguntas. IA pode ajudar nesta simulação, mas mantenha registro de suas sugestões e do que foi verificado. Faça outra sessão implementando a parte central sem ajuda. Esse formato é uma proposta de treino, não a agenda oficial do evento.
