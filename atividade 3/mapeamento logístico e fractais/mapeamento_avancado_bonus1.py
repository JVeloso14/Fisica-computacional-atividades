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
M = 2000
N = 3000
lista_r = np.linspace(1, 4, 2000)


pontos = {}
for r in lista_r:
    simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
    pontos[r] = simulacao[-M:]

regioes_zoom = [
    (1.0, 4.0), 
    (3.0, 4.0),   
    (3.5, 4.0),   
    (3.7, 3.9),   
    (3.8, 3.9),    
    (3.82, 3.87),  
]

print(len(regioes_zoom))

# Criar figura e os eixos
fig, ax = plt.subplots(figsize=(10, 7))

# Função de inicialização
def init():
    ax.clear()
    return []


def animar(i):
    ax.clear()
    r_min, r_max = regioes_zoom[i % len(regioes_zoom)]
    
    r_filtrado = [r for r in lista_r if r_min <= r <= r_max]
    
    for r in r_filtrado:
        ax.plot([r] * M, pontos[r], '.', markersize=0.05, color='blue', alpha=0.5)
    
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(0, 1)
    ax.set_xlabel('r', fontsize=14)
    ax.set_ylabel('x_n', fontsize=14)
    ax.set_title(f'Diagrama de Bifurcação - Zoom [{r_min:.2f}, {r_max:.2f}]', fontsize=16)
    return []


animacao = FuncAnimation(fig, animar, frames=len(regioes_zoom), 
                         init_func=init, interval=2000, blit=False)

animacao.save('mapa_logistico_zoom.gif', writer='pillow', fps=1/3)

plt.tight_layout()
plt.show()
