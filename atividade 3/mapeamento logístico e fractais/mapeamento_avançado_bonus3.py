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

# Definir as regiões de zoom com densidade razoável de pontos
regioes_zoom = [
    {"range": (1.0, 4.0), "pontos": 2000, "M": 500, "N": 2000},    
    {"range": (3.0, 4.0), "pontos": 3000, "M": 600, "N": 2000},    
    {"range": (3.5, 4.0), "pontos": 4000, "M": 700, "N": 3000},     
    {"range": (3.7, 3.9), "pontos": 5000, "M": 800, "N": 3000},     
    {"range": (3.8, 3.9), "pontos": 6000, "M": 900, "N": 4000},    
    {"range": (3.82, 3.87), "pontos": 7000, "M": 1000, "N": 4000},  
]

# Criar figura e eixos
fig, ax = plt.subplots(figsize=(10, 7))

# Variável global para armazenar pontos calculados
pontos_cache = {}

# Função para calcular os pontos para uma região específica
def calcular_pontos_regiao(indice):
    regiao = regioes_zoom[indice]
    
    # Verificar se os pontos já foram calculados
    if indice in pontos_cache:
        return pontos_cache[indice]
    
    r_min, r_max = regiao["range"]
    num_pontos = regiao["pontos"]
    M = regiao["M"]
    N = regiao["N"]
    
    lista_r = np.linspace(r_min, r_max, num_pontos)
    pontos = {}
    
    for r in lista_r:
        simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
        pontos[r] = simulacao[-M:]
    
    # Armazenar no cache
    resultado = (pontos, lista_r)
    pontos_cache[indice] = resultado
    return resultado

# Função de inicialização
def init():
    ax.clear()
    return []

def animar(i):
    ax.clear()
    
    # Obtendo região atual
    regiao = regioes_zoom[i]
    r_min, r_max = regiao["range"]
    
    pontos, lista_r = calcular_pontos_regiao(i)
    

    for r in lista_r:
        ax.plot([r] * len(pontos[r]), pontos[r], '.', markersize=0.05, color='blue', alpha=0.5)
    
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(0, 1)
    ax.set_xlabel('r', fontsize=14)
    ax.set_ylabel('x_n', fontsize=14)
    ax.set_title(f'Diagrama de Bifurcação - Zoom [{r_min:.3f}, {r_max:.3f}]\n'
                f'Pontos: {regiao["pontos"]}', fontsize=16)
    
    plt.tight_layout()
    return []

# Pré-calcular primeiro frame para inicializar a animação mais rapidamente
calcular_pontos_regiao(0)

# Criar animação
animacao = FuncAnimation(fig, animar, frames=len(regioes_zoom), 
                    init_func=init, interval=1000, blit=True)

animacao.save('mapa_logistico_zoom3.gif', writer='pillow', fps=1/3)

plt.tight_layout()
plt.show()