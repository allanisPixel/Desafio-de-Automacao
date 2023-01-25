from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Varivael i muda o comportamento do teste
# (Se 1 é a 1º playlist, se 1 é a 2º Playlist)

lista1 = 'This is 2Pac'
lista3 = 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS'

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(
    service=service,
)


for i in range(1): #2
    email = "alanisisabelle@gmail.com"
    senha = "azaleia987654123"

    #acessando site
    #driver = webdriver.Chrome()
    driver.get('https://open.spotify.com/')
    
    sleep(3)

    # Log-in
    enter = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
    enter.click()

    sleep(10)
    
    login = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")
    login.click
    (login).send_keys(email)
    login.click
    (password).send_keys(senha)

    #checkbox = driver.find_element(By.ID, "login-remember")
    checkbox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/label/span[1]")
    checkbox.click()

    sleep(15)

    #enter1 = driver.find_element(By.ID, "login-button")
    enter = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    enter.click()
    
    ##
    sleep(15)

    # Realizando busca

    busca = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input')

    sleep(10)

    i = {

        0: (busca).send_keys(lista1),
        1: (busca).send_keys(lista3),

    }
    busca.submit

    select = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/div/div/div/div[1]/div/a[4]')
    select.click()
 
    sleep(10)

    select = driver.find_element(By.XPATH, "//*[contains(text(), lista1 )]")
    select.click()
    sleep(90)

    if i == 0:
        select = driver.find_element(By.XPATH, "//*[contains(text(), 'This is 2Pac' )]")
        select.click()
        

    elif i == 1:
        select = driver.find_element(By.XPATH, "//*[contains(text(), 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS' )]")
        select.click()


    else: 
        print('falhou')

    sleep(90)
    #
    
    
