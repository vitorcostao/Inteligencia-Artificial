# Inteligência Artificial - Aula 18

## 1. Teoria dos Jogos e Formulação de Problemas

A **Teoria dos Jogos** é um ramo da matemática aplicada que modela ambientes multiagentes como jogos, onde o impacto de cada agente sobre os outros é significativo. Em **jogos de soma zero**, os agentes agem alternadamente e seus objetivos são sempre opostos (o que é bom para um, é ruim para o outro), como no xadrez.

Em IA, jogos são desafiadores devido à sua complexidade (ex: xadrez com fator de ramificação médio de 35 e 10^154 nós na árvore de busca). Eles exigem a capacidade de tomar decisões mesmo quando o cálculo da decisão ótima é inviável.

Um problema de jogo com dois jogadores (MAX e MIN) é formulado com os seguintes componentes:

| Componente | Descrição |
| :--- | :--- |
| **1. Estado inicial** | A configuração inicial do jogo. |
| **2. Jogador** | Indica qual jogador deve realizar uma ação no estado atual. |
| **3. Ações válidas** | O conjunto de movimentos permitidos no estado atual. |
| **4. Modelo de transição** | Define o resultado de uma ação em um estado. |
| **5. Teste de estado terminal** | Verifica se o jogo chegou ao fim. |
| **6. Função de utilidade** | Atribui um valor numérico ao jogador `p` quando o jogo termina no estado `s` (ex: 1 para vitória, 0 para derrota, ½ para empate no xadrez). |

## 2. Decisões Ótimas em Jogos: O Valor Minimax

Ao contrário dos problemas de busca normais, onde se busca uma sequência de ações para um objetivo, em jogos, as ações do oponente (MIN) influenciam o objetivo do jogador (MAX). MAX deve encontrar uma **estratégia de contingência** que especifique seus movimentos para cada possível resposta de MIN.

A estratégia ótima em um jogo é determinada pelo **valor minimax** de cada nó na árvore de jogo. O valor minimax para MAX é o resultado que ele pode garantir a partir de um determinado ponto, assumindo que ele e seu adversário jogam da melhor forma possível. Ou seja, MAX sempre tenta maximizar seu ganho, enquanto MIN tenta minimizar o ganho de MAX.

## 3. Algoritmo MINIMAX

O algoritmo MINIMAX calcula o valor minimax de cada nó na árvore de jogo para determinar a decisão ótima. Sua intuição é:

1.  **Geração da árvore**: Constrói a árvore de jogo completa até os estados terminais (folhas).
2.  **Aplicação da função de utilidade**: Atribui valores de utilidade aos estados terminais.
3.  **Propagação dos valores**: Sobe a árvore, propagando os valores minimax de volta:
    *   Nós MAX escolhem o valor máximo entre seus filhos.
    *   Nós MIN escolhem o valor mínimo entre seus filhos.
4.  **Escolha da ação**: Na raiz, MAX escolhe a ação que leva ao maior valor minimax.

**Avaliação do Algoritmo MINIMAX:**

| Critério | MINIMAX |
| :--- | :--- |
| **Completo** | ✅ Sim (se a árvore for finita) |
| **Ótimo** | ✅ Sim (assumindo que o oponente também joga de forma ótima) |
| **Complexidade de Tempo** | O(b^m) |
| **Complexidade de Espaço** | O(b^m) |

O principal problema do MINIMAX é sua **complexidade exponencial**, tornando-o impraticável para jogos com árvores de busca muito grandes. Ideias para melhoria incluem limitar a profundidade da busca e usar heurísticas, ou podar ramos irrelevantes.

## 4. Poda Alfa-Beta

A **Poda Alfa-Beta** é uma técnica que otimiza o algoritmo MINIMAX, desconsiderando partes da árvore de busca que não influenciarão a decisão final. A ideia é que não vale a pena continuar explorando um ramo se já se encontrou uma opção melhor em outro lugar.

Para isso, a Poda Alfa-Beta utiliza dois parâmetros:

*   **α (alfa)**: O melhor valor (mais alto) que o jogador MAX já garantiu em algum ponto da busca. Representa o limite inferior para o valor de um nó MAX.
*   **β (beta)**: O melhor valor (mais baixo) que o jogador MIN já garantiu em algum ponto da busca. Representa o limite superior para o valor de um nó MIN.

### Funcionamento da Poda

1.  A árvore é percorrida como no MINIMAX.
2.  Em cada nó, verifica-se se vale a pena analisar os próximos ramos:
    *   **Poda Alfa (corte no MIN)**: Se em um nó MIN, o valor `α` de um ancestral MAX for maior ou igual ao `β` atual do nó MIN (`α ≥ β`), os demais ramos do nó MIN são ignorados. Isso ocorre porque MAX já tem uma opção melhor garantida e nunca escolheria este caminho.
    *   **Poda Beta (corte no MAX)**: Se em um nó MAX, o valor `β` de um ancestral MIN for menor ou igual ao `α` atual do nó MAX (`β ≤ α`), os demais ramos do nó MAX são ignorados. Isso ocorre porque MIN já aceitou uma opção 
pior e nunca escolheria este caminho.

### Avaliação da Poda Alfa-Beta

A efetividade da poda depende da ordem em que os sucessores são analisados. Com a melhor ordem possível, a complexidade de tempo do algoritmo é reduzida para **O(b^(m/2))**, o que é significativamente melhor do que o O(b^m) do MINIMAX tradicional, tornando-o mais viável para jogos complexos.

## Referências

- RUSSELL, Stuart J.; NORVIG, Peter. *Artificial intelligence: a modern approach*. 4ª ed. Pearson, 2021. (Capítulo 5)
