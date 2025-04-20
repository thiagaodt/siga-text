import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip
import keyboard
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

def saudacao_mensagem(tecla):
    saudacao = saudacao_var.get()

    if tecla == 7:  
        mensagem = f"{saudacao}! Como podemos ajudar?"
        keyboard.write(mensagem)
    

def evento_mensagem(tipo):
    saudacao = saudacao_var.get()

    if len(ultimo_copiado) < 2:
        return

    placa, local = ultimo_copiado

    if tipo == 1:
        mensagem = f"""{saudacao}! {placa} Alimentação desconectada em {local}\nTudo certo por aí?"""

    elif tipo == 2:
        mensagem = f"""{saudacao}! {placa} Perda de sinal em {local}\nTudo certo por aí?"""

    elif tipo == 3:
        mensagem = f"""{saudacao}! {placa} Tudo certo por aí?"""
    
    pyperclip.copy(mensagem)
    keyboard.write(mensagem)
    pyperclip.copy('')

app = ttk.Window(themename="darkly")
app.title("SigaText - Macro de Mensagens")
app.iconbitmap("icone.ico")
app.geometry("600x300")
app.wm_minsize(600,300)
app.wm_maxsize(600,300)

tk.Label(app, text="Saudação:", font=("Aptos", 16,"bold")).pack(pady=5)
saudacao_var = ttk.Combobox(app, values=["Bom dia", "Boa tarde", "Boa noite"], bootstyle="primary")
saudacao_var.current(0)
saudacao_var.pack(pady=5)

tk.Label(app, text="Mensagens:", font=("Aptos", 16,"bold")).pack(pady=5)
tk.Label(app, text="Obs: Usar teclado numérico e copiar primeiro a placa, depois o local", font=("Aptos", 10,"bold")).pack(pady=5)
tk.Label(app, text="SHIFT+1 = Alimentação desconectada").pack()
tk.Label(app, text="SHIFT+2 = Sem comunicação").pack()
tk.Label(app, text="SHIFT+3 = Destino").pack()
tk.Label(app, text="SHIFT+7 = Saudação").pack()


keyboard.add_hotkey('shift+1', lambda: evento_mensagem(1))
keyboard.add_hotkey('shift+2', lambda: evento_mensagem(2))
keyboard.add_hotkey('shift+3', lambda: evento_mensagem(3))
keyboard.add_hotkey('shift+7', lambda: saudacao_mensagem(7))

monitorar_clipboard()

app.mainloop()
