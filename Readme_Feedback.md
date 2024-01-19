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

> note-se que o expoente do esquema de intervalo assume um valor arbitrário que eu mesmo coloquei baseando-me na sugestão do Rachlin (1989). 

Outra observação que deve ser feita quando ao expoente fracionário 1/n é que, se fores usa-lo, deve-se atentar que, ao dispor da função:
```python
expoente = np.arange(3)
```
Você estará considerando que, existem três retas: n=0, n=1, n=2. Um n > 1, estou considerando o 'tamanho' da exigência do esquema em um VR, se for n = 2, então, a cada duas respostas, em média, haverá um reforço. Podemos então dizer que, o expoente fracionário para n > 1 define um esquema VR. Sendo assim, para obter um VR 5, precisará considerar np.arange(6), deforma que se tenha a média de 5 respostas.

