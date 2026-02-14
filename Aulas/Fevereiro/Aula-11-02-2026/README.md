# Inteligência Artificial - Aula 02

## Introdução ao Aprendizado de Máquina

### Algumas definições de AM

O termo Aprendizado de Máquina foi introduzido por **Arthur Samuel(1959)**. Dentre algumas definições, tem-se as seguintes: 

 - **Mitchell(1997):** “A capacidade de melhorar o desempenho na realização de
alguma tarefa por meio da experiência.”

 - **Enciclopédia Britânica:** “Processo que permite aos computadores aprenderem
autonomamente, identificando padrões e tomando
decisões baseadas em dados.

---

### Indução de Hipóteses

Atualmente, em um periodo marcado pela automatização de tarefas, é de extrema importância que as máquinas tenham a capacidade de aprender sozinhas através de dados. Nesse cenário, surge-se uma pergunta: **"Como aprender autonomamente?"**. Com isso, tem-se a Indução de Hipóteses, que é uma regra ou função que realiza o processamente de dados. Além disso, é importanteque a hipóteses seja válida para instâncias que não foram vistas ainda.

#### Análise prática

Imagine que um banco quer prever se deve aprovar ou rejeitar um pedido de empréstimo com base em alguns atributos do cliente. Quais atributos seriam importantes de serem avaliados? (Valor da dívida, Renda, Idade, Histórico e etc).

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/56f0b805-b625-4efe-8f58-e4ce660e9a24" /> 

> As Instâncias são os clientes do problemas dos bancos.

<br>

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/a98b3165-f20f-4dbb-ae52-68d15561908c" />

> Os atributos de entrada (features) são os dados das instâncias.

<br>
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/f86eabe6-1b24-4881-8e02-62b37210ae53" />

> Os atributos de saída (targets) são valores que a IA tenta prever corretamente.

Em alguns casos, a IA pode não ter uma taxa boa com o os aprendizados dos dados, o que se configura como **Underfitting**. Já o **Overfitting**, é quando o modelo de IA se especializa com os dados fornecidos no tratamento

---

### Tarefas de Aprendizado

- **Preditivas:** Encontrar uma função (hipótese) a partir dos dados de treinamento para prever um rótulo ou valor com base nos atributos de entrada.
> Algoritmos seguem o paradigma do aprendizado supervisionado, ou seja, há um supervisor externos que conhece a saída desejada paracada atributo de saída

- **Descritivas:** Explorar ou descrever um conjunto de dados.
> Algoritmos seguem o paradigma do aprendizado não supervisionado, ou seja, não fazem uso do atributo de saída.

<img width="757" height="382" alt="image" src="https://github.com/user-attachments/assets/6be06a75-9f4b-4287-b078-e517945d4495" />

---

### Aprendizado Supervisionado

- **Classificação:** Tem como objetivo atribuir uma das possíveis classes (rótulos) a um exemplo não rotulado.

- **Regressão:** Tem como objetivo prever um valor numérico contínuo para um exemplo dado.

---

### Aprendizado Não Supervisionado

- **Agrupamento(Clustering):** Tem como objetivo agrupar as instâncias de acordo com asimilaridade entre as instâncias (a partir das features)
  > Não existe rotulis e atributos de saída

- **Associação:** Tem como objetivo buscar padrões frequentes de associações entre atributos de um conjunto de dados
  > Features são sempre categóricas

---

### Exemplos de Algoritmos Clássicos

<img width="776" height="297" alt="image" src="https://github.com/user-attachments/assets/0a59c9c8-95ac-4401-9444-4992cd88c04e" />

---

### Principais Ferramentas

<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/29b8ad16-fd80-4544-b69b-845392536278" />

## Referências Bibliográficas

**FACELI, Katti et al. Inteligência artificial: uma abordagem de aprendizado de máquina. Rio de Janeiro, RJ: LTC, 2011. (Capítulo 1 e Introdução das Partes II e III)**

