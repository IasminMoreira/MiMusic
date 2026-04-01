from mutagen import File
import pygame
import os

pasta = r"C:\Users\Aluno\Desktop\mimusic\musicas"

pygame.init()
pygame.mixer.init()

#lista todos os arquivos da pasta
musicas = os.listdir(pasta)
#filtra apenas os arquivos convertidos
musicas = [musica for musica in musicas if musica.endswith('_conv.mp3')]

#carrega os metadados das músicas
musicas_info = []
for musica in musicas:
    caminho = os.path.join(pasta, musica)
    audio = File(caminho)
    
    if audio and audio.tags:
        titulo = audio.tags.get("TIT2", ["Desconhecido"])[0]
        artista = audio.tags.get("TPE1", ["Desconhecido"])[0]
    else:
        titulo = "Desconhecido"
        artista = "Desconhecido"
    
    musicas_info.append({'titulo': str(titulo), 'artista': str(artista), 'caminho': caminho})

#imprime as informações da música que está tocando
def tocar_musica(musica):
    pygame.mixer.music.load(musica['caminho'])
    pygame.mixer.music.play()
    print(f"Tocando: {musica['titulo']} - {musica['artista']}")

#espera a música terminar para tocar a próxima
while True:
    for musica in musicas_info:
        tocar_musica(musica)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)