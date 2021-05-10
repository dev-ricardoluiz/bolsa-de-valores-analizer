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
browser = webdriver.Chrome(ChromeDriverManager().install())

#Array com todas as ações para avaliar
acao = ["LWSA3", "CSNA3", "ITSA4", "BBSE3", "SQIA3", "PETR3", "PETR4"]

total = len(acao)
posicao = 0

for c in range (0, total):
    browser.get('https://statusinvest.com.br/acoes/'+acao[posicao])
    print('Ação', acao[posicao])
    #pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').value
    #pl = ('Oi')
    #post.xpath(".//div[@class='list-view-item-date']/descendant-or-self::*/text()")[1])
    pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').text
    print('P/L da Ação', acao[posicao], 'é', pl)
    posicao = posicao + 1
    time.sleep(5)