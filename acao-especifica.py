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

        #########################
        #INDICADORES DE VALUATION
        #########################
        
        #P/L
        pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').text
        print('P/L:', pl)

        #D.Y.
        dy = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong').text
        print('Dividend Yield:', dy)

        #PEG RATIO
        peg_ratio = browser.find_element_by_xpath('').text
        print(peg_ratio)

        #P/VP
        p_vp = browser.find_element_by_xpath('').text
        print(p_vp)

        #EV/EBITDA
        ev_ebitda = browser.find_element_by_xpath('').text
        print(ev_ebitda)

        #EV/EBIT
        ev_ebit = browser.find_element_by_xpath('').text
        print(ev_ebit)

        #P/EBITDA
        p_ebitda = browser.find_element_by_xpath('').text
        print(p_ebitda)

        #P/EBIT
        p_ebit = browser.find_element_by_xpath('').text
        print(p_ebit)

        #VPA
        vpa = browser.find_element_by_xpath('').text
        print(vpa)

        #P/ATIVO
        p_ativo = browser.find_element_by_xpath('').text
        print(p_ativo)

        #LPA
        lpa = browser.find_element_by_xpath('').text
        print(lpa)

        #P/SR
        p_sr = browser.find_element_by_xpath('').text
        print(p_sr)

        #P/CAP.GIRO
        p_cap_giro = browser.find_element_by_xpath('').text
        print(p_cap_giro)

        #P/ATIVO CIRCULANTE LÍQUIDO
        p_ativo_circ_liq = browser.find_element_by_xpath('').text
        print(p_ativo_circ_liq)

        #############################
        #INDICADORES DE ENDIVIDAMENTO
        #############################

        #DÍVIDA LÍQUIDA/PL
        divida_liq_pl = browser.find_element_by_xpath('').text
        print(divida_liq_pl)

        #DÍVIDA LÍQUIDA/EBITDA
        divida_liq_ebitda = browser.find_element_by_xpath('').text
        print(divida_liq_ebitda)

        #DÍVIDA LÍQUIDA/EBIT
        divida_liq_ebit = browser.find_element_by_xpath('').text
        print(divida_liq_ebit)

        #PL/ATIVOS
        pl_ativos = browser.find_element_by_xpath('').text
        print(pl_ativos)

        #PASSIVOS/ATIVOS
        passivos_ativos = browser.find_element_by_xpath('').text
        print(passivos_ativos)

        #LIQ RECORRENTE
        liq_recorrente = browser.find_element_by_xpath('').text
        print(liq_recorrente)

        ##########################
        #INDICADORES DE EFICIÊNCIA
        ##########################

        #MARGEM BRUTA
        margem_bruta =  browser.find_element_by_xpath('').text
        print(margem_bruta)

        #MARGEM EBITDA
        margem_ebitda = browser.find_element_by_xpath('').text
        print(margem_ebitda)

        #MARGEM EBIT
        margem_ebit = browser.find_element_by_xpath('').text
        print(margem_ebit)

        #MARGEM LÍQUIDA
        margem_liquida = browser.find_element_by_xpath('').text
        print(margem_liquida)

        #############################
        #INDICADORES DE RENTABILIDADE
        #############################
        
        #ROE
        roe =  browser.find_element_by_xpath('').text
        print(roe)

        #ROA
        roa = browser.find_element_by_xpath('').text
        print(roa)

        #ROIC
        roic = browser.find_element_by_xpath('').text
        print(roic)

        #GIRO ATIVOS
        giro_ativos = browser.find_element_by_xpath('').text
        print(giro_ativos)

        ##########################
        #INICADORES DE CRESCIMENTO
        ##########################

        #CAGR RECEITAS 5 ANOS
        cagr = browser.find_element_by_xpath('').text
        print(cagr)

        #CAGR LUCRO 5 ANOS
        cagr_cinco_anos = browser.find_element_by_xpath('').text
        print(cagr_cinco_anos)



        #Após mostrar todos os indicadores da ação fazemos algumas análises


        
    except NoSuchElementException:
        print('Não foi possível obter os dados da ação', ticker)
except NoSuchElementException:
    print('Não foi possível encontrar essa ação. Tem certeza que digitou o Ticket corretamente?')