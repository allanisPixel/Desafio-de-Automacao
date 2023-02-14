from asyncio import wait
import pyautogui as pa
import pyperclip as pc
from time import sleep
from pathlib import Path

# largura por altuira 1366, 768
# ctr sft W = deslogar
# ativar venv no vs code = c:/Users/alanis.oliveira/Documents/Desafio-de-Automacao/BWA-Chalenge/venv/Scripts/Activate.ps1

lista2 = 'This_RockMa1io_Sh***_62'
lista4 = 'Drop the bass!!'

def found_image(caminho):
    path = str ((caminho))
    pular = pa.locateOnScreen(str(path))
    print(pular)
    pa.click(pular)

def detec_propaganda():
    # 5. AGUARDAR FIM DOS ANÚNCIOS
    try:
        found_image(Path.cwd() / "imagens" / "busca" / "fechar.png")
        sleep(33)

    except:
        sleep(33)

def pular():
    found_image(Path.cwd() / "imagens" / "busca" / "pular.png")

def voltar():
    found_image((Path.cwd() / "imagens" / "busca" / "voltar.png"))

# 1. ABRIR SPOTIFY DESKTOP
pa.PAUSE = 3
####################

####################
pa.press("win")
pa.write("spotify")
pa.press("enter")

sleep(4)

# X = Point(x=1074, y=144) clicar fora sai da propaganda

# 2. REALIZAR LOGIN
path =  str (Path.cwd() / "imagens" / "login" / "login.png") # da certo
imagem = pa.locateOnScreen(path)
if(imagem == None):
    print('logado :)')

else:
    # Se não tiver logado login
    print('não logado')
    path = (Path.cwd() / "imagens" / "login" / "email.png") 
    email = pa.locateOnScreen(str(path))
    pa.click(email) 
    #pa.press('delete', presses=20)
    #pa.write("baknurelte@gufum.com")

    path = str (Path.cwd() / "imagens" / "login" / "senha.png")
    senha = pa.locateOnScreen(path)

    pa.click(senha)
    pa.write("dummy333")

    path = str (Path.cwd() / "imagens" / "login" / "entrar.png")
    entrar = pa.locateOnScreen(str(path))
    pa.click(entrar)

    sleep(2)

# 3. PESQUISAR PLAYLIST 4 DA LISTA (PEQUISAR PLAYLIST 2 NA SEGUNDA EXECUÇÃO)
for i in range (2): #2
    #clique no busca 1
    found_image(Path.cwd() / "imagens" / "busca" / "busca1.png")

    #clique no busca 2
    found_image(Path.cwd() / "imagens" / "busca" / "busca2.png")   
    
    if i == 0:
        pa.write(lista4)
        found_image(Path.cwd() / "imagens" / "busca" / "playlists.png")
        found_image(Path.cwd() / "imagens" / "busca" / "drop_the_bass.png")

    else:
        pa.write(lista2)
        found_image(Path.cwd() / "imagens" / "busca" / "playlists.png")

        #RECONSTRUA ISSO

    # 4. AVANÇAR MUSICAS ATÉ APARECER ANÚNCIO (LIMITE DE 10 MUSICAS)
    # play
    sleep(3)
    found_image(Path.cwd() / "imagens" / "busca" / "play.png")

    for n in range(10):
        try:
            pular()
        except:
            detec_propaganda()
            pular()

    # 6. VOLTAR PARA MUSICA INICIAL DA PLAYLIST
    pa.scroll(-50)
    found_image(Path.cwd() / "imagens" / "busca" / "primeira.png")

    '''
    path = str (Path.cwd() / "imagens" / "busca" / "titulo.png")
    titulo = pa.locateOnScreen(str(path))
    print(titulo)
    pa.moveTo(titulo.left, titulo.top + 50)
    pa.click()
    '''

    # 7. AVANÇAR 2 MUSICAS
    for n in range(2):
        try:
            pular()
        except:
            detec_propaganda()
            pular()

    # 8. VOLTAR 5 MUSICAS
    for n in range(10):
        try:
            voltar()
        except:
            detec_propaganda()
            voltar()