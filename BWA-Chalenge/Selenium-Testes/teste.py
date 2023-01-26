from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Varivael i muda o comportamento do teste
# drive wait
# (Se 1 é a 1º playlist, se 1 é a 2º Playlist)

lista1 = 'This is 2Pac'
lista3 = 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS'

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(
    service=service,
)


for i in range(2): #2
    email = "alanisisabelle@gmail.com"
    senha = "azaleia987654123"

    #acessando site
    #driver = webdriver.Chrome()
    driver.get('https://open.spotify.com/')
    
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
    #checkbox = driver.find_element(By.ID, "login-remember")
    checkbox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/label/span[1]")
    checkbox.click()
    sleep(5)
    #enter1 = driver.find_element(By.ID, "login-button")
    enter = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    enter.click()
    ##
    sleep(15)

    # Realizando busca

    buton =driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a')
    buton.click()


    sleep(10)
    busca = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
    #conserte esse selector
    i = {

        0: (busca).send_keys(lista1),
        1: (busca).send_keys(lista3),

    }
    sleep(3)

    if i == 0:
        select = driver.find_elements(By.XPATH, "//*[contains(text(), 'This Is 2Pac' )]")
        select[1].click()
        

    elif i == 1:
        '''
        outra forma de fazer isso:
        select = driver.find_elements(By.XPATH, "//*[contains(text(), 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS' )]")[0].click

        '''
        select = driver.find_elements(By.XPATH, "//*[contains(text(), 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS' )]")
        select[1].click()

    else: 
        print('falhou')

    sleep(10)

    buton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]')


    for x in range (10):
        if buton.get_attribute != 'disabled' :
            buton.click()
        else: 
            sleep(100)
            x = x - 1

    select = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div')
    select.click()

    for x in range (2):
        if buton.get_attribute != 'disabled' :
            buton.click()
        else: 
            sleep(100)
            x = x - 1

    select = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]')

    for x in range(5):
        if buton.get_attribute != 'disabled' :
            buton.click()
        else: 
            sleep(100)
            x = x - 1

    '''
    select = driver.find_element(By.CSS_SELECTOR, ' #main > div > div')


    //*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]

    
    css selector

    # path do inicio da lista

    //*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]

    
    '''


        # se o botão disable espere
        #volte pra primeira
        #avance 2
        #volte 5
    
    
