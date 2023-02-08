from ast import Delete
from asyncio import wait
from contextlib import nullcontext
import pyautogui as pa
import pyperclip as pc
from time import sleep
from PIL import Image
from pathlib import Path

# largura por altuira 1366, 768
# ctr sft W = deslogar
# ativar venv no vs code = c:/Users/alanis.oliveira/Documents/Desafio-de-Automacao/BWA-Chalenge/venv/Scripts/Activate.ps1

lista2 = 'This_RockMa1io_Sh***_62'
lista4 = 'Drop the bass!!'

# 1. ABRIR SPOTIFY DESKTOP

pa.PAUSE = 1

pa.press("win")
pa.write("spotify")
pa.press("enter")

# 2. REALIZAR LOGIN

path =  str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "login.png") # da certo
#path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "busca1.png") # da errado

#vai tentar achar a imagem
imagem = pa.locateOnScreen(path)
#print(imagem)
#print(dir(imagem))
if(imagem == None):
    print('logado :)')

else:
    # Se não tiver logado login
    print('não logado')
    path = (Path.cwd() / "Pyautogui" / "imagens" / "login" / "email.png") 
    email = pa.locateOnScreen(str(path))
    pa.click(email) 
    #pa.press('delete', presses=20)
    #pa.write("baknurelte@gufum.com")
    

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "senha.png")
    senha = pa.locateOnScreen(path)

    pa.click(senha)
    pa.write("dummy333")

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "entrar.png")
    entrar = pa.locateOnScreen(str(path))
    pa.click(entrar)

    wait(5)

# 3. PESQUISAR PLAYLIST 4 DA LISTA (PEDWQUISAR PLAYLIST 2 NA SEGUNDA EXECUÇÃO)
i = 0 #2
    #clique no busca 1
    
path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "busca1.png")
pesquisar = pa.locateOnScreen(str(path))
print(pesquisar)
pa.click(pesquisar)

#clique no busca 2
path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "busca2.png")
pesquisar = pa.locateOnScreen(str(path))
print(pesquisar)
pa.click(pesquisar)
if i == 0:
    pa.write(lista4)

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "playlists.png")
    playlist = pa.locateOnScreen(str(path))
    print(playlist)
    pa.click(playlist)


    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "drop_the_bass.png")
    music = pa.locateOnScreen(str(path))
    print(music)
    pa.click(music)


# 4. AVANÇAR MUSICAS ATÉ APARECER ANÚNCIO (LIMITE DE 10 MUSICAS)baknurelte@gufum.com
# 5. AGUARDAR FIM DOS ANÚNCIOS
# 6. VOLTAR PARA MUSICA INICIAL DA PLAYLIST
# 7. AVANÇAR 2 MUSICAS
# 8. VOLTAR 5 MUSICASbaknurelte@gufum.com
# 9. REPETIR PROCESSO 2X

#screenWildth, screenHeight = pa.size()
'''
pyautogui.click(186, 439)
pyautogui.click(186, 439)
'''
