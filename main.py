import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip
import keyboard
import re

placa = ""
local = ""
texto = ""
corpo = ["", ""]

# função pra validar se o texto copiado é uma placa
def validaPlaca(texto): 
    padrao_antigo = r'^[A-Za-z]{3}-\d{4}$'
    padrao_mercosul = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
    return bool(re.fullmatch(padrao_antigo, texto)) or bool(re.fullmatch(padrao_mercosul, texto))

def validaLocal(texto):
    padrao_local = r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚãõâêîôûÃÕÂÊÎÔÛçÇ,.-]+$'
    return bool(re.fullmatch(padrao_local, texto))

# função que monitora a pasta de transferência
def scan_clipboard():
    global placa, local, texto
    texto = pyperclip.paste()
    if not texto:
        return

    if validaPlaca(texto):
        placa = texto
        corpo[0] = placa
       # placa = texto
        
    elif validaLocal(texto):
        local = texto
        corpo[1] = local
       # local = texto
    print(corpo)
    app.after(500, scan_clipboard)


def saudacao_mensagem(tecla):
    saudacao = saudacao_var.get()

    if tecla == 7:  
        mensagem = f"{saudacao}! Siga Trucks Rastreamento e Monitoramento agradece seu contato!!!"
        keyboard.write(mensagem)
    

def evento_mensagem(tipo):
    global placa, local
    saudacao = saudacao_var.get()
    if tipo == 1:
        mensagem = f"""{saudacao}! {placa} Alimentação desconectada em {local}\nTudo certo por aí?"""
       
        keyboard.write(mensagem)
        keyboard.release('shift')

    elif tipo == 2:
        mensagem = f"""{saudacao}! {placa} Perda de sinal em {local}\nTudo certo por aí?"""
        
        keyboard.write(mensagem)
        keyboard.release('shift')

    elif tipo == 3:
        mensagem = f"""{saudacao}! {placa} Tudo certo por aí?\nQual o destino?"""
        
        keyboard.write(mensagem)
        keyboard.release('shift')
    

app = ttk.Window(themename="darkly")
app.title("SigaText - Macro de Mensagens")
app.geometry("600x300")
app.wm_minsize(600,300)
app.wm_maxsize(600,300)

tk.Label(app, text="Saudação:", font=("Aptos", 16,"bold")).pack(pady=5)
saudacao_var = ttk.Combobox(app, values=["Bom dia", "Boa tarde", "Boa noite"], bootstyle="primary")
saudacao_var.current(0)
saudacao_var.pack(pady=5)

tk.Label(app, text="Mensagens:", font=("Aptos", 16,"bold")).pack(pady=5)
tk.Label(app, text="Obs: Usar teclado numérico", font=("Aptos", 12,"bold")).pack(pady=5)
tk.Label(app, text="SHIFT+1 = Alimentação desconectada").pack()
tk.Label(app, text="Exemplo: [saudacao]! [placa] Alimentação desconectada em [local]" \
"Tudo certo por aí?").pack()
tk.Label(app, text="SHIFT+2 = Sem comunicação").pack()
tk.Label(app, text="SHIFT+3 = Destino").pack()
tk.Label(app, text="SHIFT+7 = Saudação").pack()

keyboard.add_hotkey('shift+1', lambda: evento_mensagem(1))
keyboard.add_hotkey('shift+2', lambda: evento_mensagem(2))
keyboard.add_hotkey('shift+3', lambda: evento_mensagem(3))
keyboard.add_hotkey('shift+7', lambda: saudacao_mensagem(7))

scan_clipboard()

app.mainloop()
