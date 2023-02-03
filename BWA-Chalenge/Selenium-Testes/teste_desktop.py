import pyautogui
import PIL
from PIL import Image

# largura por altuira 1366, 768

'''
1. ABRIR SPOTIFY DESKTOP
2. REALIZAR LOGIN
3. PESQUISAR PLAYLIST 4 DA LISTA (PEDWQUISAR PLAYLIST 2 NA SEGUNDA EXECUÇÃO)
4. AVANÇAR MUSICAS ATÉ APARECER ANÚNCIO (LIMITE DE 10 MUSICAS)
5. AGUARDAR FIM DOS ANÚNCIOS
6. VOLTAR PARA MUSICA INICIAL DA PLAYLIST
7. AVANÇAR 2 MUSICAS
8. VOLTAR 5 MUSICAS
9. REPETIR PROCESSO 2X

'''



screenWildth, screenHeight = pyautogui.size()
'''
pyautogui.click(186, 439)
pyautogui.click(186, 439)
'''

pyautogui.locateOnScreen('.\Pyautogui\images\spotIcon.png')
