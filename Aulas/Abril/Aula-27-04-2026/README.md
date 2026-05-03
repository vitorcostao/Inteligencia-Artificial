# Inteligência Artificial - Aula 15

## Redes Neurais Artificiais

### O que é o Multilayer Perceptron (MLP)?

Para resolver problemas **não linearmente separáveis**, a alternativa mais utilizada é adicionar **uma ou mais camadas intermediárias** ao Perceptron.

O MLP possui **uma ou mais camadas intermediárias** de neurônios e uma camada de saída, geralmente usando **arquitetura completamente conectada**.

> **Uma rede multicamadas com funções de ativação lineares é equivalente a uma rede de uma única camada.**

---

### Características das Camadas

- **Primeira camada:** cada neurônio aprende uma função que define um hiperplano, separando o espaço de entrada em duas partes.
- **Segunda camada:** combina um grupo de hiperplanos da camada anterior, formando **regiões convexas**.
- **Camadas seguintes:** combinam regiões convexas em **regiões de formato arbitrário**.
- **Funções de ativação:** redes multicamadas usam funções de ativação **não lineares** (ex.: função sigmoidal).

> **É a combinação das funções desempenhadas por cada neurônio que define a função associada à RNA.**

---

## Algoritmo Backpropagation

### O que é o Backpropagation?

Proposto por **Rumelhart, Hinton e Williams (1986)**, o Backpropagation é a base do aprendizado supervisionado em redes MLP. É um algoritmo baseado no **aprendizado supervisionado por correção de erros**, composto por duas fases:

1. **Fase para frente (*forward pass*):** propagação dos dados pela rede.
2. **Fase para trás (*backward pass*):** retropropagação do erro e ajuste dos pesos.

> **A intuição é simples:** (1) imagine que você errou a classificação de uma instância. (2) Você volta, entende onde errou e tenta não repetir o erro.

---

### As Duas Fases do Backpropagation

**Fase 1 — Forward (para frente):**

1. Os dados entram pela rede.
2. Cada neurônio calcula sua saída e passa para a próxima camada.
3. A rede produz uma resposta ($\hat{y}$) — **cálculo das saídas e dos erros**.

**Fase 2 — Backward (para trás):**

1. O erro "volta" pela rede, camada por camada.
2. Os pesos são ajustados com base no erro — **ajuste dos pesos a partir da camada de saída até o início**.

---

### Treinamento (Algoritmo 7.2)

```
Entrada: Um conjunto de n objetos de treinamento
Saída:   Rede MLP com valores dos pesos ajustados

1.  Inicializar pesos da rede com valores aleatórios   ← modelo "nasce sem saber nada"
2.  Inicializar erro_total = 0
3.  repita
4.      para cada objeto x_i do conjunto de treinamento faça   ← a rede aprende um exemplo por vez
5.          para cada camada da rede, a partir da primeira camada intermediária faça   ← FORWARD
6.              para cada neurônio n_jl da camada atual faça
7.                  Calcular valor da saída produzida pelo neurônio, f̂
8.              fim
9.          fim
10.         Calcular erro_parcial = y - f̂   ← calcula o erro para o objeto em questão
11.         para cada camada da rede, a partir da camada de saída faça   ← BACKWARD
12.             para cada neurônio n_jl da camada atual faça
13.                 Ajustar pesos do neurônio utilizando Equação 7.3   ← para cada neurônio, ajusta os pesos
14.             fim
15.         fim
16.         Calcular erro_total = erro_total + erro_parcial
17.     fim
18. até erro_total < ξ   ← repetir até o erro total ficar suficientemente pequeno
```

#### Detalhamento de cada etapa

**Passo 1 — Inicialização:** Os pesos começam com valores aleatórios. O modelo "nasce sem saber nada".

**Passo 4 — Iteração:** A rede aprende **um exemplo por vez** do conjunto de treinamento.

**Passos 5–9 — Forward pass:** Para cada neurônio, em cada camada, calcula-se a saída usando pesos e função de ativação. O resultado final é a previsão da rede ($\hat{f}$).

**Passo 10 — Cálculo do erro parcial:** `erro_parcial = y - f̂`, calculado para o objeto em questão.

**Passos 11–15 — Backward pass:** Para cada neurônio, de volta pela rede, os pesos são ajustados.

**Passo 18 — Critério de parada:** Repete-se as duas fases até o erro total ficar **suficientemente pequeno** (abaixo do limiar $\xi$).

---

### Ajuste de Pesos (Regra de Atualização)

$$w_{jl}(t + 1) = w_{jl}(t) + \eta \, x^j \, \delta_l$$

| Termo | Descrição |
| :--- | :--- |
| $w_{jl}(t+1)$ | **Peso atualizado** entre o neurônio $l$ e o $j$-ésimo neurônio da camada anterior |
| $w_{jl}(t)$ | **Peso atual** entre o neurônio $l$ e o $j$-ésimo neurônio da camada anterior |
| $\eta$ | **Taxa de aprendizado** (*learning rate*) |
| $x^j$ | **Entrada recebida** pelo neurônio |
| $\delta_l$ | **Erro associado** ao $l$-ésimo neurônio |

> **Em resumo:** `Novo peso = peso antigo + (taxa de aprendizado × entrada × erro)`

---

### Cálculo do Erro ($\delta_l$)

O erro depende da camada em que o neurônio se encontra. Para neurônios da camada de saída, o erro é conhecido; para camadas intermediárias, ele precisa ser **estimado**:

$$\delta_l = \begin{cases} f'_l \, e_l, & \text{se } n_l \in C_{saida} \\ f'_l \sum w_{lk} \, \delta_k, & \text{se } n_l \in C_{intermediaria} \end{cases}$$

| Termo | Descrição |
| :--- | :--- |
| $f'_l$ | **Derivada parcial da função de ativação** (define o ajuste via gradiente descendente) |
| $e_l$ | **Erro quadrático médio (MSE)** — usado quando $n_l \in C_{saida}$: $e_l = \frac{1}{2}\sum_{q=1}^{k}(y_1 - \hat{f}_q)^2$ |
| $\sum w_{lk} \, \delta_k$ | **Soma ponderada** dos erros dos neurônios da camada seguinte — usada quando $n_l \in C_{intermediaria}$ |

> **Intuição:** os erros são conhecidos apenas para a camada de saída. Nas camadas intermediárias, estima-se o erro somando os erros dos neurônios da camada seguinte, ponderados pelo valor do peso de cada conexão.

---

## Gradiente Descendente

### O que é e por que é necessário?

O Backpropagation é um método de otimização baseado em **gradiente descendente**. Os pesos são ajustados calculando como o erro varia quando cada peso muda um pouco — a **derivada** indica a direção e a intensidade da mudança.

- **Derivada positiva** → o peso está aumentando o erro → devemos **diminuí-lo**.
- **Derivada negativa** → o peso está diminuindo o erro → devemos **aumentá-lo**.
- **Derivada zero** → chegamos a um ponto estável (**mínimo**).

> **Conclusão:** o sinal negativo da derivada é o que permite ao gradiente "subir" ou "descer" na direção certa — é isso que faz o gradiente descendente funcionar!

---

## Taxa de Aprendizado ($\eta$)

A taxa de aprendizado define o **tamanho do passo** dado a cada atualização de peso:

| Valor de $\eta$ | Efeito |
| :--- | :--- |
| **Baixo** | Pequenas mudanças nos pesos → aprendizado lento, porém estável |
| **Alto** | Grandes mudanças nos pesos → aprendizado rápido, mas com oscilações e risco de não convergir |

> **Cuidado:** um $\eta$ muito alto pode fazer o algoritmo ultrapassar o mínimo global e ficar oscilando, prendendo-se em um **mínimo local**.

---

## Funções de Ativação

É o que dá à rede a capacidade de aprender coisas **não-lineares**. Sem ela, empilhar camadas seria equivalente a ter uma rede de camada única. Como o Backpropagation usa gradiente descendente, são necessárias **funções diferenciáveis**.

### Sigmoide

$$\sigma(x) = \frac{1}{1 + e^x} \qquad \sigma'(x) = \sigma(x)(1 - \sigma(x))$$

- Saída entre **0 e 1** (útil na camada de saída para classificação binária).
- **Problema:** o gradiente some em redes profundas (*vanishing gradient*).

### Tangente Hiperbólica

$$tanh(x) = 2\sigma(2x) - 1 \qquad tanh'(x) = 1 - tanh^2(x)$$

- Saída entre **−1 e 1**.
- Geralmente **melhor que a sigmoide** em muitos casos.

### ReLU (Ativação Linear Retificada)

$$ReLU(x) = \max\{0, x\} \qquad ReLU'(x) = \begin{cases} 1, & \text{se } x \geq 0 \\ 0, & \text{c.c.} \end{cases}$$

- **Derivada simples** (0 ou 1).
- **Muito usada** atualmente em redes profundas.

---

## Outras Considerações

### Variações do Algoritmo

- **Stochastic Gradient Descent (Padrão):** atualiza os pesos após **cada exemplo** — rápido, mas instável.
- **Batch Gradient Descent:** atualiza os pesos após ver **todos os exemplos** — estável, mas lento.

> **Epoch (época):** cada vez que há a apresentação completa de todos os dados de treino.

---

### Heurísticas para Número de Neurônios na Camada Intermediária

**Valor médio** — média do número de entradas e saídas:

$$q = \frac{p + M}{2}$$

**Raiz quadrada** — raiz quadrada do produto do número de entradas e saídas:

$$q = \sqrt{p \cdot M}$$

**Kolmogorov** — dobro do número de entradas mais 1:

$$q = 2p + 1$$

**Outras sugestões:** estar entre o número de entrada e saída; 2/3 o tamanho da entrada + tamanho da saída; menor que o dobro do tamanho da entrada.

---

### Referências

- FACELI, Katti et al. *Inteligência artificial: uma abordagem de aprendizado de máquina*. Rio de Janeiro, RJ: LTC, 2011. (Capítulo 7)
- Material da Profa. Cristiane Nobre
- Slides: Gabriel P. Oliveira — Inteligência Artificial, 2026/1
- Funções de ativação: https://matheusfacure.github.io/2017/07/12/activ-func/
- Taxa de aprendizado: https://www.maxwell.vrac.puc-rio.br/32823/32823_4.PDF
- Gradiente vs. Backpropagation: https://www.analyticsvidhya.com/blog/2023/01/gradient-descent-vs-backpropagation-whats-the-difference/