# Mapeamento logístico e fractais- Atividade Bonus

A biblioteca utilizada para implementar o zoom na forma de animação é o ```matplotlib.animation```. Para a implementação, é preciso import o ```FuncAnimation```. Incialmente, foi definida a lista dos valores de r, em que foi utilizado o ```np.linspace``` com 3000 subdivisões, juntamente com o número de pontos que vai rodar na função (M e N). Nesse caso, considera-se que $$N = M + 1000.$$

Para calcular os pontos de r, foi criado primeiramente o dicianario ```pontos = {}```, para armazenar todos os valores de r. Em seguida, o loop

```
for r in lista_r:
    simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
    pontos[r] = simulacao[-M:]
```

funciona selecionando cada r no vetor ```lista_r``` e rodando no objeto ```simulacao```, em que carrega a função que contém a função ```mapa_logistico()```. No caso do código, ele calcula os valores para 3000 valores diferentes de r e executa 4000 iterações(N), mas armazena apenas os 3000 últimos pontos(M). Isso foi feito a partir de 
```
  pontos[r] = simulacao[-M:],
```
selecionando apenas os ultimos valores de M e adicionando ao dicionario pontos (O dicionário pontos mapeia cada valor de r para seus respectivos resultados, e r é a chave do dicionário).

Em seguida, foi criada a lista ```regioes_zoom``` contendo seis tuplas relacionadas aos limites mínimos e máximos de r que serão exibidos em cada frame. Na linha ```fig, ax = plt.subplots(figsize=(10, 7))```, foi criadq a figura e o conjunto de eixos ax para cada zoom. O ax foi incluído para criar um novo eixo x para cada zoom, sendo que a cada zoom vai mudar o intervalo para cada tupla da lista ```regioes_zoom```. A função ```def init()``` é utilizada para iniciar o zoom, limpa os eixos antes do início da animação e é chamada uma vez antes de iniciar a animação, garantindo que o gráfico comece em branco. O ponto chave para a animação é representada pela função ```def animar(i)```, a qual recebe um parametro i. Primeiramente , limpa os eixos pela função ```ax.clear```. Em seguida, foi definido ```r_min, r_max = regioes_zoom[i % len(regioes_zoom)]``` para indentificar os os limites de r mínimo e r máximo. Além disso, seleciona a região de zoom atual de acordo com o índice do frame(i). O uso do operador % garante que a sequência se repita, caso o número de frames exceda o número de regiões. O ```r_filtrado``` pega somente os valores de r na ```lista_r``` que estão no intervalo de ```r_min``` e ```r_max```, para cada iteração. Por fim, o loop 

```
for r in r_filtrado:
        ax.plot([r] * M, pontos[r], '.', markersize=0.05, color='blue', alpha=0.5)
```

multiplica um valor de r dentro de r filtrados e multiplica pelo numero de pontos M , isto é , [3.1] * 5 ; [3.1 , 3.1 ,3.1 , 3.1 , 3.1] e em (y) temos o pontos[r], em que definimos anteriormente. Assim, 

```
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(0, 1)
    ax.set_xlabel('r', fontsize=14)
    ax.set_ylabel('x_n', fontsize=14)
    ax.set_title(f'Diagrama de Bifurcação - Zoom [{r_min:.2f}, {r_max:.2f}]', fontsize=16)
    return []

```

define alguns limites dos eixos x e y, bem como o nome de cada eixo e o titulo, retorna uma lista. Dessa maneira, executamos a simulação a partir do ```FuncAniamtion```, que recebe os seguintes parametro por definição:
(1) a figura , (2) a função que chama em cada quadro, (3) os frames ( que no caso é do tamanho da lista regiões_zoom) , (4) 