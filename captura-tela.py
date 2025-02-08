import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import io
import os

def capturar_tela():
    # Simulação da captura de tela via Lightshot (API fictícia, Lightshot não oferece API pública)
    url = "https://prnt.sc/captura_exemplo.png"  # Exemplo fictício
    response = requests.get(url)
    if response.status_code == 200:
        img_data = io.BytesIO(response.content)
        carregar_imagem(img_data)
    else:
        messagebox.showerror("Erro", "Falha ao capturar a tela")

def carregar_imagem(caminho):
    global img, img_tk
    try:
        img = Image.open(caminho)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")

def abrir_ficheiro():
    caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp")])
    if caminho:
        carregar_imagem(caminho)

def gravar_ficheiro():
    if img:
        caminho = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")])
        if caminho:
            img.save(caminho)

def renomear_automaticamente():
    if img:
        pasta = filedialog.askdirectory()
        if pasta:
            novo_nome = os.path.join(pasta, "imagem_renomeada.png")
            img.save(novo_nome)
            messagebox.showinfo("Sucesso", f"Imagem renomeada e salva em: {novo_nome}")

def editar_imagem():
    messagebox.showinfo("Editar", "Função de edição ainda não implementada")

def criar_imagem():
    global img, img_tk
    img = Image.new("RGB", (800, 600), "white")
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

def sair():
    janela.quit()

# Criar a janela principal
janela = tk.Tk()
janela.title("Visualizador de Imagens")
janela.geometry("800x600")

# Criar um Canvas para exibir a imagem
canvas = tk.Canvas(janela, width=780, height=500, bg="gray")
canvas.pack()

# Criar os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

btn_capturar = tk.Button(frame_botoes, text="Pegar Tela", command=capturar_tela)
btn_capturar.grid(row=0, column=0)

btn_editar = tk.Button(frame_botoes, text="Editar Imagem", command=editar_imagem)
btn_editar.grid(row=0, column=1)

btn_criar = tk.Button(frame_botoes, text="Criar", command=criar_imagem)
btn_criar.grid(row=0, column=2)

btn_abrir = tk.Button(frame_botoes, text="Abrir", command=abrir_ficheiro)
btn_abrir.grid(row=0, column=3)

btn_gravar = tk.Button(frame_botoes, text="Gravar", command=gravar_ficheiro)
btn_gravar.grid(row=0, column=4)

btn_renomear = tk.Button(frame_botoes, text="Renomear Automaticamente", command=renomear_automaticamente)
btn_renomear.grid(row=0, column=5)

btn_sair = tk.Button(frame_botoes, text="Sair", command=sair)
btn_sair.grid(row=0, column=6)

janela.mainloop()
