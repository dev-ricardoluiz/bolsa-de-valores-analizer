# Instruções para rodar na vps em segundo plano deve ser usado o seguinte comando:
# para js -> nohup nodejs nome_do_arquivo.js &
# para py -> nohup python3 nome_do_arquivo.py &
# _________________________________________________________________________________

# Importa as bibliotecas necessárias
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

time.sleep(15)

# Configura o WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

time.sleep(10)

# Abre a página de login
browser.get('https://login.iqoption.com/pt/login')
login = 'iqricardoiq@gmail.com'
senha = 'Cdz221297*'

time.sleep(2)
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[1]').send_keys(login)
time.sleep(2)
#browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/div[2]').send_keys(senha)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/form/button').click()

time.sleep(15)
texto = browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div/div[2]/h1/span').text
print (texto)