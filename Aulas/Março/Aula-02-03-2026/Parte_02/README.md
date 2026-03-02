# Inteligência Artificial - Aula 05 - Parte 02

## Métricas de Avaliação

### Tipo de aprendizado

1) Classificação (Matriz de confusão)
2) Agrupamento (Silhueta)
3) Regressão (MSE e MAE)
4) Associação (Lift, Confiança)


### Matriz de confusão

Com base em dados de uma matriz é possível obter algumas taxas e métricas.

|     Matriz    | Predito: SIM | Predito: NÃO |
|---------------|-------------|---------------|
| Real: SIM     | 15          | 3             |
| Real: NÃO     | 2           | 20            |


**Taxa de Verdadeiros Positivos (VP rate) é o número de acerto do
classificador para cada classe:**

$\text{Taxa VP} = \frac{VP}{VP + FN} = \frac{15}{15 + 3} = \frac{15}{18} \approx 0,8333$

---

**Taxa de Falsos Negativos (FN rate) é número de erro do
classificador para cada classe.:**

$\text{Taxa FN} = \frac{FN}{VP + FN} = \frac{3}{15 + 3} = \frac{3}{18} \approx 0,1667$

---

**Taxa de Falsos Positivos (FP rate) são as instâncias que não são da
classe que estou considerando, mas foram
classificadas como sendo:**

$\text{Taxa FP} = \frac{FP}{FP + VN} = \frac{2}{2 + 20} = \frac{2}{22} \approx 0,0909$

---

**Taxa de Verdadeiros Negativos (VN rate) são as instâncias que não são da
classe que estou considerando, e foram classificadas
como não sendo:**

$\text{Taxa VN} = \frac{VN}{FP + VN} = \frac{20}{2 + 20} = \frac{20}{22} \approx 0,9091$

