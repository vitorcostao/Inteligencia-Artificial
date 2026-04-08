# Inteligência Artificial - Aula 12

## Conceitos Básicos de Redes Neurais

### O que são Redes Neurais?

As Redes Neurais Artificiais (RNAs) são modelos computacionais inspirados na estrutura e no funcionamento do cérebro humano. Diferente de outros métodos de aprendizado supervisionado, como Árvores de Decisão (regras) ou Naive Bayes (probabilidades), as RNAs representam padrões complexos através de uma combinação de **pesos e ativações**.

#### Propriedades das RNAs

- **Capacidade de aprender:** Adquirem conhecimento a partir de exemplos durante um processo de treinamento.
- **Generalização:** Conseguem prever ou fornecer respostas coerentes para dados que não foram vistos durante o treinamento.
- **Tolerância a falhas:** São robustas contra ruídos nos dados de entrada.

---

### Inspiração Biológica: O Sistema Nervoso

As RNAs são baseadas na forma como se acredita que o cérebro humano funciona, utilizando o neurônio como unidade fundamental.

#### Componentes do Neurônio Biológico vs. Artificial

- **Dendritos:** Recebem estímulos de outros neurônios.
- **Corpo Celular:** Combina e processa as informações, gerando um impulso.
- **Axônio:** Prolongamento responsável por conduzir os impulsos elétricos.
- **Sinapses:** Pontos de contato que controlam a transmissão de impulsos (fluxo de informação) entre os neurônios.

> Nas RNAs, as sinapses são representadas pelos **pesos sinápticos**, onde o conhecimento da rede fica armazenado de forma distribuída.

---

### Histórico das RNAs

A evolução das redes neurais passou por períodos de grande entusiasmo e momentos de estagnação, conhecidos como "Invernos da IA".

#### Linha do Tempo

- **Década de 1940 (O Início):** McCulloch e Pitts (1943) criaram o primeiro modelo matemático de um neurônio artificial. Hebb (1949) propôs que conexões entre neurônios ativos simultaneamente devem ser reforçadas.
- **Décadas de 1950-60 (Era de Ouro):** Rosenblatt (1958) implementou o **Perceptron**, a primeira rede neural prática, com ajuste iterativo de pesos.
- **Década de 1970 (Inverno da IA):** Minsky e Papert (1969) demonstraram as limitações do Perceptron, provando que ele só resolve problemas **linearmente separáveis** (como as funções lógicas AND e OR, mas não a função XOR).
- **Década de 1980 (Nova Onda):** Surgimento do algoritmo **Backpropagation** (retropropagação), permitindo o treinamento de redes com múltiplas camadas e maior capacidade de representação.
- **Século XXI (Deep Learning):** Avanço para redes com muitas camadas, culminando em arquiteturas como **Transformers** (2017) e modelos **GPT** (2018).

---

### Vantagens e Desvantagens

#### Vantagens

- **Aprendizado Complexo:** Capacidade de capturar relações não lineares nos dados.
- **Conhecimento Distribuído:** A informação não está centralizada, mas espalhada pelos pesos da rede.
- **Alta Performance:** Excelente em tarefas de visão computacional, processamento de linguagem natural e reconhecimento de padrões.

#### Desvantagens

- **Efeito "Caixa-Preta":** A relação entre entrada e saída não é facilmente explicável por humanos.
- **Custo Computacional:** O treinamento pode ser demorado e exigir hardware potente (GPUs).
- **Necessidade de Dados:** Exigem grandes volumes de dados para alcançar boa precisão.
- **Ajuste de Parâmetros:** Encontrar a topologia e os hiperparâmetros ideais exige muitas simulações.

---

### Estrutura de uma Rede Neural

Uma rede neural típica é organizada em camadas:

1.  **Camada de Entrada:** Recebe os dados brutos.
2.  **Camadas Intermediárias (Hidden):** Onde o processamento e a extração de características ocorrem.
3.  **Camada de Saída:** Fornece o resultado final da classificação ou regressão.

> A definição de quantas camadas e neurônios utilizar é um dos desafios do projeto de uma RNA.
