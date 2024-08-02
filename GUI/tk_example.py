from tkinter import Tk, Label, Entry, Button, StringVar

janela = Tk()

# widgets (componentes)
label = Label(janela, text="Nome:")
nome = Entry(janela)

var = StringVar()
mensagem = Label(janela, textvariable=var)


def callback_diga_ola():
    nome_digitado = nome.get()
    var.set(f"Olá {nome_digitado}, boas vindas!!!")


diga_ola = Button(janela, text="Diga Olá", command=callback_diga_ola)
sair = Button(janela, text="Sair", command=janela.destroy)

"""
-----------------
|   1   |   2   |
-----------------
|   1   |   2   |
-----------------
"""

# Posicionar
label.grid(column=1, row=1)
nome.grid(column=2, row=1)
mensagem.grid(column=2, row=2)
diga_ola.grid(column=2, row=3)
sair.grid(column=2, row=4)

janela.mainloop()
