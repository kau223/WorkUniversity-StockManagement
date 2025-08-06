import tkinter as tk
import subprocess
import sys
import os

def abrir_main():
    janela.destroy()

    if sys.platform.startswith("linux") or sys.plataform == "darwin":
        subprocess.Popen(["gnome-terminal", "--", "python3", "main.py"])
    elif sys.platform == "win32":
        subprocess.Popen(["start", "cmd", "/k", "python main.py"], shell=True)
janela = tk.Tk()
janela.title("Gerenciador de Estoque")

botao = tk.Button(janela, text="Começar", command=abrir_main)
botao.pack(pady=10)

janela.mainloop()
