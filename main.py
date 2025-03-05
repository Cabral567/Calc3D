import numpy as np                                                                      # Importa a biblioteca numpy
import matplotlib.pyplot as plt                                                         # Importa a biblioteca matplotlib
import sympy as sp                                                                      # Importa a biblioteca para expressões matemáticas
import tkinter as tk                                                                    # Importa a biblioteca para criar janelas e botões
from tkinter import messagebox                                                          # Importa a biblioteca para exibir caixas de mensagem de erro
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk   # Importa a biblioteca que permite adicionar o gráfico à janela

def desenha_e_mostra_info(expressao, onde_desenhar_grafico, onde_mostrar_info):
    x = sp.symbols('x')                                                                 # 'x' é uma variável matemática
    try:
        y = sp.sympify(expressao)                                                       # Converte a expressão digitada pelo usuário para uma fórmula matemática
        funcao_y = sp.lambdify(x, y, 'numpy')                                           # Cria uma função que pode ser usada para calcular os valores de y

        intervalo_x = np.linspace(-10, 10, 1000)                                        # Cria um intervalo de valores para o eixo x
        valores_y = funcao_y(intervalo_x)                                               # Calcula os valores correspondentes de y

        figura, eixos = plt.subplots(figsize=(8, 6))                                    # Cria a figura e os eixos do gráfico
        eixos.plot(intervalo_x, valores_y)                                              # Plota a linha do gráfico
        eixos.set_xlabel('Eixo X')                                                      # Define o nome do eixo x
        eixos.set_ylabel('Eixo Y')                                                      # Define o nome do eixo y
        eixos.set_title(f'Gráfico de: {expressao}')                                     # Define o título do gráfico
        eixos.grid(True)                                                                # Ativa a grade no gráfico
        eixos.axhline(0, color='black')                                                 # Desenha a linha horizontal no eixo y = 0
        eixos.axvline(0, color='black')                                                 # Desenha a linha vertical no eixo x = 0
        eixos.set_xlim(min(intervalo_x), max(intervalo_x))                              # Ajusta os limites do eixo x
        eixos.set_ylim(min(valores_y), max(valores_y))                                  # Ajusta os limites do eixo y

        for widget in onde_desenhar_grafico.winfo_children():
            widget.destroy()                                                            # Remove qualquer gráfico anterior da tela
        canvas = FigureCanvasTkAgg(figura, master=onde_desenhar_grafico)                # Coloca o gráfico em um espaço da janela
        canvas.draw()                                                                   # Desenha o gráfico
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)                          # Exibe o gráfico na janela

        barra = NavigationToolbar2Tk(canvas, onde_desenhar_grafico)                     # Adiciona uma barra de ferramentas
        barra.update()                                                                  # Atualiza a barra de ferramentas
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        raizes = sp.solve(y, x)                                                         # Calcula as raízes da função (onde ela cruza o eixo x)
        derivada = sp.diff(y, x)                                                        # Calcula a derivada da função
        
        pontos_criticos = sp.solve(derivada, x)                                         # Calcula os pontos críticos (onde a função muda de direção)
        
        assintota_horizontal = sp.limit(y, x, sp.oo) if sp.limit(y, x, sp.oo) == sp.limit(y, x, -sp.oo) else None  # Calcula a assíntota horizontal
        assintotas_verticais = [f"x = {raiz}" for raiz in sp.solve(sp.denom(y), x) if sp.denom(y) != 1]            # Calcula as assíntotas verticais

        
        info = f"Função: {y}\nRaízes: {raizes}\nPontos críticos: {pontos_criticos}\nAssíntota horizontal: {assintota_horizontal}\nAssíntotas verticais: {assintotas_verticais}"
        onde_mostrar_info.config(text=info)                                             # Exibe as informações da função na janela

        
        if assintota_horizontal is not None:
            eixos.axhline(y=assintota_horizontal, color='red', linestyle='--')          # Desenha a assíntota horizontal no gráfico
        for assintota in assintotas_verticais:
            try:
                eixos.axvline(x=float(assintota.split('=')[1]), color='red', linestyle='--')  # Desenha as assíntotas verticais no gráfico
            except:
                pass

    except Exception as erro:
        
        messagebox.showerror("Erro", f"Erro: {erro}\nVerifique a função.")               # Exibe uma mensagem de erro caso algo dê errado


def cria_janela_principal():                                                             # Função para criar a janela principal do programa
    def ao_clicar_botao_gerar():                                                         # Função chamada quando o botão "Gerar" é clicado
        
        texto_digitado = campo_funcao.get()                                              # Pega o texto digitado pelo usuário
        if texto_digitado:
            desenha_e_mostra_info(texto_digitado, espaco_grafico, texto_info)            # Chama a função para desenhar o gráfico e exibir as informações
        else:
            messagebox.showwarning("Aviso", "Digite uma função.")                        # Exibe um aviso caso o usuário não tenha digitado nada

    janela = tk.Tk()                                                                     # Cria a janela principal
    janela.title("Gerador de Gráfico")                                                   # Define o título da janela
    janela.geometry("800x600")                                                           # Define o tamanho da janela

    frame_entrada = tk.Frame(janela)                                                     # Cria um espaço para o usuário digitar a função
    frame_entrada.pack(pady=20)                                                          # Exibe o espaço na janela

    tk.Label(frame_entrada, text="Função:").grid(row=0, column=0, padx=10)               # Exibe o texto "Função:"
    campo_funcao = tk.Entry(frame_entrada, width=50)                                     # Cria um campo para o usuário digitar a função
    campo_funcao.grid(row=0, column=1, padx=10)                                          # Exibe o campo de entrada na janela
    tk.Button(frame_entrada, text="Gerar", command=ao_clicar_botao_gerar).grid(row=1, columnspan=2, pady=10)  # Exibe o botão "Gerar"

    espaco_grafico = tk.Frame(janela)                                                    # Cria um espaço para o gráfico
    espaco_grafico.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)                         # Exibe o espaço na janela

    frame_info = tk.Frame(janela)                                                        # Cria um espaço para as informações da função
    frame_info.pack(side=tk.RIGHT, fill=tk.Y, padx=20)                                   # Exibe o espaço na janela
    texto_info = tk.Label(frame_info, text="Informações", justify=tk.LEFT)               # Exibe o texto "Informações"
    texto_info.pack(pady=10)                                                             # Exibe o texto na janela

    janela.mainloop()                                                                    # Inicia a execução do programa

if __name__ == "__main__":
    cria_janela_principal()                                                              # Chama a função para criar a janela principal
