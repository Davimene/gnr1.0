import tkinter as tk
import tkinter.simpledialog
from random import randint

#----- PAGINAS -----

#----- PAGINA01 -----
def mostrar_pagina01():
    pagina02.pack_forget()
    pagina03.pack_forget()

    pagina01.pack()

def fechar_pagina01():
    janela.destroy()

#----- PAGINA02 -----
def mostrar_pagina02():
    pagina01.pack_forget()
    pagina03.pack_forget()

    pagina02.pack()

def fechar_pagina02():
    janela.destroy()

#----- PAGINA03 -----
def mostrar_pagina03():
    pagina01.pack_forget()
    pagina02.pack_forget()

    pagina03.pack()

def fechar_pagina03():
    janela.destroy()


#----- FIM DAS PAGINAS -----


#----- DEFINICOES DA JANELA -----

# Cria uma instância das janelas
janela = tk.Tk()

# Define o título da pagina01
janela.title("Gerador De Numero Real")

# Define as dimensões da pagina01 (largura x altura)
janela.geometry("360x540")

#----- PAGINAS COMO WIDGETS FREME -----

pagina01 = tk.Frame(janela)
pagina02 = tk.Frame(janela)
pagina03 = tk.Frame(janela)

#----- FIM PAGINAS COMO WIDGETS FREME -----

#----- CRIAÇÃO DE FUNCOES  -----

# Variável global para armazenar o rótulo de números
rotulo_numeros = None

# Função para gerar 2 números aleatórios
def gerar_a():
    return ''.join(str(randint(0, 9)) for _ in range(2))

# Função para gerar 8 números aleatórios
def gerar_b():
    return ''.join(str(randint(0, 9)) for _ in range(8))

# Função para gerar 10 números usando a lógica fornecida
def gerar_numeros():
    d = "wa.me/55"
    c = "9"
    
    # Use a função gerar_a e gerar_b para criar a lista de 10 números
    lista_numeros = [d + gerar_a() + c + gerar_b() for _ in range(10)]

    # Exiba o resultado
    mostrar_resultado(lista_numeros)

def mostrar_resultado(lista_numeros):
    if lista_numeros:
        resultado = '\n'.join(lista_numeros)
        rotulo_numeros.config(text=f"{resultado}")

        # Habilitar o botão "Copiar"
        botao_copiar.config(state=tk.NORMAL)
    else:
        rotulo_numeros.config(text="Nenhum número gerado!")

        # Desabilitar o botão "Copiar"
        botao_copiar.config(state=tk.DISABLED)

#----- CRIAÇÃO DE FUNCOES  -----

#----- INICIO DA JANELA 01 -----

# Adiciona um rótulo à pagina01
rotulo01 = tk.Label(pagina01, text="Gerador De Numero Real 1.0")
rotulo01.pack(pady=10)

# Criar botão para iniciar - ir para outra pagina.
botao_iniciar = tk.Button(pagina01, text="Iniciar", command=mostrar_pagina02)
botao_iniciar.pack(pady=10)

# Criar botão para creditos - ir para outra pagina.
botao_creditos = tk.Button(pagina01, text="Creditos", command=mostrar_pagina03)
botao_creditos.pack(pady=10)

# Cria um botão para fechar a pagina01
botao_fechar = tk.Button(pagina01, text="Fechar", command=fechar_pagina01)
botao_fechar.pack(pady=10)

# Inicialmente, mostra a primeira página
mostrar_pagina01()

#----- FINAL DA JANELA 01 -----

#----- INICIO DA JANELA 02 -----

# Adiciona um rótulo à pagina02
rotulo02 = tk.Label(pagina02, text="Gerar Números")
rotulo02.pack(pady=10)

# Criar botão para Nmr Brasil - ir para outra pagina.
botaoGerar = tk.Button(pagina02, text="Gerar", command=lambda: gerar_numeros())
botaoGerar.pack(pady=10)

texto04 = tk.Label(pagina02, text="Números gerados:")
texto04.pack(pady=3)

# Adiciona um rótulo para exibir os números gerados
rotulo_numeros = tk.Label(pagina02, text="Nenhum número gerado!")
rotulo_numeros.pack(pady=10)

# Cria um botão para copiar os números gerados
def copiar():
    numeros_copiados = rotulo_numeros.cget("text")
    janela.clipboard_clear()
    janela.clipboard_append(numeros_copiados)
    janela.update()


# Adiciona um botão "Copiar"
botao_copiar = tk.Button(pagina02, text="Copiar", command=copiar, state=tk.DISABLED)
botao_copiar.pack(pady=10)

# Criar botão para inicio - ir para outra pagina.
botao_inicio02 = tk.Button(pagina02, text="Voltar Ao Inicio", command=mostrar_pagina01)
botao_inicio02.pack(pady=10)

# Cria um botão para fechar a pagina02
botao_fechar = tk.Button(pagina02, text="Fechar", command=fechar_pagina01)
botao_fechar.pack(pady=10)

#----- FINAL DA JANELA 02 -----


#----- INICIO DA JANELA 03 -----

# Adiciona um rótulo à pagina03
rotulo03 = tk.Label(pagina03, text="CREDITOS")
rotulo03.pack(pady=10)

texto01 = tk.Label(pagina03, text="Versao:1.0")
texto01.pack(pady=10)

texto02 = tk.Label(pagina03, text="Criador: Davi Menezes")
texto02.pack(pady=10)

texto03 = tk.Label(pagina03, text="Uso livre, foda-se os direitos autorais! \n\nSe tiver afim de ajudar dando money, fique a vontade. \nMas se foda pra achar nossa carteira. \n\nFavor se for usar o codigo fonte, deixa os creditos!")
texto03.pack(pady=10)

# Criar botão para inicio - ir para outra pagina.
botao_inicio02 = tk.Button(pagina03, text="Voltar Ao Inicio", command=mostrar_pagina01)
botao_inicio02.pack(pady=10)

#----- FINAL DA JANELA 03 -----

#----- INICIO DA JANELA -----
#----- FINAL DA JANELA -----

janela.mainloop()
