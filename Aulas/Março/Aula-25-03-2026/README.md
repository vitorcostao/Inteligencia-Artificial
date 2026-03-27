# Inteligência Artificial - Aula 12

## Etapas de pré-processamento de dados

### Balanceamento de dados

O problema de dados desbalanceados é tópico da área de classificação de dados. Em vários 
conjuntos de dados reais, o número de objetos varia para diferentes classes.
Isso é comum em aplicações em que dados de um subconjunto das classes aparecem com uma
frequência maior que os dados das demais classes.

Por exemplo, se em uma determinada coleta de dados de um teste, o resultado X foi de 80% 
e o resultado Y foi de 20%, os algoritmos para tomada de decisões (classificações) tendem 
a favorecer os resultados da classe majoritária, que é aquela que possui uma possui um maior
número.

#### Técnicas para solução

- É possível redefinir o tamanho do conjunto de dados, removendo (undersampling) ou adicionando(oversampling) dados das classes majoritária e minoritária, respectivamente. 
   > Adicionar instâncias inúteis podem atrapalhar o modelo(overfitting), bem como a remoção de dados importantes (underffiting).

- É possível determinar um custo de classificação para diferentes classes, de modo que, se o número de X, que é majoritário, for o dobro de Y, logo o erro de um pode equivaler a dois erros do outro.
   > Definir o custo é um processo indireto e complexo.

- Induzir um modelo para cada classe é uma das soluções, pois um modelo aprende de uma e outro de outra. Tem-se como exemplos o Smote (oversampling), TomekLinks (undersampling) e o RandomUnderSampler
   > Ao usar undersampling, é importante colocar no teste as intâncias descartadas pelo método.

---

### Dados Ausentes


A base de dados pode conter dados ausentes e isto apresenta
dificuldades relacionadas à qualidade dos dados. Os dados ausentes
podem ocorrer devido a problemas nos equipamentos de coleta, transmissão 
e armazenamento de dados falho ou até mesmo pelo mal preenchimento dos dados.
Alguns algoritmos conseguem lidar com valores ausentes, porém nem todos possuem
tal capacidade.

#### Razões para dados ausentes

- O atributo não foi considerado importante na época da coleta (campo e-mail em 1990)
- Falta de conhecimento do campo (ex: tipo sanguíneo)
- Distração
- Falta de necessidade ou obrigação de apresentar um valor para o atributo (Ex. renda)
- Inexistência de um valor para o atributo em algumas instâncias (ex: número de partos de for homem)
- Problema com equipamento ou processo utilizado para coleta, transmissão e armazenamento de dados


#### Técnicas para solução dos problemas

- Eliminar instâncias com dados ausentes é uma solução, porém não é recomendado para conjuntos de dados pequenos e quando existem muitos atributos distintos que possuem valores ausentes.

- Preencher tais valores manualmente é uma solução, todavia é ineficiente quando se tem um conjunto de dados muito grande em termos de valores ausentes.

- Utilizar heurísticas de otimização através da média, moda e um indutor é umas das formas mais recomendadas para inputar dados ausentes.

- É possível utilizar algoritmos que já lidam com valores ausentes. 


--- 

### Dados inconsistentes e redundantes

A inconsistência dos dados é expressa quando existem valores conflitantes entre seus atributos, por exemplos, duas instâncias podem ser iguais e ter resultados finais distintos em uma base de dados. Em se tratanto de uma instância redundante, tem-se como exemplo instâncias que são muito semelhantes em termos de atributos, sendo possível descartar uma delas. Quando se fala em atributos, pensar em atributos derivados é algo redundante, pois tecnicamente não é necessário saber a idade tendo a data de nascimento da pessoa e vice-versa.


A redundância de um atributo está relacionada à sua correlação com um ou mais atributos do conjunto de dados. Nesse contexto, dois ou mais atributos estão correlacionados quando apresentam
um perfil de variação semelhante para as diferentes instâncias. Além disso, se a correlação ocorrer entre um atributo de entrada e um atributo de classificação, este atributo de entrada terá uma
grande influência na predição do valor do atributo rótulo.

#### Principais causas

Tais problemas são causados principalmente por problemas na coleta, na entrada, no armazenamento, na
integração ou na transmissão de dados. Além disso, os modelos e indutores tentam aprender questões da vida real, que por si só possuem redundância e inconsistência.

---

### Conversões numérico-simbólica e simbólico-numérico

#### Numérico-simbólica

Em se tratando de conversões, é extremamente importante que alguns dados possam ser discretizados. Nas conversões numéricas, a recomendação é discretizar o atributo. Quando um atributo quantitativo é discretizado, o conjunto de possíveis valores é dividido em intervalos, e cada intervalo de valores quantitativos é convertido em um valor qualitativo. Em alguns métodos, o usuário pode influenciar a definição dos intervalos, definindo valores para parâmetros como número máximo de intervalos.
Já os métodos não paramétricos definem os intervalos utilizando apenas as informações presentes nos valores dos atributos.

Algumas das estratégias utilizadas pelos diferentes
métodos são apresentados a seguir:

- Larguras iguais: Divide o intervalo original de valores em subintervalos de mesma largura
- Frequências iguais: Atribui o mesmo número de objetos a cada subintervalo.

#### Simbólico-numérica

As técnicas como redes neurais artificias, SVM e vários algoritmos de agrupamento lidam apenas com dados numéricos. Para transformar os dados para simbólicos existem diversas soluções:

- Quando o atributo é do tipo simbólico e assume apenas dois valores, se os valores denotam a presença ou ausência de uma característica podemos utilizar um dígito binário

- Quando o atributo é do tipo simbólico e assume mais de dois valores, a técnica utilizada na conversão depende de o atributo ser nominal ou ordinal.
    > Se não houver relação de ordem entre os valores do atributo, tal ordem deve continuar sem inexistente para os valores numéricos gerados.

<p align="center">
<img width="441" height="250" alt="image" src="https://github.com/user-attachments/assets/5b219234-d45f-475a-9570-6c802d7b9bb7" />
<p align="center">


- Quando existe uma relação de ordem, o atributo é do tipo ordinal, e a codificação deve preservar essa relação. Para isso, deve ser utilizada uma codificação em que a ordem dos valores esteja clara.

<p align="center">
<img width="322" height="235" alt="image" src="https://github.com/user-attachments/assets/6c1d6529-cb8c-48b4-a3d3-31622b8472e9" />
<p align="center">


