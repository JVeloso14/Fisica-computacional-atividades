import numpy as np
import matplotlib.pyplot as plt

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
    

M = 1000
N = 5000

lista_r = np.linspace(1, 4, 3000)
# plt.ion() 

plt.ion()
plt.figure(figsize=(8, 6))
for r in lista_r:
    simulacao = MapaLogistico(r, 0.5, N).mapa_logistico()
    plt.plot([r] * M, simulacao[-M:], '.', markersize=0.05, color='blue', alpha=0.5)

plt.xlabel('r', fontsize=14)
plt.ylabel('x_n', fontsize=14)
plt.title('Diagrama de Bifurcação - Mapa Logístico', fontsize=16)
plt.tight_layout()
plt.ioff()
plt.show()
