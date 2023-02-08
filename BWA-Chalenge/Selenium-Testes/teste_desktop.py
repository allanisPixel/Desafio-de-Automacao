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

#lista2 = 'This_RockMa1io_Sh***_62' #nunca nem vi
lista2 = 'This Is Roc Marciano'

lista4 = 'Drop the bass!!'

def pular():
    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "pular.png")
    pular = pa.locateOnScreen(str(path))
    print(pular)
    pa.click(pular)


def voltar():

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "voltar.png")
    pular = pa.locateOnScreen(str(path))
    print(pular)
    pa.click(pular)


# 1. ABRIR SPOTIFY DESKTOP

pa.PAUSE = 3

pa.press("win")
pa.write("spotify")
pa.press("enter")

sleep(8)
# 2. REALIZAR LOGIN

path =  str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "login.png") # da certo

#vai tentar achar a imagem
imagem = pa.locateOnScreen(path)
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

    sleep(4)

# 3. PESQUISAR PLAYLIST 4 DA LISTA (PEDWQUISAR PLAYLIST 2 NA SEGUNDA EXECUÇÃO)
# 9. REPETIR PROCESSO 2X


#clique no busca 1
for i in range (2): #2


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
        sleep(3)
        path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "playlists.png")
        playlist = pa.locateOnScreen(str(path), confidence= 0.9)
        print(playlist)
        pa.click(playlist)

        sleep(2)
        path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "drop_the_bass.png")
        music = pa.locateOnScreen(str(path))
        print(music)
        pa.click(music)

    else:
        pa.write(lista2)
        sleep(3)
        path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "playlists.png")
        playlist = pa.locateOnScreen(str(path), confidence= 0.9)
        print(playlist)
        pa.click(playlist)

        sleep(2)
        path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "drop_the_bass.png")
        music = pa.locateOnScreen(str(path))
        print(music)
        pa.click(music)

    # 4. AVANÇAR MUSICAS ATÉ APARECER ANÚNCIO (LIMITE DE 10 MUSICAS)baknurelte@gufum.com
    # 5. AGUARDAR FIM DOS ANÚNCIOS
    # play
    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "play.png")
    play = pa.locateOnScreen(str(path))
    print(play)
    pa.click(play)

    for n in range(10):
        try:
            pular()
        except:
            try:
                #se encontrar x, mate se não espere
                path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "fechar.png")
                fechar = pa.locateOnScreen(str(path), confidence= 0.9)
                print(fechar)
                pa.click(fechar)

                sleep(35)
                pular()

            except:
                sleep(35)
                pular()

    # 6. VOLTAR PARA MUSICA INICIAL DA PLAYLIST
    pa.scroll(3)

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "primeira.png")
    music = pa.locateOnScreen(str(path))
    print(music)
    pa.click(music)


    # 7. AVANÇAR 2 MUSICAS
    for n in range(2):
        try:
            pular()
        except:
            try:
                #se encontrar x, mate se não espere
                path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "fechar.png")
                fechar = pa.locateOnScreen(str(path), confidence= 0.9)
                print(fechar)
                pa.click(fechar)

                sleep(35)

                pular()

            except:
                sleep(50)
                pular()

    # 8. VOLTAR 5 MUSICASbaknurelte@gufum.com
    for n in range(10):
        try:
            voltar()
        except:
            try:
                #se encontrar x, mate se não espere
                path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "fechar.png")
                fechar = pa.locateOnScreen(str(path), confidence= 0.9)
                print(fechar)
                pa.click(fechar)

                sleep(35)


                voltar()

            except:
                sleep(50)
                voltar()



    #screenWildth, screenHeight = pa.size()
    '''
    pyautogui.click(186, 439)
    pyautogui.click(186, 439)
    '''
