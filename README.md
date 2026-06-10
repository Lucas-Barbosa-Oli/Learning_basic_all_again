# Learning Basic All Again

Repositório pessoal de estudos para reaprender programação do zero ao nível mais avançado que eu conseguir alcançar — com foco em **Python**, **JavaScript**, **Java**, **Go** e seus ecossistemas de frameworks e ferramentas.

> *"Não é sobre saber tudo. É sobre construir base sólida, praticar com consistência e subir de nível de forma intencional."*

---

## Objetivo

Este repositório documenta minha jornada de reaprendizado. Cada pasta representa um tópico, exercício ou mini-projeto. O foco é:

- **Fundamentos sólidos** — sintaxe, tipos, estruturas de dados, algoritmos, paradigmas
- **Prática constante** — exercícios, desafios e projetos pequenos antes de projetos grandes
- **Profundidade progressiva** — do básico ao avançado, sem pular etapas
- **Ecossistema completo** — linguagem + frameworks + ferramentas + boas práticas

---

## Linguagens e frameworks

### Python

| Nível | Tópicos |
|-------|---------|
| **Básico** | Sintaxe, tipos, estruturas de controle, funções, listas/dicts/sets, arquivos, exceções |
| **Intermediário** | OOP, comprehensions, decorators, generators, `typing`, módulos e pacotes, testes com `pytest` |
| **Avançado** | Async/await, metaclasses, context managers, performance, design patterns, arquitetura |
| **Frameworks & libs** | FastAPI, Django, Flask, Pandas, NumPy, SQLAlchemy, Celery, Streamlit |

### JavaScript

| Nível | Tópicos |
|-------|---------|
| **Básico** | Variáveis, funções, arrays, objetos, DOM, eventos, ES6+ (arrow functions, destructuring, modules) |
| **Intermediário** | Promises, async/await, fetch API, closures, prototypes, npm, bundlers |
| **Avançado** | Event loop, performance, patterns, TypeScript, testes (Jest/Vitest), Node.js internals |
| **Frameworks & libs** | React, Next.js, Vue, Express, NestJS, Vite |

### Java

| Nível | Tópicos |
|-------|---------|
| **Básico** | Sintaxe, tipos primitivos, classes, herança, interfaces, collections, exceções |
| **Intermediário** | Generics, streams, lambdas, I/O, JDBC, Maven/Gradle, JUnit |
| **Avançado** | Concorrência, JVM, design patterns, arquitetura em camadas, microserviços |
| **Frameworks & libs** | Spring Boot, Spring Data, Hibernate, Quarkus, JUnit 5, Mockito |

### Go

| Nível | Tópicos |
|-------|---------|
| **Básico** | Sintaxe, tipos, structs, métodos, interfaces, slices, maps, error handling |
| **Intermediário** | Goroutines, channels, packages, testing, `context`, standard library |
| **Avançado** | Concorrência avançada, profiling, design patterns, arquitetura de serviços |
| **Frameworks & libs** | Gin, Echo, Fiber, GORM, Cobra, Viper |

---

## Estrutura do repositório

```
Learning_basic_all_again/
├── python/
│   ├── 01-fundamentos/
│   ├── 02-intermediario/
│   ├── 03-avancado/
│   ├── frameworks/
│   │   ├── fastapi/
│   │   ├── django/
│   │   └── flask/
│   └── projetos/
├── javascript/
│   ├── 01-fundamentos/
│   ├── 02-intermediario/
│   ├── 03-avancado/
│   ├── frameworks/
│   │   ├── react/
│   │   ├── nextjs/
│   │   └── node-express/
│   └── projetos/
├── java/
│   ├── 01-fundamentos/
│   ├── 02-intermediario/
│   ├── 03-avancado/
│   ├── frameworks/
│   │   └── spring-boot/
│   └── projetos/
├── go/
│   ├── 01-fundamentos/
│   ├── 02-intermediario/
│   ├── 03-avancado/
│   ├── frameworks/
│   │   └── gin/
│   └── projetos/
├── algoritmos/          # Estruturas de dados e algoritmos (todas as linguagens)
├── desafios/            # Exercícios de plataformas (LeetCode, HackerRank, etc.)
└── notas/               # Anotações, resumos e referências
```

Cada pasta de estudo segue um padrão simples:

```
01-fundamentos/
├── README.md        # O que estou aprendendo neste módulo
├── exercicios/      # Exercícios resolvidos
├── exemplos/        # Código de referência e experimentos
└── notas.md         # Resumo do que aprendi
```

---

## Roadmap de aprendizado

### Fase 1 — Fundamentos (base comum)

- [ ] Lógica de programação e resolução de problemas
- [ ] Estruturas de dados: arrays, listas, pilhas, filas, árvores, grafos, hash maps
- [ ] Algoritmos: busca, ordenação, recursão, complexidade (Big O)
- [ ] Git e controle de versão
- [ ] Linha de comando (terminal)
- [ ] HTTP, REST e noções de APIs

### Fase 2 — Uma linguagem por vez

Escolher **uma linguagem** e ir do básico ao intermediário antes de trocar. Sugestão de ordem:

1. **Python** — curva suave, ótima para consolidar conceitos
2. **JavaScript** — web, frontend e backend com Node
3. **Java** — OOP forte, ecossistema enterprise
4. **Go** — concorrência, performance, sistemas

### Fase 3 — Frameworks e projetos

Para cada linguagem, depois de dominar o intermediário:

- [ ] Construir 2–3 projetos guiados (tutorial)
- [ ] Construir 1–2 projetos próprios (ideia original)
- [ ] Explorar o framework principal do ecossistema
- [ ] Escrever testes automatizados

### Fase 4 — Avançado e integração

- [ ] Design patterns e princípios SOLID
- [ ] Arquitetura: MVC, camadas, microserviços, event-driven
- [ ] Bancos de dados: SQL (PostgreSQL) e NoSQL (Redis, MongoDB)
- [ ] Docker e containerização
- [ ] CI/CD básico
- [ ] Projeto full-stack integrando mais de uma linguagem

---

## Como usar este repositório

1. **Escolha um módulo** — ex.: `python/01-fundamentos/`
2. **Crie um `README.md` local** — defina o que vai estudar naquela sessão
3. **Pratique** — escreva código, não apenas leia teoria
4. **Documente** — anote o que aprendeu em `notas.md`
5. **Commite com mensagens claras** — ex.: `python: adiciona exercícios de list comprehensions`
6. **Revise** — volte aos módulos anteriores e refatore com o que aprendeu depois

### Convenção de commits

```
<linguagem>: <descrição curta>

Exemplos:
python: adiciona exercícios de decorators
javascript: projeto todo-list com React
java: implementa binary search tree
go: API REST com Gin e testes
algoritmos: resolve problema two-sum em 3 linguagens
```

---

## Ferramentas recomendadas

| Ferramenta | Uso |
|------------|-----|
| [VS Code](https://code.visualstudio.com/) / [Cursor](https://cursor.com/) | Editor principal |
| [Git](https://git-scm.com/) | Controle de versão |
| Python 3.12+ / [uv](https://github.com/astral-sh/uv) ou `venv` | Ambiente Python |
| [Node.js](https://nodejs.org/) + npm/pnpm | JavaScript/TypeScript |
| JDK 21+ / [Maven](https://maven.apache.org/) ou Gradle | Java |
| Go 1.22+ | Go |
| [Docker](https://www.docker.com/) | Containers (fase avançada) |
| [PostgreSQL](https://www.postgresql.org/) | Banco relacional |

---

## Recursos de estudo

### Gerais
- [freeCodeCamp](https://www.freecodecamp.org/)
- [Exercism](https://exercism.org/) — exercícios com mentoria em todas as 4 linguagens
- [LeetCode](https://leetcode.com/) / [HackerRank](https://www.hackerrank.com/) — algoritmos

### Por linguagem
- **Python:** [Documentação oficial](https://docs.python.org/3/), [Real Python](https://realpython.com/), [FastAPI docs](https://fastapi.tiangolo.com/)
- **JavaScript:** [MDN Web Docs](https://developer.mozilla.org/), [javascript.info](https://javascript.info/), [React docs](https://react.dev/)
- **Java:** [Documentação Oracle](https://docs.oracle.com/en/java/), [Baeldung](https://www.baeldung.com/), [Spring guides](https://spring.io/guides)
- **Go:** [Tour of Go](https://go.dev/tour/), [Go by Example](https://gobyexample.com/), [Effective Go](https://go.dev/doc/effective_go)

---

## Progresso

| Linguagem | Fundamentos | Intermediário | Avançado | Frameworks | Projetos |
|-----------|:-----------:|:-------------:|:--------:|:----------:|:--------:|
| Python    | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| JavaScript| ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Java      | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Go        | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Substitua ⬜ por ✅ conforme for avançando.

---

## Licença

Este é um repositório pessoal de estudos. Sinta-se livre para usar como referência, mas o código aqui é primariamente para aprendizado — não é produção.

---

*Recomeçar do básico não é voltar atrás — é construir uma fundação que aguenta qualquer altura.*
