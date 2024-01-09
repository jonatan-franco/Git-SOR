# Esquemas de reforçamento 

Olá! Este arquivo irá te orientar na interpretação dos códigos cujos quais contém algumas equações, talvez, não tão familiares.


## Fixed Ratio (Razão Fixa)

Este primeiro esquema é na forma:
```python
f(x) = a*x
```
>Sendo *a* , a taxa de resposta exigida para o esquema; e f(x) a taxa de reforçamento. 

Dado que o esquema é de razão fixa, então a taxa é constante, ou seja, ***a* = 1**, isto resultada em **f(x) = x**, ou seja, a taxa de reforçamento será igual a taxa de resposta.

```
a = delta_y/delta_x
(y2-y1) = m(x2-x1)
```
É possível perceber que uma taxa constante só é possível quando os deltas(x,y) são iguais, ou seja, a taxa de resposta cresce a taxa constantes porque foi pré-definido no esquema que a 'x' respostas **fixas**, por isso, a resposta não pode aumentar de 10 para 20, por exemplo, e receber 20 reforços. E justamente por isso que você encontrará: 
```python
def reforco_0(comportamento_0):
	return comportamento_0
```
### Coeficiente angular
É possível obter a = 10 e isto significar FR10? Testemos: a cada 10 resposta, obtenho 1 reforço. 
(y2-y1)*a =(x2-x1)
delta_y/delta_x=10
conclui-se que delta_y precisa ser 10x maior que delta_x:

> nao é possível porque se eu fizer a = 10, entao, a cada x, tenho inclinação de 10 unidades, sendo assim, nao expressa o esquema que quero demonstrar: a cada DEZ respostas tenho UM reforço, e não **a cada resposta uma inclinação de 10 unidades**.
> É interessante pensar também no coeficiente linear, porque eu poderia pensar f(x)=a*x+b, com *b* sendo o reforço que o indivíduo ja recebeu, ou seja, eu poderia fazer duas restas em que o indiv1 nao recebeu nada b=0, e o indiv2 recebeu 2 reforços e ver o que acontece (Imagem abaixo)

![enter image description here](https://media.discordapp.net/attachments/1159224295642374255/1194103584242028605/image.png?ex=65af229f&is=659cad9f&hm=a3724ba84ed6bfcf1e7e913bcf7e947b36d5802696e359264f317304b5a8e3a3&=&format=webp&quality=lossless)



## Variable Ratio

Ao contrário da primeira, essa razão é variável, ou seja, em média, pode-se esperar que um esquema VR5 atenda a condição: 

 - a cada 5 respostas, em média, obtém-se um reforçador. 

Sendo assim, o que se encontra no código é: 
```python
def reforco(resposta):
	return resposta/5
```
O que este código diz é: pegue a quantidade total de respostas dentro de uma sessão e divida pela exigencia (tamanho) do esquema (5), e obterá a taxa de reforço que se pode obter neste esquema (R=2), ou seja, na sessão inteira, pode-se obter 2 reforçadores ao todo, com a taxa sendo x/5 para cada resposta, ou seja, a probabilidade de se obter o reforçador aumenta com o aumento da resposta: P(r=1|x=5) >P(r=1|x = 1).
> A probabilidade de receber reforço (r=1) é maior, dado que apertou a barra 5 vezes, do que a probabilidade de receber reforço quando se comportou 1 vez. 

## Variable Interval

Neste esquema específico, tem-se que a taxa de reforçamento é dependente da passagem do tempo (intervalo) e da resposta, ou seja, um VR5, é o esquema cujo qual irá ditar ao organismo que só receberá reforço após após 't' unidade de tempo e 'x' respostas, ou seja, aqui não será mais uma função linear pois não se pode obter uma taxa constante para toda variação na resposta. Logo, o que aparece no código é:
```python
def reforco(comportamento):
	return T / (C +  0.5  * (1  /  comportamento))
```` 
> T: tempo total da sessão (T=60),
> C: tamanho do esquema (C=6)
> comportamento: B
> 1/comportamento: entende-se aqui que, quando comportamento --> +inf/-inf, então 0.5*(1/comportamento) --> 0, ou seja, a medida que as respostas aumentam, chega-se próximo a uma assíntota horizontal em T/C, que neste caso é 10 (60/6=10), e também quando o comportamento (B) tende a zero pela direita e esquerda, essa fração 1/B --> +/-inf, ou seja, a assíntota vertical se encontra em B = 0, isto é, a função se aproxima de 0 sem nunca tocá-lo. 

Sendo assim, o que descreve a taxa de reforçamento neste esquema, é: 1) ela depende do tempo total em que a sessão é realizada; 2) o tempo médio entre cada reforço dado que a resposta já ocorreu; e 3) a resposta cresce a taxas decrescentes.

## Variable Time

Neste esquema, o que se tem é simples: a taxa de reforçamento depende de uma constante única, o tempo. Ou seja, matematicamente o que se tem é: 
```
R = T/C,