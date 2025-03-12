import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 2, 500)
func1 = np.exp(x)
func2 =np.exp(-10 * x)
func3 =np.exp(10 * x)

caminho_arquivo = './Graficos_atividade_2_intermediario/Dados da exponencial.npz'
np.savez(caminho_arquivo, x=x, y1=func1, y2=func2, y3=func3 )