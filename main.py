import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Entrada da função
expr = input('Digite a função (exemplo: sin(x) + cos(x)): ')

# Símbolo para a variável x
x = sp.symbols('x')

try:
    # Convertendo a expressão em uma função sympy
    y_expr = sp.sympify(expr)

    # Convertendo a função sympy em uma função numpy vetorizada
    y_func = sp.lambdify(x, y_expr, 'numpy')

    # Intervalo para o eixo x
    intervalo_eixox = 100
    x_vals = np.linspace(-intervalo_eixox, intervalo_eixox, 1000)

    # Calculando os valores de y correspondentes
    y_vals = y_func(x_vals) #aqui esta a funcao propriamente configurada

    # Plotando o gráfico
    plt.plot(x_vals, y_vals)

    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title(expr)
    # Estilo
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # inicia o gráfico
    plt.show()

except Exception as e:
    print("Erro: ", e)
    print("Certifique-se de que a expressão inserida é válida.")
