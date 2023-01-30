from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Varivael i muda o comportamento do teste
# drive wait
# (Se 1 é a 1º playlist, se 1 é a 2º Playlist)
# arquivo config/acessar dado da planilha

#um arquivo guardando os xpaht e identicando quem são 
#funções e tratamento de erros(registrar os exceptions)

lista1 = 'This Is 2Pac'
lista3 = 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS'

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(
    service=service,
    options=options
)
driver.delete_all_cookies()

#use como parametro a lista das playlists
for i in range(2): #2
    email = "baknurelte@gufum.com"
    senha = "dummy333"

    #acessando site
    driver.get('https://open.spotify.com/')
    driver
    
    sleep(3)

    # Log-in
    enter = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
    enter.click()

    sleep(5)
    
    login = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")
    login.click
    (login).send_keys(email)
    login.click
    (password).send_keys(senha)
    checkbox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/label/span[1]")
    checkbox.click()
    sleep(3)
    enter = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    enter.click()
    ##
    sleep(8)

    # Realizando busca

    buton =driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a')
    buton.click()

    sleep(5)
    busca = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
    if i == 0:
        (busca).send_keys(lista1)
    elif i == 1:
        (busca).send_keys(lista3),
    else:
        print("Erro")

    sleep(3)

    #Encontra a playlist na pagina e seleciona ela

    if i == 0:
        select = driver.find_elements(By.XPATH, f"//*[contains(text(), '{lista1}' )]")
        select[1].click()
        
    elif i == 1:
        '''
        outra forma de fazer isso:
        select = driver.find_elements(By.XPATH, "//*[contains(text(), 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS' )]")[1].click

        '''
        select = driver.find_elements(By.XPATH, f"//*[contains(text(), '{lista3}' )]")
        select[1].click()

    else: 
        print('falhou')

    sleep(5)
     
    #acha o item 1 e seleciona

    #buton = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div')
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button/span')
    buton.click()
    sleep(1)
    #buton2 = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/button')
    #buton2.click()

    sleep(5)
    #pular 10
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')
    for x in range (9):
        sleep(3)
        if buton.get_attribute != 'disabled' :
            buton.click()
        else: 
            sleep(50)
            x = x - 1
    
    sleep(6)
    #volte para o 1º
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div')
    buton.click()
    sleep(2)
    #buton2 = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/button')
    buton2 = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/button')
    buton2.click()

    #pule 2
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')
    for x in range (2):
        sleep(3)
        if buton.get_attribute != 'disabled' :
            buton.click()
        else: 
            sleep(50)
            x = x - 1

    #volte 5
    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]')

    for x in range(5):
        sleep(1)
        if buton.get_attribute != 'disabled' :
            buton.click()
        else: 
            sleep(50)
            x = x - 1

    sleep(10)
    print("Feito!!")
    driver.delete_all_cookies()
    #driver.close()

    
    
