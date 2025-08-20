A equação abaixo sumariza e integra todos os esquemas de reforçamento principais abordados neste repositório.

```python
R = m*(t/T)**n
```
Onde 'n' é o epxoente que indica a exigência do esquema. Quando n = 1, o esquema será VR/FR, quando n = 0, será VT/FT e quando 0<n<1, o esquema será VI/FI. É importante notar que aqui estou apontando tanto variável quanto fixo por uma simples razão: não é somente o expoente que ditará o esquema, mas sim, a distribuição da variável 'resposta'. Note que, em um esquema de razão variável a dispersão das respostas é tal que, o organismo responde seguindo uma estatística de centralidade (a média), entretanto, não o é garantido que assim seja no momento t+1. Sendo assim, o preponderante aqui é a distribuição da variável 'resposta'. Quanto menor a variabilidade, maior será a chance do esquema em vigor ser categorizado como 'FR', pois, a resposta prediz com 100% de precisão o reforço, isto é, y = x. Cada resposta una produz o número de reforços correspondente. 
