import tkinter as tk
from tkinter import ttk
import pyperclip
import keyboard
import ctypes
from ctypes import windll

ultimo_copiado = []

def monitorar_clipboard():
    global ultimo_copiado
    texto = pyperclip.paste()
    if texto and (not ultimo_copiado or texto != ultimo_copiado[-1]):
        ultimo_copiado.append(texto)
        if len(ultimo_copiado) > 2:
            ultimo_copiado.pop(0)
    app.after(500, monitorar_clipboard)

def gerar_mensagem(tipo):
    saudacao = saudacao_var.get()

    if len(ultimo_copiado) < 2:
        return

    placa, local = ultimo_copiado

    if tipo == 1:
        mensagem = f"""{saudacao}! {placa} Alimentação desconectada em {local}\nTudo certo por aí?"""

    elif tipo == 2:
        mensagem = f"""{saudacao}! {placa} Perda de sinal em {local}\nTudo certo por aí?"""

    elif tipo == 3:
        mensagem = f"""{saudacao}! {placa} Tudo certo por aí?\nQual o destino?"""
    
    elif tipo == 4:
        mensagem = f"""{saudacao}! SIGA TRUCKS agradece seu contato!!!\nQual o seu nome e como podemos ajudar?"""

    pyperclip.copy(mensagem)
    keyboard.write(mensagem)
    pyperclip.copy('')

app = tk.Tk()
app.title("Gerador de Mensagens")
app.geometry("300x150")

tk.Label(app, text="Saudação:").pack(pady=5)
saudacao_var = ttk.Combobox(app, values=["Bom dia", "Boa tarde", "Boa noite"])
saudacao_var.current(0)
saudacao_var.pack()

tk.Label(app, text="CTRL+SHIFT+1 = Alimentação desconectada").pack(pady=5)
tk.Label(app, text="CTRL+SHIFT+2 = Sem comunicação").pack()
tk.Label(app, text="CTRL+SHIFT+3 = Destino").pack()
tk.Label(app, text="CTRL+SHIFT+4 = Saudação").pack()

keyboard.add_hotkey('ctrl+shift+1', lambda: gerar_mensagem(1))
keyboard.add_hotkey('ctrl+shift+2', lambda: gerar_mensagem(2))
keyboard.add_hotkey('ctrl+shift+3', lambda: gerar_mensagem(3))
keyboard.add_hotkey('ctrl+shift+4', lambda: gerar_mensagem(4))

monitorar_clipboard()

app.mainloop()
