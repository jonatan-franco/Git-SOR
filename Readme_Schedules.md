# Esquemas de reforçamento 

Olá! Este arquivo irá te orientar na interpretação dos códigos cujos quais contém algumas equações, talvez, não tão familiares.


## Fixed Ratio (Razão Fixa)

Este primeiro esquema é na forma:
```python
f(x) = a*x
```
>Sendo *a* , a taxa de resposta exigida para o esquema; e f(x) a taxa de reforçamento. 

Dado que o esquema é de razão fixa, então a taxa é constante, ou seja, ***a* = 1**, isto resultada em **f(x) = x**, ou seja, a taxa de reforçamento será igual a taxa de resposta.

$a = \Delta_{y}/\Delta_{x}$

$(y_{2}-y_{1}) = m(x_{2}-x_{1})$

É possível perceber que uma taxa constante só é possível quando os deltas(x,y) são iguais, ou seja, a taxa de resposta cresce a taxa constantes porque foi pré-definido no esquema que 'x' respostas **fixas** (e por isso, a resposta não pode aumentar de 10 para 20, por exemplo) e receber 20 reforços. E este é o motivo para te fará encontrar: 

```python
def reforco_0(comportamento_0):
	return comportamento_0
```

### Coeficiente angular
Caso tenha percebido, é o coeficiente angular que descreve a exigência do esquema, se pouco ou muito exigente. É, fazendo um paralelo, o parâmetro de 'dificuldade' da Teoria de Resposta ao Item (TRI). Entretanto, quando temos uma função linear:

```
y = a*x
```
Com 'a' sendo inteiro, estamos dizendo que, a medida que aumenta 'x', 'y' crescerá em um fator de 'a'. É como se fosse uma constante de conversão de real para dólar. Quando temos uma FR10, por exemplo, estamos dizendo que a cada 10 respostas o organismo receberá 1 reforço. Logo, quanto maior essa 'exigencia'/'dificuldade' de obter o reforçador, maior a inclinação da reta em direção ao eixo-x, é como se estivéssemos tentando forçar uma relação quase negativa entre resposta e reforço. Então, para representarmos essa possibilidade de relação, podemos escrever assim:

$y = \dfrac{1}{a}*x$

Então, no caso em que $a = 1$, $$f(x) = x$$, entretanto, $a > 0 \implies f(x) \neq x$ logo, entendemos que a relação entre $f(x)$ e $x$ (reforço e resposta, respectivamente) é lida como: a cada 1 resposta em x aumenta-se $\frac{1}{a}$ reforços. Ex.:

$reforco = \dfrac{1}{5}*resposta$

A cada 1 resposta de pressão à barra a mais, aumenta $\dfrac{1}{5}$ unidades do estímulo reforçador (gramas do alimento ou ml de água, por exemplo), ou seja, para obter 1 reforço são necessárias $1*\dfrac{5}{1} = 5$ respostas.

## Variable Ratio

Ao contrário da primeira, essa razão é variável, ou seja, em média, pode-se esperar que um esquema VR5 atenda a condição: 

 - a cada 5 respostas, em média, obtém-se um reforçador. 

Sendo assim, o que se encontra no código é: 
```python
def reforco(resposta):
	return resposta/5
```
O que este código diz é: pegue a quantidade total de respostas dentro de uma sessão e divida pela exigencia (tamanho) do esquema (5), e obterá a taxa de reforço que se pode obter neste esquema (R=2), ou seja, na sessão inteira, pode-se obter 2 reforçadores ao todo, com a taxa sendo x/5 para cada resposta, ou seja, a probabilidade de se obter o reforçador aumenta com o aumento da resposta: $P(r=1|x=5) >P(r=1|x = 1)$.
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
```
> onde T é o tempo total da sessão e C a exigencia do esquema.

No código, você encontrará:
```python
taxa_reforcamento_3  = [reforco_constante] *  len(comp)
```

>De forma implícita, está que  'reforco_constante' = T/C, por isso a fórmula para VT não está no código de forma explícita, pois ela não é necessária para a implementação, apenas o valor da taxa (T/C = 10 = reforco_constante)
 
É pelo fato de se ter uma taxa constante para todo valor que 'x' assumir que coloca-se 'len' e não a variavel em si, ou seja, eu quero que o programe contabilize cada elemento de 'comp' e cruze com a variável reforco_constante, ou seja, estou pegando R = 10 e aplicando para todo valor do conjunto do comportamento. 

Ou seja, para todo e qualquer elemento do conjunto 'x' (respostas), obtém-se uma mesma taxa constante de reforço.  Analisando esta relação pelo óculos dos estudos de derivada, então teríamos que f(x) representa a função que mapeia reforço e repostas, uma d(x) seria a variação que o reforço sofre dado uma resposta; sendo assim, se obtivéssemos uma derivada nula, concluiríamos que a resposta nao produz nenhuma alteração na taxa de reforçamento, ou seja, a derivada primeira sendo 0 para todo o intervalo do eixo das abscissas é uma descrição matemática do esquema de tempo variável e o possível aparecimento de um comportamento supersticioso.
