from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import _find_elements
from selenium.common.exceptions import *
import openpyxl
import smtplib
import pylint
import os
from email.message import EmailMessage
import re
import time
from time import sleep


#input para especificar ticket da ação que deseja avaliar

acao = input('Digite o Ticket (Ex.: PETR3) da Ação que deseja analizar: ')

browser = webdriver.Chrome(ChromeDriverManager().install())

print('Analisando ação', acao)

try:
    browser.get('https://statusinvest.com.br/acoes/'+acao)
    #tenta pegar o P/L da ação
    try:
        pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').text
        print('P/L da Ação', acao, 'é', pl,'.')
    except NoSuchElementException:
        print('Não foi possível obter o P/L da ação', acao)
except NoSuchElementException:
    print('Não foi possível encontrar essa ação. Tem certeza que digitou o Ticket corretamente?')