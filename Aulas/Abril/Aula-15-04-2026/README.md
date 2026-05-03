# Inteligência Artificial - Aula 14

## Algoritmo de Perceptron

Desenvolvido por Rosenblatt (1958), o Perceptron utiliza o modelo de McCulloch-Pitts com **função de ativação limiar** e **apenas uma camada de neurônios**.

A superfície de decisão forma um **hiperplano** que separa o espaço de entrada em duas partes — para um lado está uma classe, para o outro está a outra classe.

> **Um único Perceptron consegue separar somente conjuntos linearmente separáveis.**

---

### O Neurônio de McCulloch-Pitts

O Perceptron é baseado no neurônio de McCulloch-Pitts, modelado como um discriminador linear. Seu funcionamento segue três etapas:

1. **Entrada:** Recebe sinais de entrada ($x_1, x_2, \ldots, x_m$) ponderados pelos pesos sinápticos ($w_{k1}, w_{k2}, \ldots, w_{km}$).
2. **Soma ponderada:** Combina as entradas e aplica o bias ($b_k$):

$$v_k = \sum_{j=1}^{m} w_{kj} x_j - b_k$$

3. **Função de ativação (limiar):** Produz a saída $y_k$:

$$y_k = \begin{cases} 1, & \text{se } v_k \geq 0 \\ 0, & \text{se } v_k < 0 \end{cases}$$

O **bias** ($b_k$) define o quanto a soma ponderada das entradas deve ser alta para que o neurônio "ative".

---

### Características e Limitações

- **Classificador linear:** A superfície de decisão é um hiperplano num espaço n-dimensional.
- **Limitação fundamental:** Só resolve problemas **linearmente separáveis** (ex.: funções AND e OR). Falha em problemas como XOR.
- **Teorema da Convergência:** Se um problema for linearmente separável, o algoritmo do Perceptron garantidamente encontrará uma solução.

---

### Treinamento

A ideia é **encontrar um conjunto de pesos** que defina uma reta capaz de separar as diferentes classes corretamente.

#### Algoritmo de Treinamento (Algoritmo 7.1)

```
Entrada: Um conjunto de n objetos de treinamento
Saída:   Rede perceptron com valores dos pesos ajustados

1. Inicializar pesos da rede com valores baixos
2. repita
3.     para cada objeto x_i do conjunto de treinamento faça
4.         Calcular valor da saída produzida pelo neurônio, f(x_i)
5.         Calcular erro = y_i - f(x_i)
6.         se erro > 0 então
7.             Ajustar pesos do neurônio
8.         fim
9.     fim
10. até erro = 0
```

#### Detalhamento de cada etapa

**Passo 1 — Inicialização:** Os pesos começam com valores pequenos (aleatórios ou zero). O modelo "nasce sem saber nada".

**Passo 3 — Iteração:** Para cada instância do conjunto de treinamento, utilizam-se os atributos $x_i$ e a saída esperada $y_i$.

**Passo 4 — Cálculo da saída:** Aplica-se a soma ponderada dos atributos seguida da função de ativação limiar.

**Passo 5 — Cálculo do erro:** `Erro = esperado - calculado`, ou seja, $y_i - \hat{f}(x_i)$.

**Passo 6/7 — Ajuste de pesos:** Enquanto o erro for maior que zero, os pesos continuam sendo ajustados.

---

### Ajuste de Pesos (Regra de Atualização)

$$w_j(t + 1) = w_j(t) + \eta \, x_i^j \, (y_i - \hat{f}(x_i))$$

| Termo | Descrição |
| :--- | :--- |
| $w_j(t+1)$ | **Peso atualizado** |
| $w_j(t)$ | **Peso atual** |
| $x_i^j$ | Valor do atributo $j$ do exemplo $i$ |
| $(y_i - \hat{f}(x_i))$ | **Erro** (diferença entre esperado e calculado) |
| $\eta$ | **Taxa de aprendizado** (*learning rate*) |

> **Em resumo:** `Novo peso = peso antigo + (taxa de aprendizado × entrada × erro)`

#### Taxa de Aprendizado ($\eta$)

Controla a **magnitude do ajuste** feito em cada peso e a **velocidade de convergência** da rede:

- Valores **altos** → grandes variações nos pesos (convergência rápida, mas pode ser instável)
- Valores **baixos** → poucas variações nos pesos (convergência lenta, mas mais estável)

---

### Teorema da Convergência

> *"Se é possível classificar um conjunto de entradas linearmente, uma rede perceptron fará a classificação."*

Caso os dados **não sejam linearmente separáveis**, o Perceptron simples não converge — sendo necessário utilizar arquiteturas mais complexas, como o **Multilayer Perceptron (MLP)**.

---

### Referências

- FACELI, Katti et al. *Inteligência artificial: uma abordagem de aprendizado de máquina*. Rio de Janeiro, RJ: LTC, 2011. (Capítulo 7)
- Material da Profa. Cristiane Nobre
- Slides: Gabriel P. Oliveira — Inteligência Artificial, 2026/1