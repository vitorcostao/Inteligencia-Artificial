# Inteligência Artificial - Aula 11

## Algoritmo a priori

O algoritmo a priori é composto por duas fases sendo elas:

    1) Gerar item set com suporte mínimo especificado.
    2) Para cada item set gerar as regras com a confiança mínima especificada.

Desse modo, para a primeira fase os itens sets são gerados através das combinações de cada um dos itens até que ao fim se tenha uma combinação de tamanho máximo.

Por exemplo, para conjuntos de tamanho um, tem-se: [pão], [café] e [manteiga]. Para conjuntos de tamanho dois, tem-se: [pão,manteiga], [café,manteiga] e [café,pão]. Por fim, dado que apenas pão café e manteiga passaram no suporte mínimo especificado, tem-se o conjunto de tamanho três: [café,pão,manteiga].

Prosseguindo, para a segunda fase, basta calcular a confiança para as regras geradas de modo que aquelas que possuirem a confiança mínima exigida "passam" no teste.

>OBS: Confiança e suporte mínimo são hiperparâmetros.