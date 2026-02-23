# Inteligência Artificial - Aula 03

## Árvore de decisão e regressão

### O que são Árvores de decisão e regressão?

Tratam-se de algoritmos utilizados para realizar a classificação e realizar a regressão.
Nesse contexto, a árvore é uma espécie de grafo, contendo nós e arestas sendo que há dois tipos de nós:

- Nós internos (atributos de entrada).
- Nós externos (atributos de saída).
> As decisões são tomadas por meio de testes e treinamento de dados.

---

### Exemplo de Árvore de decisão baseada no tempo  
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/14c93411-6bf4-417d-87fc-2d54b1777a0f" />

> Para toda instância, há um resultado.

---

## Indução de Árvores

### Problema

"Encontro-me em um restaurante e preciso decidir se vou esperar uma mesa ou não".

Para este problema, tem-se um aprendizado supervisionado baseado em classificação, ou seja, ou irei esperar ou não. Desse modo, o
objetivo é construir uma árvore de decisão para o problema.

- **Instâncias (Restaurantes)**.
- **Atributos de entrada(Fome, Tempo de espera e etc)**.
- **Atributo de saída(Sim ou Não)**.

Uma árvore consistente possui menor nível possível e começa por atributos de entrada que produzem saídas com resultados heterogêneos(Pouca distribuição de resultados).

---

## Vantagens e desvantagens

### Vantagens

- Flexibilidade: Consegue se adaptar a vários problemas.
- Seleção de atributos adequados: Não é necessário julgar todos atributos para se ter uma árvore eficiente.
- Interpretabilidade: Decisões complexas podem ser divididas em decisões simples (Dividir para conquistar).
- Eficiência Algoritmica.

### Desvantagens

- Dificuldade com ausência de valores.
- Ordenação de atributos contínuos consome recursos.
- Instabilidad de resultados devido a de alteração dos atributos de entrada.

## Referências Bibliográficas

**RUSSEL, Stuart J. e NORVIG, James. Artificial Intelligence:
a modern approach. (Cap. 18 – 3ª ed. ou Cap. 19 – 4ª ed.)**