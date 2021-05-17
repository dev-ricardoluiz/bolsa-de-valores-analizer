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

# input para especificar ticket da ação que deseja avaliar
ticker = input('Digite o Ticket (Ex.: PETR3) da Ação que deseja analizar: ')

browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    browser.get('https://statusinvest.com.br/acoes/'+ticker) 
    try:
        #DESCRIÇÃO DA AÇÃO
        acao = browser.find_element_by_xpath('//*[@id="main-header"]/div/div/div[1]/h1/small').text
        print('____________________________________________________________________')
        print('Analisando ação', ticker, '-', acao) 
        print('')

        #COTAÇÃO
        cotacao = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong').text
        print('Cotação:', cotacao)

        #MÍNIMA DO MÊS
        min_mes = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/span[2]').text
        print('Mín. Mês:', min_mes)

        #MÍNIMA DO ANO (52 SEMANAS)
        min_ano = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[2]/div/div[1]/strong').text
        print('Mín. Ano:', min_ano)

        #MÁXIMA DO MÊS
        max_mes = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/span[2]').text
        print('Máx. Mês:', max_mes)

        #MÁXIMA DO ANO (52 SEMANAS)
        max_ano = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[3]/div/div[1]/strong').text
        print('Máx. Ano', max_ano)

        #VALORIZAÇÃO 12 ANUAL (12 SEMANAS)
        valorizacao_anual = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[5]/div/div[1]/strong').text
        print('Valorização 12 Meses:', valorizacao_anual)

        #VALORIZAÇÃO MENSAL
        valorizacao_mensal = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div/div[1]/div/div[5]/div/div[2]/div/span[2]/b').text
        print('Valorização Último Mês:', valorizacao_mensal)

        #########################
        #INDICADORES DE VALUATION
        #########################
        print('')
        
        #P/L
        pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').text
        print('P/L:', pl)

        #D.Y.
        dy = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong').text
        print('DIVIDEND YIELD:', dy)

        #PEG RATIO
        peg_ratio = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[3]/div/div/strong').text
        print('PEG RATIO:', peg_ratio)

        #P/VP
        p_vp = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[4]/div/div/strong').text
        print('P/VP:', p_vp)

        #EV/EBITDA
        ev_ebitda = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[5]/div/div/strong').text
        print('EV/EBITDA:', ev_ebitda)

        #EV/EBIT
        ev_ebit = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[6]/div/div/strong').text
        print('EV/EBIT:', ev_ebit)

        #P/EBITDA
        p_ebitda = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[7]/div/div/strong').text
        print('P/EBITDA:', p_ebitda)

        #P/EBIT
        p_ebit = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[8]/div/div/strong').text
        print('P/EBIT:', p_ebit)

        #VPA
        vpa = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong').text
        print('VPA:', vpa)

        #P/ATIVO
        p_ativo = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[10]/div/div/strong').text
        print('P/ATIVO:', p_ativo)

        #LPA
        lpa = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[11]/div/div/strong').text
        print('LPA:', lpa)

        #P/SR
        p_sr = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[12]/div/div/strong').text
        print('P/SR:', p_sr)

        #P/CAP.GIRO
        p_cap_giro = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[13]/div/div/strong').text
        print('P/CAP. GIRO:', p_cap_giro)

        #P/ATIVO CIRCULANTE LÍQUIDO
        p_ativo_circ_liq = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[14]/div/div/strong').text
        print('P/ATIVO CIRCULANTE LÍQUIDO:', p_ativo_circ_liq)

        #############################
        #INDICADORES DE ENDIVIDAMENTO
        #############################
        print('')

        #DÍVIDA LÍQUIDA/PL
        divida_liq_pl = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[1]/div/div/strong').text
        print('DÍVIDA LÍQUIDA:', divida_liq_pl)

        #DÍVIDA LÍQUIDA/EBITDA
        divida_liq_ebitda = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[2]/div/div/strong').text
        print('DÍVIDA LÍQUIDA/EBITDA:', divida_liq_ebitda)

        #DÍVIDA LÍQUIDA/EBIT
        divida_liq_ebit = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[3]/div/div/strong').text
        print('DÍVIDA LÍQUIDA/EBIT:', divida_liq_ebit)

        #PL/ATIVOS
        pl_ativos = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[4]/div/div/strong').text
        print('PL/ATIVOS:', pl_ativos)

        #PASSIVOS/ATIVOS
        passivos_ativos = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[5]/div/div/strong').text
        print('PASSIVOS/ATIVOS:', passivos_ativos)

        #LIQ RECORRENTE
        liq_recorrente = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[6]/div/div/strong').text
        print('LIQUIDEZ RECORRENTE:', liq_recorrente)

        ##########################
        #INDICADORES DE EFICIÊNCIA
        ##########################
        print('')

        #MARGEM BRUTA
        margem_bruta =  browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[1]/div/div/strong').text
        print('MARGEM BRUTA:', margem_bruta)

        #MARGEM EBITDA
        margem_ebitda = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[2]/div/div/strong').text
        print('MARGEM EBITDA:', margem_ebitda)

        #MARGEM EBIT
        margem_ebit = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[3]/div/div/strong').text
        print('MARGEM EBIT:', margem_ebit)

        #MARGEM LÍQUIDA
        margem_liquida = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div/div/strong').text
        print('MARGEM LÍQUIDA:', margem_liquida)

        #############################
        #INDICADORES DE RENTABILIDADE
        #############################
        print('')
        
        #ROE
        roe =  browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[1]/div/div/strong').text
        print('ROE:', roe)

        #ROA
        roa = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[2]/div/div/strong').text
        print('ROA:', roa)

        #ROIC
        roic = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[3]/div/div/strong').text
        print('ROIC:', roic)

        #GIRO ATIVOS
        giro_ativos = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[4]/div/div/strong').text
        print('GIRO ATIVOS:', giro_ativos)

        ##########################
        #INICADORES DE CRESCIMENTO
        ##########################
        print('')

        #CAGR RECEITAS 5 ANOS
        cagr_receitas = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[1]/div/div/strong').text
        print('CAGR RECEITAS (5 ANOS):', cagr_receitas)

        #CAGR LUCRO 5 ANOS
        cagr_lucros = browser.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[2]/div/div/strong').text
        print('CAGR LUCROS (5 ANOS):', cagr_lucros)

        # Após mostrar todos os indicadores da ação fazemos algumas análises

        # Enquanto menor o P/L MELHOR
        # Enquanto maior o ROE MELHOR

        # Classificar por notas os maiores ROE's
        # Classificar por notas os menores P/L's
        # Somar notas dos ROE's e P/L's
        # Por em ordem decrescente as empresas com base em suas notas

        print('')
    except NoSuchElementException:
        print('____________________________________________________________________________________')
        print('Não foi possível obter os dados da ação', ticker[posicao])
        print('____________________________________________________________________________________')
except NoSuchElementException:
    print('____________________________________________________________________________________')
    print('Não foi possível encontrar essa ação. Tem certeza que digitou o Ticket corretamente?')
    print('____________________________________________________________________________________')