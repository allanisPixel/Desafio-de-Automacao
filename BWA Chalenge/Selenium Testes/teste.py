from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Varivael i muda o comportamento do teste
# (Se 1 é a 1º playlist, se 1 é a 2º Playlist)

lista1 = 'This is 2Pac'
lista3 = 'ELETRÔNICAS 2022 ⚡ MAIS TOCADAS'

for i in range(2): #2
    email = "alanisisabelle@gmail.com"
    senha = "azaleia987654123"

    #acessando site
    driver = webdriver.Chrome()
    driver.get("https://open.spotify.com/")
    
    sleep(3)

    # Log-in
    enter = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
    enter.click()

    sleep(3)

    login = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")
    login.click
    (login).send_keys(email)
    login.click
    (password).send_keys(senha)

    enter1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/button')
    enter1.click
    

    sleep(10)
    #
    
    

