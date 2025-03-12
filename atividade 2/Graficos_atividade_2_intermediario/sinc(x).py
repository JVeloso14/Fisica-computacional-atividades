import numpy as np

x = np.linspace(-50,50, 200)
sinc_x = np.sin(x)/x

caminho_arquivo = './Graficos_atividade_2_intermediario/Dados de sinc(x).npz'
np.savez(caminho_arquivo, x=x, funcao= sinc_x )