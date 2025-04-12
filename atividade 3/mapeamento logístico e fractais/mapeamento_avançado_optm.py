import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MapaLogistico:
    def __init__(self, r, x0, N):
        self.r = r
        self.x0 = x0
        self.N = N
        
    def mapa_logistico(self):
        x_n = [self.x0]
        for i in range(self.N - 1):
            novo_valor = self.r * x_n[i] * (1 - x_n[i])
            x_n.append(novo_valor)
        return x_n

# Parâmetros iniciais
M = 1000   # Quantidade de pontos plotados por r
N = 2000   # Total de iterações por r
lista_r = np.linspace(1, 4, 2000)  # 2000 valores de r entre 1 e 4

# Geração dos pontos iniciais
pontos = {}
for r in lista_r:
    simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
    pontos[r] = simulacao[-M:]  # Últimos M pontos

#
TempoTotal = 15  # s
fps = 30
TotalFrames = fps * TempoTotal

inicial = np.array([1.0, 4.0, 0.0, 1.0])  # [r_min, r_max, y_min, y_max] inicial
final = np.array([3.55, 3.6, 0.8, 0.9])    # [r_min, r_max, y_min, y_max] final

fig, ax = plt.subplots(figsize=(10, 7))


def coords(frame):
    fator = frame / (TotalFrames - 1)
    estado_atual = inicial + fator * (final - inicial)
    return estado_atual[0], estado_atual[1], estado_atual[2], estado_atual[3]


def init():
    ax.clear()
    return []

def animar(frame):
    ax.clear()
    r_min, r_max, y_min, y_max = coords(frame)
    
    # 1. Gerar mais valores de r na região de zoom
    num_r_extra = 1000  # Quantidade de novos r a gerar
    r_extra = np.linspace(r_min, r_max, num_r_extra)  # Novos valores de r
    
    # Calcular e plotar pontos adicionais
    for r in r_extra:
        simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
        pontos_filtrados = [p for p in simulacao[-M:] if y_min <= p <= y_max]
        ax.plot([r] * len(pontos_filtrados), pontos_filtrados, 
                '.', markersize=0.5, color='blue', alpha=0.5)
    
    # 2. Plotar os pontos iniciais filtrados
    r_filtrado = [r for r in lista_r if r_min <= r <= r_max]
    for r in r_filtrado:
        pontos_filtrados = [p for p in pontos[r] if y_min <= p <= y_max]
        ax.plot([r] * len(pontos_filtrados), pontos_filtrados, 
                '.', markersize=0.5, color='blue', alpha=0.5)
    
    # Configurações do gráfico
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel('r', fontsize=14)
    ax.set_ylabel('x_n', fontsize=14)
    ax.set_title(f'Diagrama de Bifurcação - Zoom [{r_min:.2f}, {r_max:.2f}]', fontsize=16)
    return []

# Criar e salvar a animação
animacao = FuncAnimation(fig, animar, frames=TotalFrames, 
                         init_func=init, interval=1000 / fps, blit=False)

animacao.save('mapa_logistico_zoom_maispontos3.gif', writer='pillow', fps=30)

plt.tight_layout()
plt.show()