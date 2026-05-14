# Inteligência Artificial - Aula 17

## 1. Busca com Informação (Heurística)

A busca com informação difere da busca sem informação (cega) por utilizar um **conhecimento maior sobre o problema** para tornar a busca mais eficiente. Enquanto algoritmos como Dijkstra (busca de custo uniforme) escolhem o caminho com menor custo acumulado até o momento, a busca com informação considera o custo já percorrido (`g(n)`) e uma **estimativa do custo restante até o objetivo (`h(n)`)**.

### Função de Avaliação `f(n)`

O nó a ser expandido é escolhido de acordo com uma função de avaliação `f(n)`. Geralmente, `f(n)` incorpora uma função heurística `h(n)`.

### Função Heurística `h(n)`

A função heurística `h(n)` fornece uma indicação do melhor caminho até a solução desejada. Ela representa o **custo estimado do melhor caminho de um nó `n` até o objetivo**. Se `n` já for o objetivo, `h(n) = 0`.

**Exemplo:** Na viagem na Romênia (Arad → Bucareste), a função heurística `h(n)` pode ser a distância em linha reta entre a cidade `n` e Bucareste.

## 2. Busca Gulosa (*Greedy Search*)

A Busca Gulosa tem como ideia expandir o nó que está **mais próximo do objetivo** de acordo com a função heurística. Sua função de avaliação é `f(n) = h(n)`.

É chamada de "gulosa" porque busca reduzir o custo imediato para alcançar o objetivo em cada expansão, sem se preocupar com o custo total do caminho. Isso significa que a Busca Gulosa **não garante otimalidade**.

**Avaliação da Busca Gulosa:**

| Critério | Busca Gulosa |
| :--- | :--- |
| **Completo** | ❌ Não (pode entrar em loop) |
| **Ótimo** | ❌ Não |
| **Tempo** | O(b^m) |
| **Espaço** | O(b^m) |

A eficiência da Busca Gulosa é fundamentalmente dependente da **qualidade da função heurística** utilizada. Uma heurística bem escolhida pode levar a uma execução rápida, mas a falta de otimalidade e completude são desvantagens significativas.

## 3. Algoritmo A*

O Algoritmo A* busca minimizar o custo total estimado da solução. Ele expande o nó de acordo com a função de avaliação:

`f(n) = g(n) + h(n)`

Onde:
*   `g(n)`: é o custo real de chegar ao nó atual `n` a partir do estado inicial.
*   `h(n)`: é a estimativa do custo do nó atual `n` até o objetivo (função heurística).

Assim, `f(n)` é a estimativa do custo da melhor solução que passa por `n`. O Algoritmo A* combina as vantagens da busca de custo uniforme (considerando `g(n)`) com as da busca gulosa (considerando `h(n)`).

**Avaliação do Algoritmo A*:**

| Critério | Algoritmo A* |
| :--- | :--- |
| **Completo** | ✅ Sim (se `h(n)` for admissível e o fator de ramificação for finito) |
| **Ótimo** | ✅ Sim (se `h(n)` for admissível e consistente) |
| **Tempo** | Exponencial, mas geralmente melhor que busca cega |
| **Espaço** | Exponencial (similar à BFS) |

### Heurísticas Admissíveis e Consistentes

*   **Heurística Admissível:** Uma heurística `h(n)` é admissível se ela **nunca superestima o custo real** para alcançar o objetivo (ou seja, `h(n) ≤ h*(n)`, onde `h*(n)` é o custo real). Heurísticas admissíveis são cruciais para garantir a otimalidade do A*.
*   **Heurística Consistente (ou Monotônica):** Uma heurística `h(n)` é consistente se, para cada nó `n` e cada sucessor `n'` de `n` gerado por uma ação `a` com custo `c(n, a, n')`, a seguinte condição for satisfeita: `h(n) ≤ c(n, a, n') + h(n')`. Heurísticas consistentes são sempre admissíveis e garantem que o A* nunca precise reabrir nós.

### Heurísticas para o 8-Puzzle

Dois exemplos de heurísticas para o 8-puzzle são:

*   **h1: Número de peças na posição errada:** Conta quantas peças não estão em suas posições-alvo. É admissível porque cada peça fora do lugar precisará de pelo menos um movimento.
*   **h2: Soma das distâncias de Manhattan:** Soma das distâncias (horizontal + vertical) de cada peça até sua posição-alvo. É admissível e geralmente mais informativa que `h1`.

### Qualidade da Heurística

A qualidade de uma heurística é avaliada pelo **Fator de Ramificação Efetivo (b*)**. Um `b*` próximo de 1 indica uma heurística muito eficiente. Heurísticas mais informativas (que dominam outras, como `h2` domina `h1` no 8-puzzle) geralmente resultam em menos nós expandidos, mas o tempo para computá-las também deve ser considerado.

### Criação de Heurísticas

Heurísticas admissíveis podem ser criadas a partir de **versões relaxadas do problema**, onde algumas restrições são removidas. O custo de uma solução ótima para o problema relaxado serve como uma heurística admissível para o problema original. Por exemplo, para o 8-puzzle, relaxar as regras de movimento das peças pode levar às heurísticas `h1` e `h2`.

## Referências

- RUSSELL, Stuart J.; NORVIG, Peter. *Artificial intelligence: a modern approach*. 4ª ed. Pearson, 2021. (Capítulo 3)
- Slides: Gabriel P. Oliveira — Inteligência Artificial, 2026/1
