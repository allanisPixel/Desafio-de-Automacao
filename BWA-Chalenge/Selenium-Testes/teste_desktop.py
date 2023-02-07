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
lista3 = 'Drop the bass!!'

# 1. ABRIR SPOTIFY DESKTOP

pa.PAUSE = 1

pa.press("win")
pa.write("spotify")
pa.press("enter")

# 2. REALIZAR LOGIN

path =  str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "login.png")
#path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "busca1.png")
    #vai tentar achar a imagem
imagem = pa.locateOnScreen(path)
print(imagem)
print(dir(imagem))
if(imagem == None):
    print('logado :)')

else:
    # Se não tiver logado login
    print('não logado')
    path = (Path.cwd() / "Pyautogui" / "imagens" / "login" / "email.png") 
    email = pa.locateOnScreen(str(path))
    pa.click(email) 
    '''
    pa.press('delete', presses=20)
    pa.write("baknurelte@gufum.com")

    '''

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "senha.png")
    senha = pa.locateOnScreen(path)

    pa.click(senha)
    pa.write("dummy333")

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "login" / "entrar.png")
    #######
    pa.click(entrar)

    wait(10)

'''
# 3. PESQUISAR PLAYLIST 4 DA LISTA (PEDWQUISAR PLAYLIST 2 NA SEGUNDA EXECUÇÃO)
for i in range(1):
    #clique no busca 1

    
    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "busca1.png")
    pa.click(path)

    #clique no busca 2

    path = str (Path.cwd() / "Pyautogui" / "imagens" / "busca" / "busca2.png")

    pa.click(str(path))

# 4. AVANÇAR MUSICAS ATÉ APARECER ANÚNCIO (LIMITE DE 10 MUSICAS)baknurelte@gufum.com
# 5. AGUARDAR FIM DOS ANÚNCIOS
# 6. VOLTAR PARA MUSICA INICIAL DA PLAYLIST
# 7. AVANÇAR 2 MUSICAS
# 8. VOLTAR 5 MUSICASbaknurelte@gufum.com
# 9. REPETIR PROCESSO 2X

#screenWildth, screenHeight = pa.size()
'''
'''
pyautogui.click(186, 439)
pyautogui.click(186, 439)
'''
