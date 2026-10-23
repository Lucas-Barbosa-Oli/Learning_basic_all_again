# Usar IA e continuar responsável pela solução

Treine dois modos. No primeiro, resolva a lógica central sem IA para desenvolver autonomia. No segundo, trabalhe com IA como ferramenta e revise cada sugestão. Em uma avaliação, siga as regras específicas comunicadas para aquela etapa; não presuma que uma autorização se estenda a todas as fases.

## Um ciclo de trabalho

1. Escreva o problema, exemplos, restrições e critério de sucesso.
2. Faça uma tentativa e identifique uma dúvida concreta.
3. Peça uma pista ou revisão direcionada, preservando sua tentativa.
4. Leia o código proposto, faça um rastreamento e tente quebrá-lo com um caso de borda.
5. Teste resultado, complexidade e suposições. Registre a sugestão aceita ou rejeitada.
6. Reconstrua a ideia sem a resposta aberta e explique ao grupo.

Prompt de treino: “Minha função deve retornar dois índices distintos. Não escreva a solução inteira. Dê um contraexemplo para minha tentativa e pergunte qual mudança eu faria.”

## Desafio de revisão

Uma IA sugeriu isto para Two Sum:

```python
def duas_somas(nums, alvo):
    for i, numero in enumerate(nums):
        if alvo - numero in nums:
            return [i, nums.index(alvo - numero)]
    return None
```

Antes de corrigir, rode mentalmente `[3],6` e `[3,3],6`. A função pode usar o mesmo índice duas vezes. A busca `in nums` e `index` pode percorrer a lista a cada iteração, levando a tempo O(n²). Peça à IA explicações e casos de teste, não aceite só uma resposta confiante. Um teste feliz como `[2,7],9` não identifica esses problemas.

## Colaboração

Faça perguntas sobre objetivo, dados e prioridade. Sugira um escopo pequeno que funcione. Divida tarefas por resultado, combine interfaces e reserve tempo para integrar. Convide outra pessoa a revisar o seu raciocínio. Apresente sua contribuição com precisão e dê crédito ao grupo.

Perguntas úteis: “What assumptions are we making?”, “Can we test an empty input?”, “What should we prioritize first?”, “Let me check if I understood your proposal.”

Registro: hipótese inicial; sugestão da IA; trecho alterado; teste que justificou a alteração; limite ainda existente. Não transforme geração de código em evidência automática de aprendizado.
