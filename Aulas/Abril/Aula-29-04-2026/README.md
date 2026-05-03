# Inteligência Artificial - Aula 16

## Estratégias de Busca sem Informação

### As Dimensões da IA

A Inteligência Artificial pode ser classificada em dois eixos principais: **como humanos** vs. **racionalmente**, e **pensar** vs. **agir**. O foco desta aula está no quadrante **agir racionalmente** — o paradigma dos **agentes racionais**.

> **Agentes** → entidades que percebem o ambiente e tomam decisões (ações) a partir dele.
> **Racionais** → buscam sempre a melhor saída (esperada).

Exemplos: assistentes virtuais, robôs aspiradores, carros autônomos.

---

## Agentes Inteligentes

Um agente inteligente opera seguindo o ciclo: **perceber → decidir → agir**.

| Conceito | Descrição |
| :--- | :--- |
| **Percepts** | Entrada recebida pelo agente em um determinado momento |
| **Actions** | Decisão tomada com base na sequência de percepts até aquele instante |
| **Função do agente** | Mapeamento abstrato de percepts para ações (modelo matemático) |
| **Programa do agente** | Implementação concreta da função, que roda em uma arquitetura específica |

> **Distinção importante:** a *função* descreve o comportamento ideal; o *programa* é o que realmente executa na máquina.

---

## 1. Busca

### Problem-Solving Agents

Um **problem-solving agent** é um tipo de agente que encontra o que fazer buscando **sequências de ações** que levam a um objetivo (estado desejado).

A ideia central é: a partir de um estado atual, o agente examina as sequências possíveis de ações que levam a estados com valores conhecidos e escolhe a melhor entre elas.

Em outras palavras:
- O objetivo é representado por um **conjunto de estados**.
- O agente começa em um **estado inicial** e ações fazem-no mudar de um estado para outro.
- O agente deve encontrar uma **sequência de ações** (de preferência a melhor) que o leve do estado inicial ao estado final.

---

### Formulação do Problema

Um problema de busca é definido por cinco componentes:

| Componente | Descrição |
| :--- | :--- |
| **1. Estado inicial** | O estado em que o agente começa |
| **2. Ações disponíveis** | Conjunto de ações possíveis para o agente |
| **3. Modelo de transição** | Resultado de cada ação (função sucessora: pares `<ação, estado>`) |
| **4. Teste do objetivo** | Verificação se um estado é o estado final (pode ser explícito ou uma propriedade abstrata, como xeque-mate) |
| **5. Custo da solução** | Soma dos custos dos passos individuais; a **solução ótima** minimiza esse valor |

> O estado inicial + ações + modelo de transição definem o **espaço de estados** do problema — um grafo com todos os estados atingíveis.

---

### Exemplos de Problemas

#### Exemplo 1: Aspirador de Pó

Um mundo simples com dois locais (A e B), onde um aspirador percebe sua posição e se há sujeira. Suas ações são mover-se ou aspirar.

| Elemento | Definição |
| :--- | :--- |
| **Estados** | Agente em A ou B, cada local podendo estar sujo ou limpo (8 estados no total) |
| **Estado inicial** | Qualquer um dos 8 estados |
| **Ações** | Esquerda, direita, aspirar |
| **Teste de objetivo** | Todos os quadrados estão limpos? |
| **Custo** | Cada ação tem custo 1 |

#### Exemplo 2: 8-Puzzle

Um tabuleiro 3×3 com oito peças numeradas e um quadrado vazio. Uma peça adjacente ao espaço vazio pode deslizar para ele. O objetivo é alcançar uma configuração alvo.

| Elemento | Definição |
| :--- | :--- |
| **Estados** | Posição de cada peça e do espaço vazio |
| **Estado inicial** | Qualquer configuração |
| **Ações** | Esquerda, direita, cima, baixo (movimento do espaço vazio) |
| **Teste de objetivo** | Configuração desejada foi atingida? |
| **Custo** | Cada ação tem custo 1 |

#### Exemplo 3: Problema das 8 Rainhas

Posicionar oito rainhas em um tabuleiro de xadrez de forma que nenhuma ataque qualquer outra. Rainhas atacam qualquer peça na mesma linha, coluna ou diagonal.

| Elemento | Definição |
| :--- | :--- |
| **Estados** | Qualquer disposição de 0 a 8 rainhas no tabuleiro |
| **Estado inicial** | Tabuleiro vazio |
| **Ações** | Colocar uma rainha em qualquer quadrado vazio |
| **Teste de objetivo** | 8 rainhas posicionadas sem se atacarem |
| **Custo** | Não importa neste problema |

#### Exemplo 4: Viagem na Romênia (Arad → Bucareste)

Viagem entre cidades romenas representadas como um grafo ponderado.

| Elemento | Definição |
| :--- | :--- |
| **Estados** | Conjunto de cidades onde o agente pode estar |
| **Estado inicial** | Arad |
| **Ações** | Viajar de uma cidade para outra |
| **Teste de objetivo** | Estar em Bucareste |
| **Custo** | Distância em km entre as cidades |

> **Outros exemplos reais:** problema do caixeiro viajante, design de circuitos VLSI, navegação de robôs, sequência automática de montagem.

---

## 2. Busca em Espaço de Estados

As sequências de ações possíveis a partir do estado inicial formam uma **árvore de busca**:

- **Raiz** → estado inicial
- **Arestas** → ações (com custo ou utilidade associada)
- **Nós** → representam os estados
- **Folhas objetivo** → estados finais (solução)

Cada caminho da raiz até um nó representa uma sequência de ações. **Navegar no espaço de busca é construir e explorar essa árvore até encontrar uma solução.**

### Expansão de um Nó

**Expandir** um nó significa aplicar as ações válidas nele e gerar seus "filhos" na árvore. A decisão de **qual nó expandir** é o que define a estratégia de busca.

- **Borda (ou Fronteira):** conjunto de nós gerados mas ainda não expandidos.
- A expansão do nó objetivo **encerra a busca com sucesso**.

### Avaliação dos Algoritmos

Todo algoritmo de busca é avaliado segundo quatro critérios:

| Critério | Descrição |
| :--- | :--- |
| **Completude** | O algoritmo encontra uma solução quando ela existir? |
| **Otimalidade** | O algoritmo encontra a solução de menor custo? |
| **Complexidade de Tempo** | Quantos nós são gerados/expandidos? |
| **Complexidade de Espaço** | Quantos nós precisam ser mantidos em memória? |

As complexidades dependem de três parâmetros:
- **b** — fator de ramificação (máximo de sucessores de um nó)
- **d** — profundidade da solução mais rasa
- **m** — comprimento máximo de qualquer caminho no espaço de estados

> **Custo Total = Custo de Busca + Custo da Solução**

### Tipos de Busca

**1. Busca sem informação (cega):** não tem nenhuma informação adicional sobre os estados além das fornecidas na definição do problema. Inclui: BFS, DFS, busca de custo uniforme, busca com profundidade limitada e aprofundamento iterativo.

**2. Busca com informação (heurística):** sabe se um estado não-objetivo é mais "promissor" que outro — tema de aulas futuras.

---

## 3. Busca em Largura (BFS — *Breadth-First Search*)

### Como Funciona

A BFS expande o nó raiz, depois **todos os filhos da raiz**, depois os filhos desses nós, e assim por diante — nível por nível.

- Utiliza **fila FIFO** (primeiro a entrar, primeiro a sair) para garantir que o nó mais raso seja sempre expandido primeiro.
- O teste de objetivo é aplicado a cada nó **quando ele é gerado** (não quando é selecionado para expansão) — refinamento importante para eficiência.

### Algoritmo (pseudocódigo)

```
função BFS(problema) retorna nó-solução ou falha

  nó ← NÓ(problema.INICIAL)
  se problema.É-OBJETIVO(nó.ESTADO) então retorne nó
  fronteira ← fila FIFO contendo nó
  alcançados ← {problema.INICIAL}

  enquanto fronteira não vazia faça
      nó ← REMOVER(fronteira)
      para cada filho em EXPANDIR(problema, nó) faça
          s ← filho.ESTADO
          se problema.É-OBJETIVO(s) então retorne filho
          se s não está em alcançados então
              adicione s a alcançados
              adicione filho à fronteira

  retorne falha
```

### Exemplo Passo a Passo

Árvore com estado inicial `a`, estados finais `f` e `j`:

```
Passo 1 — FIFO: [a]          → expande a
Passo 2 — FIFO: [b, c]       → expande b
Passo 3 — FIFO: [c, d, e]    → expande c
Passo 4 — FIFO: [d, e, f, g] → expande d → f encontrado! ✓
```

Ordem de visitação: **a, b, c, d, e, f**
Solução encontrada: **[a, c, f]** (mais curta, antes de [a, b, e, j])

### Avaliação

| Critério | BFS |
| :--- | :--- |
| **Completo** | ✅ Sim (se a profundidade *d* for finita) |
| **Ótimo** | ✅ Sim, se o custo for função não-decrescente da profundidade |
| **Tempo** | O(b^d) |
| **Espaço** | O(b^d) — todos os nós ficam em memória |

> **Desvantagem principal:** o uso de memória cresce exponencialmente com a profundidade da solução.

---

## 4. Busca de Custo Uniforme (*Uniform Cost Search*)

### Como Funciona

Similar à BFS, mas os caminhos são colocados em uma **fila de prioridade (heap)** ordenada pelo **custo acumulado** do caminho até o momento. O algoritmo sempre expande o nó com o **menor custo acumulado** na fronteira.

- Se todos os custos forem iguais, a busca de custo uniforme se comporta exatamente como a BFS.
- Também conhecida como **Algoritmo de Dijkstra**.

### Exemplo: Sibiu → Bucareste

| Passo | Nó Expandido | Heap (fronteira) | Explorados |
| :--- | :--- | :--- | :--- |
| 1 | Sibiu (0) | R. Vilcea (80), Fagaras (99) | Sibiu |
| 2 | R. Vilcea (80) | Fagaras (99), Pitesti (177) | Sibiu, R. Vilcea |
| 3 | Fagaras (99) | Pitesti (177), Bucharest (310) | +Fagaras |
| 4 | Pitesti (177) | Bucharest (**278** ← atualizado!) | +Pitesti |
| 5 | Bucharest (278) | — | **Solução encontrada!** |

> **Detalhe chave:** ao expandir Pitesti, o custo de Bucareste via Pitesti (177 + 101 = 278) é **menor** que o custo anterior via Fagaras (99 + 211 = 310). O heap é **atualizado** com o valor mais baixo.

### Avaliação

| Critério | Busca de Custo Uniforme |
| :--- | :--- |
| **Completo** | ✅ Sim (se cada passo tiver custo ≥ ε > 0) |
| **Ótimo** | ✅ Sim (sempre expande pelo menor custo) |
| **Tempo** | O(b^(1 + ⌊C*/ε⌋)), onde C* é o custo da solução ótima |
| **Espaço** | Similar ao tempo |

---

## 5. Busca em Profundidade (DFS — *Depth-First Search*)

### Como Funciona

A DFS sempre expande o **nó mais profundo** na fronteira atual. Quando todos os sucessores de um nó foram explorados, a busca realiza **backtracking** — retorna ao nó anterior para explorar outros ramos.

- Utiliza **pilha LIFO** (último a entrar, primeiro a sair) para expandir o nó gerado mais recentemente.
- O processo continua até que todos os nós tenham sido descobertos ou a solução seja encontrada.

### Exemplo Passo a Passo

Árvore com estado inicial `a`, estados finais `j` e `f`:

```
Passo 1 — LIFO: [a]         → expande a
Passo 2 — LIFO: [b, c]      → expande b (mais à esquerda/profundo)
Passo 3 — LIFO: [d, e, c]   → expande d
Passo 4 — LIFO: [h, e, c]   → h é folha → backtrack
Passo 5 — LIFO: [e, c]      → expande e
Passo 6 — LIFO: [i, j, c]   → expande i → backtrack
Passo 7 — LIFO: [j, c]      → j encontrado! ✓
```

Ordem de visitação: **a, b, d, h, e, i, j**
Solução encontrada: **[a, b, e, j]** (não necessariamente a mais curta)

### Avaliação

| Critério | DFS |
| :--- | :--- |
| **Completo** | ❌ Não (pode cair em caminhos infinitos ou loops) |
| **Ótimo** | ❌ Não |
| **Tempo** | O(b^m) no pior caso |
| **Espaço** | O(b·m) — vantagem em relação à BFS! |

> **Problema:** se o espaço de busca for infinito, a DFS pode nunca encontrar o estado objetivo — indo sempre em profundidade por um caminho sem fim. **Refinamento:** limitar a profundidade máxima da busca.

---

## 6. Variações da Busca em Profundidade

### Busca com Profundidade Limitada (*Depth-Limited Search*)

Define uma **profundidade máxima L**, na qual a DFS para mesmo sem encontrar o objetivo. É especialmente útil quando se tem conhecimento prévio sobre o espaço de busca (e.g., sabe-se que a solução está a no máximo 10 passos).

- **Desvantagem:** se L for menor que a profundidade real da solução, o algoritmo **não encontrará** a resposta.

### Aprofundamento Iterativo (*Iterative Deepening Search*)

Executa **várias DFS com profundidade crescente**, combinando as vantagens da BFS (completude e otimalidade) com as da DFS (economia de memória).

```
Para L = 0, 1, 2, 3, …:
    Execute DFS com limite L
    Se encontrar solução → retorna
    Caso contrário → aumenta L e repete
```

> **Intuição:** parece ineficiente re-expandir os nós rasos a cada iteração, mas o custo extra é pequeno — a maioria dos nós está nas camadas mais profundas.

| Critério | Aprofundamento Iterativo |
| :--- | :--- |
| **Completo** | ✅ Sim |
| **Ótimo** | ✅ Sim (mesma garantia da BFS com custos uniformes) |
| **Tempo** | O(b^d) — semelhante à BFS |
| **Espaço** | O(b·d) — semelhante à DFS ✅ |

---

## Comparativo dos Algoritmos

| Algoritmo | Completo | Ótimo | Tempo | Espaço | Estrutura |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **BFS** | ✅ | ✅* | O(b^d) | O(b^d) | Fila FIFO |
| **Custo Uniforme** | ✅ | ✅ | O(b^(1+C*/ε)) | O(b^(1+C*/ε)) | Heap (prioridade) |
| **DFS** | ❌ | ❌ | O(b^m) | O(bm) | Pilha LIFO |
| **Prof. Limitada** | ❌** | ❌ | O(b^L) | O(bL) | Pilha LIFO |
| **Aprofund. Iterativo** | ✅ | ✅* | O(b^d) | O(bd) | Pilha LIFO |

*Ótimo se custo = função não-decrescente da profundidade (ou custos unitários).
**Incompleto se L < d.

---

### Referências

- RUSSELL, Stuart J.; NORVIG, Peter. *Artificial intelligence: a modern approach*. 4ª ed. Pearson, 2021. (Capítulo 3)
- Slides: Gabriel P. Oliveira — Inteligência Artificial, 2026/1
- Material da Profa. Cristiane Nobre