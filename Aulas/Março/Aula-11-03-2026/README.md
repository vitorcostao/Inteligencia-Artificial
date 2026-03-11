# Inteligência Artificial - Aula 08

## Método probabilísticos Naive Bayes

Para determinar decisões a partir de incertezas, é importante que seja trabalhada a ideia de probabilidade em IA, por exemplo:
Diagnósticos médicos, detecção de spam, recomendação de músicas.

### Probabilidade

Trata-se de um ramo da matemática que calcula a chance de um evento aleatório ocorrer. Desse modo, em se tratanto de inteligência
artificial, muitos dos eventos aleatórios possuem certos graus de dependência uns com os outros, o que resulta na mudança da 
probabilidade.

Nesse contexto, o Teorema de Bayes surge como uma das principais abordagens para determinações probabilísticas:

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

- **P(A|B)** → Probabilidade de **A acontecer dado que B ocorreu** (probabilidade posterior)
- **P(B|A)** → Probabilidade de **B acontecer dado que A ocorreu**
- **P(A)** → Probabilidade inicial de **A** (probabilidade a priori)
- **P(B)** → Probabilidade total de **B**
>Para cada exemplo de teste, a classe predita será a com maior probabilidade posterior

---

### Naive Bayes (Ingênuo)

Quando o problema possui muitos atributos, acaba que a possibilidade de um influênciar o outro é altíssima e isso
faria com que os custos computacionais para determinar a ocorrência desses eventos fosse altíssima.

Por isso, Naive Bayes assume **independência** dos atributos, o que não é um fato porém possui um bom acerto.
Assumindo que os valores dos atributos de um exemplo são independentes entre si dada a classe, a probabilidade de um
exemplo com atributos (x1, … xn) pertencer à classe c é proporcional à expressão:

$$P(c \mid x_1, ..., x_n) \propto P(c) \prod_{j=1}^{n} P(x_j \mid c)$$


### Funcionamento do algoritmo

1. No conjunto de treinamento, para cada classe:
   
   a. Calcular a priori P(classe)

   b. Calcular P(atributo | classe)

   c. Multiplicar P(classe) e P(atributo | classe) para todos os atributos

2. Escolher classe de maior probabilidade

## Exemplo Naive Bayes

Para um exemplo teste em que um banco quer classificar o risco de inadimplência dos
clientes dadas as suas características, supondo que tal exemplo possui um hisórico bom,
uma dívida alta, sem garantias e renda acima de trinta e cinco mil. Calcule a probabilidade 
do risco de inadimplência para cada target.

<img width="1111" height="752" alt="image" src="https://github.com/user-attachments/assets/6ea0344e-f755-47a9-a669-bd2bcb7f6376" />

<img width="1277" height="397" alt="image" src="https://github.com/user-attachments/assets/3c5acc03-3229-499a-8e5b-1f434484df5d" />

Tendo os valores da tabela, basta realizar o produtório para cada uma das possibilidades.


## Referências Bibliográficas

FACELI, Katti et al. Inteligência artificial: uma abordagem de
aprendizado de máquina. Rio de Janeiro, RJ: LTC, 2011. (Capítulo 5)

Material da Profa. Cristiane Nobre
