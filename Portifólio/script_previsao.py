import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

cidades = ['Niterói rj', 'São Gonçalo rj', 'Magé rj', 'Penha rj', 'São João da Barra rj']
driver = webdriver.Chrome()
dict_cidade = {}
for cidade in cidades:
    google = driver.get('https://www.google.com/')
    time.sleep(0.5)
    barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    time.sleep(0.5)
    barra_pesquisa.send_keys(fr'Tempo Em {cidade}')
    barra_pesquisa.send_keys(Keys.ENTER)
    element = driver.find_element(By.ID, 'wob_tm')
    element_chuva = driver.find_element(By.ID, 'wob_pp')
    chuva = element_chuva.text
    element_chuva = driver.find_element(By.ID, 'wob_ws')
    vento = element_chuva.text
    data = element.text
    dict_cidade[cidade] = [data, chuva, vento]
    print(fr'O tempo em {cidade} está em {data}°')
    print(fr'Porcentagem de chuva {chuva}')
    print(fr'Vento em {cidade} é {vento}')

    time.sleep(0.5)

df = pd.DataFrame(dict_cidade, index=['Temperatura', 'Chuva', 'Vento'])
excel = df.to_excel('tempo.xlsx', index=True)
print(df)
