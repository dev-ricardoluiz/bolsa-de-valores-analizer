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

# array com todos os ativos
ticker = ["BRIP11", "CVBI11", "HCTR11", "KEVE11", "KISU11", "LVBI11", "MALL11", "MGHT11", "HGCR11", "HTMX11", "FEXC11", "FIGS11", "FIIB11", "FLCR11", "FLMA11", "FPAB11", "FVPQ11", "GALG11", "GTWR11", "HAAA11", "MORE11", "BRCR11", "BRHT11B","CTXT11", "JRDM11", "MGCR11", "PATB11", "RBBV11", "TEPP11", "CXCO11", "ORPD11", "OUFF11", "FATN11", "FCFL11", "MVFI11", "NAVT11", "NCHB11", "PQDP11", "BICR11", "BLMG11", "BLMR11", "BRCO11", "RBED11", "RBFF11", "RBGS11", "RBHY11", "RBIR11","RBRR11", "RBRS11", "BTAL11", "BTCR11", "CJFI11", "CNES11", "BTSG11", "CXRI11", "FLRP11", "FMOF11", "FOFT11", "PQAG11","HBTT11", "HCRI11", "HCST11", "HMOC11", "HOSI11", "HREC11", "HSLG11", "HSRE11", "BPFF11", "BPML11", "BTWR11", "BZEL11", "CEOC11", "CJCT11", "CXCE11B", "ELDO11B", "JFLL11", "FISD11", "CPTS11", "MTOF11", "ONEF11", "RBRY11", "RCRB11", "RECX11","DAMT11B", "DEVA11", "DLMT11", "HBRH11", "LUGG11", "FINF11", "GCRI11", "GESE11B", "GGRC11", "GSFI11", "ERCR11", "OUJP11", "OULG11", "REIT11", "RELG11", "MGLG11", "PORD11", "PRTS11", "RCRI11B", "RMAI11", "RRCI11", "SEQR11", "TRNT11", "SBCL11", "TBOF11", "TCIN11", "VISC11", "MOFF11", "TFOF11", "TGAR11", "TORD11", "VTPL11", "RBCB11", "SOLR11", "AIEC11", "ALZR11", "ANCR11B", "AQLL11", "ATWN11", "CORM11", "HBCR11", "MINT11", "PATL11", "HGIC11", "RBLG11", "RBRM11", "SALI11", "BBFO11", "BBPO11", "BBRC11", "BRLA11", "BLMC11", "AFCR11", "AFHI11", "AFOF11", "BCFF11", "BCIA11", "BCRI11", "BICE11", "BREV11", "HCHG11", "CARE11", "HFOF11", "HGBS11", "DMAC11", "DOMC11", "EGYR11", "ESTQ11", "EVBI11", "FAED11", "FAMB11B", "HUSC11", "HUSI11", "IBFF11", "IFID11", "IFIE11", "JBFO11", "KNIP11", "KNSC11", "LKDV11", "LOFT11B", "LSPA11", "PEMA11", "ROOF11", "PLOG11", "PNDL11", "PNPR11", "RSPD11", "RVBI11", "RZAK11", "SHDP11B", "SJAU11", "RDPD11", "RECR11", "RECT11", "URPR11", "VERE11", "VGHF11", "VGIP11", "VGIR11", "VIDS11", "VIFI11", "VINO11", "VSHO11", "VSLH11", "VTPA11", "VTRT11", "VTVI11", "VTXI11", "VVPR11", "VXXV11", "WPLZ11", "YUFI11", "ZIFI11", "TSER11", "VILG11", "STRX11", "HPDP11", "HRDF11", "HSAF11", "HSML11", "IRDM11", "RBCO11", "RBDS11", "ARCT11", "ATCR11", "BBFI11B", "BBIM11", "DOVL11B", "FISC11", "HGLG11", "HGPO11", "HGRE11", "LATR11B", "PABY11", "PATC11", "PVBI11", "QAGR11", "QIFF11", "SPVJ11", "VSEC11", "VTLT11", "BMII11", "BVAR11", "LFTT11", "MAXR11", "MBRF11", "MCCI11", "RZTR11", "VOTS11", "VRTA11", "XPCI11", "XPCM11", "XPHT11", "CXTL11", "FCAS11", "RFOF11", "RNDP11", "SADI11", "SAIC11B", "BLCP11", "BTLG11", "HGFF1", "HGRU11", "HLOG11", "LASC11", "LGCP11", "RBIV11", "RBRD11", "RBRF11", "RBRL11", "RBRP11", "SHOP11", "VLJS11", "VLOL11", "WTSP11B", "CBOP11", "FPNG11", "PBLV11", "SARE11", "ARFI11B", "BZLI11", "KINP11", "KNCR11", "KNHY11", "MFAI11", "MFII11", "MGFF11", "NVHO11", "NVIF11B", "SFND11", "SHPH11", "SPAF11", "TRXB11", "TRXF11", "TSNC11", "MXRF11", "TOUR11", "ATSA11", "KNRI11", "SPTW11", "EDGA11", "FIIP11B", "FIVN11", "BMLC11", "BNFS11", "RCFF11", "TCPF11", "EDFO11B", "GRLV11", "PLRI11", "ABCP11", "JPPA11", "JPPC11", "KNRE11", "OURE11", "PLCR11", "ARRI11", "BARI11", "DRIT11B", "FTCE11B", "FVBI11", "GCFF11", "BRIM11", "HABT11", "CFHI11", "ERPA11", "PRSN11B", "PRSV11", "SCPF11", "SDIL11", "BPRP11", "RNGO11", "THRA11", "TORM13", "VCJR11", "CRFF11", "EURO11", "BLMO11", "JSRE11", "JTPR11", "KFOF11", "NEWL11", "NEWU11", "NPAR11", "NSLU11", "RBTS11", "RBVA11", "RBVO11", "RCFA11", "ALMI11", "CPFF11", "VPSI11", "XPHT12", "XPIN11", "XPLG11", "XPML11", "XPPR11", "XPSF11", "XTED11"]

total = len(ticker)
posicao = 0

browser = webdriver.Chrome(ChromeDriverManager().install())

for c in range (0, total):
    try:
        browser.get('https://statusinvest.com.br/fundos-imobiliarios/'+ticker[posicao])
        try:
            #DESCRIÇÃO DO FII
            fii = browser.find_element_by_xpath('//*[@id="main-header"]/div/div/div[1]/h1/small').text
            print('____________________________________________________________________')
            print('Analisando FII', ticker[posicao], '-', fii)
            print('')

            #COTAÇÃO
            cotacao = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[1]/strong').text
            print('Cotação:', cotacao)

            #MÍNIMA DO MÊS
            min_mes = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[2]/div/div[2]/div/span[2]').text
            print('Mín. Mês:', min_mes)

            #MÍNIMA DO ANO (52 SEMANAS)
            min_ano = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[2]/div/div[1]/strong').text
            print('Mín. Ano:', min_ano)

            #MÁXIMA DO MÊS
            max_mes = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[3]/div/div[2]/div/span[2]').text
            print('Máx. Mês:', max_mes)

            #MÁXIMA DO ANO (52 SEMANAS)
            max_ano = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[3]/div/div[1]/strong').text
            print('Máx. Ano', max_ano)

            #VALORIZAÇÃO 12 ANUAL (12 SEMANAS)
            valorizacao_anual = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[5]/div/div[1]/strong').text
            print('Valorização 12 Meses:', valorizacao_anual)

            #VALORIZAÇÃO MENSAL
            valorizacao_mensal = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[5]/div/div[2]/div/span[2]/b').text
            print('Valorização Último Mês:', valorizacao_mensal)

            ############
            #INDICADORES
            ############
            print('')
        
            #D.Y.
            dy = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[1]/div[4]/div/div[1]/strong').text
            print('DIVIDEND YIELD:', dy)

            #VALOR PATRIM. P/COTA
            vp_p_c = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[1]/div/div[1]/strong').text
            print('VALOR PATRIM. P/COTA:', vp_p_c)

            #P/VP
            pv_p = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[2]/div/div[1]/strong').text
            print('P/VP:', pv_p)

            #VALOR EM CAIXA
            val_caixa = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[3]/div/div[1]/strong').text
            print('VALOR EM CAIXA:', val_caixa)

            #DY CAGR
            dy_cagr = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[4]/div/div[1]/strong').text
            print('DY CAGR:', dy_cagr)

            #VALOR CAGR
            val_cagr = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[5]/div/div[1]/strong').text
            print('VALOR CAGR:', val_cagr)

            #NÚMERO DE COTISTAS
            num_cotistas = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[6]/div/div[1]/strong').text
            print('NÚMERO DE COTISTAS:', num_cotistas)

            #NÚMERO DE COTAS
            num_cotas = browser.find_element_by_xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[6]/div/div[2]/span[2]').text
            print('NÚMERO DE COTAS:', num_cotas)

            #PRAZO DE DURAÇÃO
            prazo = browser.find_element_by_xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[4]/div/div/div/strong').text
            print('PRAZO DE DURAÇÃO:', prazo)

            #SEGMENTO
            segmento = browser.find_element_by_xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[6]/div/div/strong').text
            print('SEGMENTO:', segmento)

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
            print('Não foi possível obter os dados do FII', ticker[posicao])
            print('____________________________________________________________________________________')
    except NoSuchElementException:
        print('____________________________________________________________________________________')
        print('Não foi possível encontrar esse FII. Tem certeza que digitou o Ticket corretamente?')
        print('____________________________________________________________________________________')
    posicao = posicao + 1