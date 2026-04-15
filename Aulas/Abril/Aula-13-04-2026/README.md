# Inteligência Artificial - Aula 13

## Arquitetura e Funcionamento do Neurônio Artificial

### Componentes das Redes Neurais Artificiais (RNAs)

As RNAs são sistemas compostos por unidades simples chamadas **neurônios artificiais**, que computam funções matemáticas e estão organizados em camadas interligadas por conexões unidirecionais.

#### Elementos Fundamentais

- **Unidades de Processamento (Nodos):** Os neurônios individuais da rede.
- **Conexões e Pesos ($w_{ij}$):** Simulam as sinapses biológicas. Os pesos podem ser positivos (excitatórios) ou negativos (inibitórios).
- **Topologia:** A forma como os neurônios estão conectados (arquitetura).
- **Aprendizado:** O processo de ajuste dos pesos para minimizar o erro, formulado como uma busca de otimização no espaço de pesos.

---

### O Neurônio Artificial

O neurônio é a unidade fundamental de processamento de uma RNA. Seu funcionamento segue três etapas básicas:

1.  **Entrada:** Recebe valores numéricos de outros neurônios ou do ambiente.
2.  **Processamento:** Multiplica cada entrada pelo seu respectivo peso e soma os resultados (soma ponderada).
3.  **Ativação:** Aplica uma **função de ativação** ao resultado da soma para gerar a saída.

#### Funções de Ativação Comuns

- **Linear:** Retorna a própria soma ponderada.
- **Limiar (Threshold):** Atua como um interruptor (0 ou 1) baseado em um valor de corte.
- **Sigmoidal:** Uma aproximação contínua e diferenciável da função limiar, essencial para redes multicamadas.

---

### O Modelo Perceptron

Desenvolvido por Rosenblatt em 1958, o **Perceptron** é a forma mais simples de rede neural, composta por uma única camada de neurônios.

#### Características e Limitações

- **Classificador Linear:** A superfície de decisão de um Perceptron forma um hiperplano que separa o espaço em duas classes.
- **Limitação Fundamental:** Um único Perceptron só consegue resolver problemas **linearmente separáveis** (ex: funções AND e OR). Ele falha em problemas como o XOR.
- **Teorema da Convergência:** Se um problema for linearmente separável, o algoritmo do Perceptron garantidamente encontrará uma solução.

#### Processo de Treinamento (Ajuste de Pesos)

O treinamento é iterativo e busca corrigir os pesos sempre que a rede comete um erro:
> **Novo Peso = Peso Antigo + ($\eta$ * Entrada * Erro)**

Onde:
- **Erro:** Diferença entre a saída esperada e a calculada.
- **$\eta$ (Taxa de Aprendizado):** Controla a magnitude do ajuste. Valores altos aceleram a convergência, mas podem causar instabilidade.

---

### Multilayer Perceptron (MLP)

Para superar as limitações do Perceptron e resolver problemas não linearmente separáveis, utiliza-se a arquitetura **MLP**, que adiciona camadas intermediárias (ocultas).

#### Funcionamento da MLP

- **Camadas Ocultas:** Permitem que a rede aprenda características cada vez mais complexas.
- **Não-Linearidade:** É obrigatório o uso de funções de ativação não-lineares (como a Sigmoide). Sem elas, múltiplas camadas seriam matematicamente equivalentes a uma única camada linear.
- **Hierarquia de Processamento:**
  - **1ª Camada:** Define hiperplanos simples.
  - **2ª Camada:** Combina hiperplanos em regiões convexas.
  - **Camadas Seguintes:** Combinam regiões para formar fronteiras de decisão de formato arbitrário.

---

### Comparativo: Perceptron vs. MLP

| Característica | Perceptron Simples | Multilayer Perceptron (MLP) |
| :--- | :--- | :--- |
| **Camadas** | Apenas uma (saída). | Entrada, Ocultas e Saída. |
| **Separação** | Apenas Linear. | Não-Linear (Complexa). |
| **Função de Ativação** | Geralmente Limiar. | Não-lineares (Sigmoide, ReLU). |
| **Aprendizado** | Regra do Perceptron. | Backpropagation (Retropropagação). |
| **Complexidade** | Baixa. | Alta. |
