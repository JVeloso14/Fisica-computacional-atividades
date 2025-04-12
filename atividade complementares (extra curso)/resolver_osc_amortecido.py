import numpy as np
from scipy.integrate import solve_ivp

# Definir os parâmetros e o intervalo de tempo
t = np.linspace(0, 15, 1000)  # 1000 pontos entre 0 e 15
y = [0, 1]  # Condições iniciais: y(0)=0 e y'(0)=1
omega_quadrado = 100
gamma = 1

# Definir a função do oscilador amortecido
def oscilador_amortecido(t, y):
    return (y[1], (-gamma * y[1] - omega_quadrado * y[0]))

# Resolver a equação diferencial
solucao = solve_ivp(oscilador_amortecido, [0, 15], y0=y, t_eval=t, method='RK45')

# Salvar os dados no arquivo .npz usando keyword arguments
np.savez('dados_oscilador.npz', tempo=t, posicao=solucao.y[0])
