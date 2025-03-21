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

# Parâmetros
M = 2000     # Quantidade de iterações a serem exibidas (descartando as primeiras)
N = 3000     # Total de iterações da simulação
lista_r = np.linspace(1, 4, 2000)

# Pré-calcular todos os pontos do mapa logístico para cada valor de r
pontos = {}
for r in lista_r:
    simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
    pontos[r] = simulacao[-M:]

# Definir regiões de zoom (r_min, r_max) para cada etapa da animação
regioes_zoom = [
    (1.0, 4.0), 
    (3.0, 4.0),   
    (3.5, 4.0),   
    (3.7, 3.9),   
    (3.8, 3.9),    
    (3.82, 3.87),  
]


num_frames_por_zoom = 60  
total_frames = (len(regioes_zoom) - 1) * num_frames_por_zoom


fig, ax = plt.subplots(figsize=(10, 7))

# Função para calcular os limites de zoom interpolados para o frame atual
def calcular_limites_interpolados(frame):
    indice_regiao = int(frame / num_frames_por_zoom)
    if indice_regiao >= len(regioes_zoom) - 1:
        return regioes_zoom[-1]
    fator = (frame % num_frames_por_zoom) / num_frames_por_zoom
    r_min_origem, r_max_origem = regioes_zoom[indice_regiao]
    r_min_destino, r_max_destino = regioes_zoom[indice_regiao + 1]
    r_min_atual = r_min_origem + fator * (r_min_destino - r_min_origem)
    r_max_atual = r_max_origem + fator * (r_max_destino - r_max_origem)
    return (r_min_atual, r_max_atual)


def init():
    ax.clear()
    return []


def animar(frame):
    ax.clear()
    r_min, r_max = calcular_limites_interpolados(frame)
    
  
    r_filtrado = [r for r in lista_r if r_min <= r <= r_max]
    
  
    for r in r_filtrado:
        ax.plot([r] * M, pontos[r], '.', markersize=0.5, color='blue', alpha=0.5)
    
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(0, 1)
    ax.set_xlabel('r', fontsize=14)
    ax.set_ylabel('x_n', fontsize=14)
    ax.set_title(f'Diagrama de Bifurcação - Zoom [{r_min:.2f}, {r_max:.2f}]', fontsize=16)
    return []

# Cria a animação
animacao = FuncAnimation(fig, animar, frames=total_frames, 
                         init_func=init, interval=33.3, blit=False)

# Salva a animação como GIF 
animacao.save('mapa_logistico_zoom_suave.gif', writer='pillow', fps=30)

plt.tight_layout()
plt.show()
