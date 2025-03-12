import numpy as np

x= np.linspace(-10 , 10 ,200)

func1= np.exp(-x**2)
func2 = 1.5*np.exp(-x**2)
func3 = np.exp(-2*x**2)
func4 = np.exp(-(x-1)**2)


caminho_arquivo = './Graficos_atividade_2_intermediario/Dados da gaussiana.npz'
np.savez(caminho_arquivo, x=x, y1=func1, y2=func2, y3=func3 , y4= func4 )