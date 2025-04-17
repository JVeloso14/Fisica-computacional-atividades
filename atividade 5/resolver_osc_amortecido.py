import numpy as np
from scipy.integrate import solve_ivp


t = np.linspace(0, 100, 10000) 
y = [0, 1]  # Condições iniciais: y(0)=0 e y'(0)=1
omega_quadrado = 2*np.pi
b  = 2

def oscilador_amortecido(t, y):
    return (y[1], (-b * y[1] - omega_quadrado * y[0]))

solucao = solve_ivp(oscilador_amortecido, [0, 100], y0=y, t_eval=t, method='RK45')

np.savez('dados_oscilador_minimo.npz', tempo=t, posicao=solucao.y[0])
