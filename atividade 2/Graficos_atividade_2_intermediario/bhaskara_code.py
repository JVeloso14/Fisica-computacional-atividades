import numpy as np

# Coeficientes das equações quadráticas
a = 1
b = -5
c = 6

d = 1
e = -10
f = 25

def Bhaskara(a, b, c):
    """
    Calcula as raízes reais da equação quadrática ax² + bx + c = 0 utilizando a fórmula de Bhaskara.

    Parâmetros:
        a (float): Coeficiente quadrático (não pode ser zero).
        b (float): Coeficiente linear.
        c (float): Termo constante.

    Retorna:
        tuple: Raízes reais da equação quadrática. Se delta = 0, retorna uma única raiz.
    
    Levanta:
        AssertionError: Se 'a' for zero (a equação deixaria de ser quadrática).
        ValueError: Se delta for negativo (não há raízes reais).

    Exemplo:
        >>> Bhaskara(1, -5, 6)
        (3.0, 2.0)
    """
    delta = b**2 - 4 * a * c
    assert a != 0, "O coeficiente 'a' não pode ser zero"

    if delta < 0:
        raise ValueError('O delta não pode ser negativo')

    if delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        return (x1, x2)

# Cálculo das raízes das equações quadráticas
raizes = Bhaskara(a, b, c)
raizes2 = Bhaskara(d, e, f)

# Definição do intervalo de x e cálculo das funções quadráticas
x = np.linspace(-1, 6, 200)
y = a * x**2 + b * x + c
y2 = d * x**2 + e * x + f

# Caminho do arquivo para armazenar os dados
caminho_arquivo = './Graficos_atividade_2_intermediario/Dados_de_Bhaskara.npz'

# Salvando os dados no formato .npz para posterior análise
np.savez(caminho_arquivo, x=x, y=y, y2=y2, raizes=raizes, raizes2=raizes2, a=a, b=b, c=c, d=d, e=e, f=f)
