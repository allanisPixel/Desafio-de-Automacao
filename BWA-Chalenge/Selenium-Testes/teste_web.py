from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# drive
# (Se 1 é a 1º playlist, se 1 é a 2º Playlist)
# arquivo config/acessar dado da planilha

#use como parametro a lista das playlists

# um arquivo guardando os xpaht e identicando quem são 
# funções e tratamento de erros(registrar os exceptions)

lista1 = 'This Is 2Pac'
lista3 = 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS'

email = "baknurelte@gufum.com"
senha = "dummy333" 

t=10

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(
    service=service,
    options=options
)
driver.delete_all_cookies()

def acessar_site(t):
    driver.get('https://open.spotify.com/')
    WebDriverWait(driver, timeout=t).until(ec.new_window_is_opened)

def login(t):
    WebDriverWait(driver, timeout=t).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]'))).click()
    WebDriverWait(driver, timeout=t).until(ec.element_to_be_clickable((By.ID, "login-username"))).send_keys(email)
    WebDriverWait(driver, timeout=t).until(ec.element_to_be_clickable((By.ID, "login-password"))).send_keys(senha)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/label/span[1]").click()
    sleep(5)
    WebDriverWait(driver, timeout=10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

def busca_musica():
    # Realizando busca
    WebDriverWait(driver, timeout=20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a'))).click()
    busca = WebDriverWait(driver, timeout=20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')))

    if i == 0:
        (busca).send_keys(lista1)
        sleep(3)
        # Forma 1 de se fazer
        driver.find_elements(By.XPATH, f"//*[contains(text(), '{lista1}' )]")[1].click()

    else:
        (busca).send_keys(lista3)
        sleep(5)
        # forma 2 de se fazer   
        select = driver.find_elements(By.XPATH, f"//*[contains(text(), '{lista3}' )]")
        select[0].click()

    sleep(6)
    
#ajuste isso depois
'''
def pular:
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button/span').click()
    sleep(4)
    #pular 10
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')
    for x in range (10):
        sleep(3)
        WebDriverWait(driver, timeout=50).until(ec.element_to_be_clickable((buton))).click()
    sleep(5)

def voltar:
'''

for i in range(2): #2
    try:
        acessar_site(t)
    except:
        acessar_site(t+10)
    try: 
        login(t)
    except:
        login(t+10)
    try:
        busca_musica()
    except:
        busca_musica()

    #acha o item 1 e seleciona
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button/span').click()
    sleep(4)
    #pular 10
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')
    for x in range (10):
        sleep(3)
        WebDriverWait(driver, timeout=50).until(ec.element_to_be_clickable((buton))).click()
    sleep(5)

    #volte para o 1º
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/span').click()
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/button').click()

    #pule 2
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')
    for x in range (2):
        sleep(3)
        WebDriverWait(driver, timeout=50).until(ec.element_to_be_clickable((buton))).click()

    #volte 5
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]')
    for x in range(5):
        sleep(3)
        WebDriverWait(driver, timeout=50).until(ec.element_to_be_clickable((buton))).click()

    sleep(10)
    print("Feito!!")
    driver.delete_all_cookies()