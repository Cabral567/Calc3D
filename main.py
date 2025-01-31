import numpy as np                                                     # Importa a biblioteca numpy como np
import matplotlib.pyplot as plt                                        # Importa a biblioteca matplotlib como plt
import sympy as sp                                                     # Importa a biblioteca sympy como sp

expr = input('Digite a função (exemplo: sin(x) + cos(x)): ')           # Entrada da função como expr

x = sp.symbols('x')                                                    # Associa a varivel x ao simbolo x

try:
    
    y_expr = sp.sympify(expr)                                          # Converte a expressão em uma função sympy
    
    y_func = sp.lambdify(x, y_expr, 'numpy')                           # Converte a expressao em uma função vetorizada
    
    intervalo_eixox = 100                                              # Definiçao do tamanho do intervalo do eixo x
    x_vals = np.linspace(-intervalo_eixox, intervalo_eixox, 1000)      # Associa a varivel x_vals ao intervalo do eixo x
    
    y_vals = y_func(x_vals)                                            # Calcula os valores de y correspondentes a função em um determinado ponto (x)

    plt.plot(x_vals, y_vals)                                           # Define a função para plotar o grafico

    plt.xlabel('Eixo X')                                               # Define o nome que será mostrado na tela para o eixo X
    plt.ylabel('Eixo Y')                                               # Define o nome que será mostrado na tela para o eixo Y
    plt.title(expr)                                                    # Mostra na tela como titulo a expressão (função) definida pelo usuario 

    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')        # Define o estilo do grafico, estilo de linha, espaçamento e cor

    plt.axhline(0, color='black', linewidth=1)                         # Define a cor do fundo da linha horizontal
    plt.axvline(0, color='black', linewidth=1)                         # Define a cor do fundo da linha vertical
    
    plt.show()                                                         # Chama a função para inicializar o grafico 

except Exception as e:                                                 # caso ocorra um erro define o erro expection como e
    print("Erro: ", e)                                                 # Printa na tela a palavra erro seguido do erro em si
    print("Certifique-se de que a expressão inserida é válida.")       # Printa na tela a mensagem para verficar a expressão inserida
