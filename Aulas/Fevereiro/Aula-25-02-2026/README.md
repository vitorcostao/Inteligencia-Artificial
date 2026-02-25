# Inteligência Artificial - Aula 04

## Árvore de Decisão - Cálculo do ganho

Para melhor construção de uma árvore de decisão eficiente é necessário que a profundidade seja a menor possível e que
os atributos possuam respostas definidas, ou seja, para cada atributo a resposta alvo deve ser a mesma de acordo com os rótulos.
Nesse contexto, identificar uma forma de encontrar esses atributos de entrada adequados é fundamental para determinar quais devem ser
analisados primeiro, em alguns casos, nem é preciso analisar uma feature, pois os resultados probabilistícos podem ser determinados por
outros atributos.

## Entropia e ganho de informação

A Entropia de Shannon, desenvolvida por Claude Shannon, é uma teoria que auxilia a escolha de um atributo para análise em uma árvore de decisão
utilizando os conceitos de incerteza e informação. Nesse contexto, tem-se as principais afirmações propostas por Claude:

1) A informação pode ser representada por meio de perguntas.
2) A quantidade de informação depende do conhecimento prévio (Dados ou contexto).
3) Eventos com baixa probabilidade trazem mais informações quando eles ocorrem (Entropia maior).
4) Quanto menor for a entropia mais informação se tem sobre o evento, logo mais certo ele é.

---

### Análise matemática

$H(v) = -\sum_{i=1}^{n} p_i \log_2(p_i)$

- **$p_i$** é a probabilidade do i-ésimo evento.
- **$-\log_2(p_i)$** é a quantidade de informação associada ao evento.

---

## Como calcular entropia de uma moeda honesta?

<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/94a378b3-9761-4962-a5e2-676056b7da51" />


---


## Entropia nas Árvore de Decisão

Sendo H(x) a entropia, para saber qual o melhor atributo a ser utilizado para se ter uma árvore de decisão eficiente é necessário analisar
a entropia de todos os atributos do conjunto e saber qual deles irá produzir maior ganho de informação (H(alvo) - H(atributo)), logo, como o
ganho de informação é a diferença entre a entropia do conjunto pela entropia do atributo, aquele atributo que tiver menor entropia irá produzir
um maior ganho de informação.


<img width="1320" height="970" alt="image" src="https://github.com/user-attachments/assets/e90071a5-567b-42fa-93a6-d69a721004ec" />

> Para o exemplo do restaurante mencionado aulas passadas, o atributo clientes é o melhor para ser analisado primeiro na árvore de decisão, pois
ele possui maior ganho de informação, logo ele produz saídas bem definidas (Nenhum e Alguns). 

