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

ticker = input('Digite o Ticket (Ex.: PETR3) da Ação que deseja analizar: ')

browser = webdriver.Chrome(ChromeDriverManager().install())


try:
    browser.get('https://statusinvest.com.br/acoes/'+ticker)
    try:
        #DESCRIÇÃO DA AÇÃO
        acao = browser.find_element_by_xpath('//*[@id="main-header"]/div/div/div[1]/h1/small').text
        print('')
        print('Analisando ação', ticker, '-', acao)
        print('')

        #COTAÇÃO
        cotacao = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong').text
        print('Cotação:', cotacao)

        #P/L
        pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').text
        print('P/L:', pl)

        #D.Y.
        dy = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong').text
        print('Dividend Yield:', dy)

        #PEG RATIO
        #P/VP
        #EV/EBITDA
        #EV/EBIT
        #P/EBITDA
        #P/EBIT
        #VPA
        #P/ATIVO
        #LPA
        #P/SR
        #P/CAP.GIRO
        #P/ATIVO CIRCULANTE LÍQUIDO
        #
        #
        #

        #Após mostrar todos os indicadores da ação fazemos algumas análises
    except NoSuchElementException:
        print('Não foi possível obter os dados da ação', ticker)
except NoSuchElementException:
    print('Não foi possível encontrar essa ação. Tem certeza que digitou o Ticket corretamente?')