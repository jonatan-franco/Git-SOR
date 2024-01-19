É importante notar que, na função utilizada:

```python
R = m*(t/T)**1/n
```
Fiz uma modificação matemática no expoente '1/n', a sua versão orgiinal, é esta: 
```python
R = m*(t/T)**n
```
Onde 'n' indica o tipo de esquema em vigor. 

A modificação foi necessária para que eu pudesse incluir o esquema de razão variável, pois se considerarmos apenas o expoente 'n'
não é possível plotar o esquema de razão variável mas sim, somente o de razão fixa. 

Por enquanto, não foi possível juntar as duas funções para que ficassem somente em uma única definição da função
todos os esquemas implementados. Entretanto, foi possível otimizar o código para essas duas funções, ficando assim, uma para os esquemas
contingentes (VR e FR) e o não contingente (VT) e outra para o esquema de intervalo (VI).

> note-se que o expoente do esquema de intervalo assume um valor arbitrário que eu mesmo coloquei. 
