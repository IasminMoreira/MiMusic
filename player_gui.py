import tkinter as tk
import pygame
import os
from mutagen import File

# configura o pygame
pygame.init()
pygame.mixer.init()

# carrega as músicas
pasta = r"C:\Users\Aluno\Desktop\mimusic\musicas"
musicas = [m for m in os.listdir(pasta) if m.endswith('_conv.mp3')]

musicas_info = []
for musica in musicas:
    caminho = os.path.join(pasta, musica)
    audio = File(caminho)
    if audio and audio.tags:
        titulo = audio.tags.get("TIT2", ["Desconhecido"])[0]
        artista = audio.tags.get("TPE1", ["Desconhecido"])[0]
    else:
        titulo = musica.replace('_conv.mp3', '')
        artista = "Desconhecido"
    musicas_info.append({'titulo': str(titulo), 'artista': str(artista), 'caminho': caminho})

# estado do player
indice_atual = 0
tocando = False

# funções
def tocar():
    global tocando, indice_atual
    musica = musicas_info[indice_atual]
    pygame.mixer.music.load(musica['caminho'])
    pygame.mixer.music.play()
    tocando = True
    atualizar_labels()
    btn_play.config(text="⏸ Pausar")

def pausar():
    global tocando
    if tocando:
        pygame.mixer.music.pause()
        tocando = False
        btn_play.config(text="▶ Play")
    else:
        pygame.mixer.music.unpause()
        tocando = True
        btn_play.config(text="⏸ Pausar")

def proxima():
    global indice_atual
    indice_atual = (indice_atual + 1) % len(musicas_info)
    tocar()

def anterior():
    global indice_atual
    indice_atual = (indice_atual - 1) % len(musicas_info)
    tocar()

def atualizar_labels():
    musica = musicas_info[indice_atual]
    label_titulo.config(text=musica['titulo'])
    label_artista.config(text=musica['artista'])

# janela
janela = tk.Tk()
janela.title("MiMusic Player")
janela.geometry("320x500")
janela.configure(bg="#1a1a2e")

label_titulo = tk.Label(janela, text="Nenhuma música", font=("Arial", 14, "bold"), bg="#1a1a2e", fg="white")
label_titulo.pack(pady=30)

label_artista = tk.Label(janela, text="---", font=("Arial", 11), bg="#1a1a2e", fg="#aaaaaa")
label_artista.pack()

# botões
frame_botoes = tk.Frame(janela, bg="#1a1a2e")
frame_botoes.pack(pady=30)

btn_anterior = tk.Button(frame_botoes, text="⏮", font=("Arial", 18), bg="#16213e", fg="white", border=0, command=anterior)
btn_anterior.pack(side="left", padx=10)

btn_play = tk.Button(frame_botoes, text="▶ Play", font=("Arial", 14), bg="#0f3460", fg="white", border=0, command=lambda: pausar() if tocando else tocar())
btn_play.pack(side="left", padx=10)

btn_proxima = tk.Button(frame_botoes, text="⏭", font=("Arial", 18), bg="#16213e", fg="white", border=0, command=proxima)
btn_proxima.pack(side="left", padx=10)

janela.mainloop()