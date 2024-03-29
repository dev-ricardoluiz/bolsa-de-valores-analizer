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
ticker = ["AALR3", "ABCB4", "ABEV3", "ADHM3", "AERI3", "AESB3", "AFLT3", "AGRO3", "AHEB3", "AHEB5", "AHEB6", "ALLD3", "ALPA3", "ALPA4", "ALPK3", "ALSO3", "ALUP11", "ALUP3", "ALUP4", "AMAR3", "AMBP3", "ANIM3", "APER3", "APTI3", "APTI4", "ARZZ3", "ASAI3", "ATMP3", "ATOM3", "AURA33", "AVLL3", "AZEV3", "AZEV4", "AZUL4", "B3SA3", "BAHI3", "BALM3", "BALM4", "BAUH4", "BAZA3", "BBAS3", "BBDC3", "BBDC4", "BBML3", "BBRK3", "BBSE3", "BDLL3", "BDLL4", "BEEF3", "BEES3", "BEES4", "BFRE11", "BFRE12", "BGIP3", "BGIP4", "BIDI11", "BIDI3", "BIDI4", "BIOM3", "BKBR3", "BLAU3", "BMEB3", "BMEB4", "BMGB4", "BMIN3", "BMIN4", "BMKS3", "BMOB3", "BNBR3", "BOAS3", "BOBR3", "BOBR4", "BPAC11", "BPAC3", "BPAC5", "BPAN4", "BPAR3", "BPAT33", "BPHA3", "BRAP3", "BRAP4", "BRDT3", "BRFS3", "BRGE11", "BRGE12", "BRGE3", "BRGE5", "BRGE6", "BRGE7", "BRGE8", "BRIV3", "BRIV4", "BRKM3", "BRKM5", "BRKM6", "BRML3", "BRPR3", "BRQB3", "BRSR3", "BRSR5", "BRSR6", "BSEV3", "BSLI3", "BSLI4", "BTOW3", "BTTL3", "BTTL4", "CALI3", "CALI4", "CAMB3", "CAMB4", "CAML3", "CARD3", "CASH3", "CASN3", "CASN4", "CATA3", "CATA4", "CBEE3", "CCPR3", "CCRO3", "CCXC3", "CEAB3", "CEBR3", "CEBR5", "CEBR6", "CEDO3", "CEDO4", "CEEB3", "CEEB5", "CEEB6", "CEED3", "CEED4", "CEGR3", "CEPE3", "CEPE5", "CEPE6", "CESP3", "CESP5", "CESP6", "CGAS3", "CGAS5", "CGRA3", "CGRA4", "CIEL3", "CLSC3", "CLSC4", "CMIG3", "CMIG4", "CMIN3", "CMSA3", "CMSA4", "CNSY3", "COCE3", "COCE5", "COCE6", "COGN3", "CORR3", "CORR4", "CPFE3", "CPLE11", "CPLE3", "CPLE5", "CPLE6", "CPRE3", "CRDE3", "CREM3", "CRFB3", "CRIV3", "CRIV4", "CRPG3", "CRPG5", "CRPG6", "CSAB3", "CSAB4", "CSAN3", "CSED3", "CSMG3", "CSNA3", "CSRN3", "CSRN5", "CSRN6", "CTCA3", "CTKA3", "CTKA4", "CTNM3", "CTNM4", "CTSA3", "CTSA4", "CTSA8", "CURY3", "CVCB3", "CXSE3", "CYRE3", "DASA3", "DIRR3", "DMM03", "DMVF3", "DOHL3", "DOHL4", "DTCY3", "DTCY4", "DTEX3", "EALT3", "EALT4", "ECOR3", "ECPR3", "ECPR4", "EEEL3", "EEEL4", "EGIE3", "EKTR3", "EKTR4", "ELEK3", "ELEK4", "ELET3", "ELET5", "ELET6", "ELMD3", "ELPL3", "EMAE3", "EMAE4", "EMBR3", "ENAT3", "ENBR3", "ENEV3", "ENGI11", "ENGI3", "ENGI4", "ENJU3", "ENMA3B", "ENMA6B", "ENMT3", "ENMT4", "EQPA3", "EQPA5", "EQPA6", "EQPA7", "EQTL3", "ESPA3", "ESTR3", "ESTR4", "ETER3", "EUCAD3", "EUCAD4", "EVEN3", "EZTC3", "FBMC3", "FBMC4", "FESA3", "FESA4", "FHER3", "FIGE3", "FIGE4", "FLEX3", "FLRY3", "FNCN3", "FRAS3", "FRIO3", "FRAT3", "FTRT3B", "GBIO33", "GEPA3", "GEPA4", "GFSA3", "GGBR3", "GGBR4", "GGPS3", "GMAT3", "GNDI3", "GOAU3", "GOAU4", "GOLL4", "GPAR3", "GPCP3", "GPCP4", "GPIV33", "GRND3", "GSHP3", "GUAR3", "HAGA3", "HAGA4", "HAPV3", "HBOR3", "HBRE3", "HBSA3", "HBTS5", "HETA3", "HETA4", "HGTX3", "HOOT3", "HOOT4", "HYPE3", "IDVL3", "IDVL4", "IFCM3", "IGBR3", "IGSN3", "IGTA3", "INEP3", "INEP4", "INNT3", "IRBR3", "ITEC3", "ITSA3", "ITSA4", "ITUB3", "ITUB4", "JALL3", "JBDU3", "JBDU4", "JBSS3", "JFEN3", "JHSF3", "JOPA3", "JOPA4", "JPSA3", "JSLG3", "KEPL3", "KLBN11", "KLBN3", "KLBN4", "LAME3", "LAME4", "LAVV3", "LCAM3", "LEVE3", "LHER3", "LHER4", "LIGT3", "LINX3", "LIPR3", "LJQQ3", "LLIS3", "LOGG3", "LOGN3", "LPSB3", "LREN3", "LTEL3B", "LUPA3", "LUXM3", "LUXM4", "LWSA3", "MAPT3", "MAPT4", "MATD3", "MBLY3", "MDIA3", "MDNE3", "MEAL3", "MELK3", "MERC3", "MERC4", "MGEL3", "MGEL4", "MGLU3", "MILS3", "MMXM3", "MNDL3", "MNPR3", "MOAR3", "MODL11", "MODL3", "MODL4", "MOSI3", "MOVI3", "MRFG3", "MRSA3B", "MRSA5B", "MRSA6B", "MRVE3", "MSPA3", "MSPA4", "MSRO3", "MTIG3", "MTIG4", "MTRE3", "MTSA3", "MTSA4", "MULT3", "MWET3", "MWET4", "MYPK3", "NAFG3", "NAFG4", "NEMO3", "NEMO5", "NEMO6", "NEOE3", "NGRD3", "NINJ3", "NORD3", "NRTQ3", "NTCO3", "NUTR3", "ODER4", "ODPV3", "OFSA3", "OGXP3", "OIBR3", "OIBR4", "OMGE3", "OPCT3", "ORVR3", "OSXB3", "PARD3", "PATI3", "PATI4", "PCAR3", "PCAR4", "PDGR3", "PDTC3", "PEAB3", "PEAB4", "PETR3", "PETR4", "PETZ3", "PFRM3", "PGMN3", "PINE3", "PINE4", "PLAS3", "PLPL3", "PMAN3", "PNVL3", "PNVL4", "POMO3", "POMO4", "POSI3", "POWE3", "PPAR3", "PPLA11", "PRIO3", "PRNR3", "PSSA3", "PTBL3", "PTCA11", "PTCA3", "PTNT3", "PTNT4", "QUAL3", "QUSW3", "QVQP3B", "RADL3", "RAIL3", "RANI3", "RANI4", "RAPT3", "RAPT4", "RCSL3", "RCSL4", "RDNI3", "RDOR3", "RECV3", "REDE3", "RENT3", "RLOG3", "RNEW11", "RNEW3", "RNEW4", "ROMI3", "RPAD3", "RPAD5", "RPAD6", "RPMG3", "RRRP3", "RSID3", "RSUL3", "RSUL4", "SANB11", "SANB3", "SANB4", "SAPR11", "SAPR3", "SAPR4", "SBFG3", "SBSP3", "SCAR3", "SEDU3", "SEER3", "SEQL3", "SGPS3", "SHOW3", "SHUL3", "SHUL4", "SIMH3", "SLCE3", "SLED3", "SLED4", "SMFT3", "SMLS3", "SMTO3", "SNSY3", "SNSY5", "SNSY6", "SOJA3", "SOMA3", "SOND3", "SOND5", "SOND6", "SPRT3B", "SQIA3", "STBP3", "STKF3", "STTR3", "SULA11", "SULA3", "SULA4", "SUZB3", "TAEE11", "TAEE3", "TAEE4", "TASA3", "TASA4", "TCNO3", "TCNO4", "TCSA3", "TECN3", "TEKA3", "TEKA4", "TELB3", "TELB4", "TEND3", "TESA3", "TFCO4", "TGMA3", "TIET11", "TIET3", "TIET4", "TIMS3", "TKNO3", "TKNO4", "TOTS3", "TOYB3", "TOBY4", "TPIS3", "TRIS3", "TRPL3", "TRPL4", "TUPY3", "TXRX3", "TXRX4", "UCAS3", "UGPA3", "UNIP3", "UNIP5", "UNIPE6", "USIM3", "USIM5", "USIM6", "VALE3", "VAMO3", "VIVA3", "VIVR3", "VIVT3", "VIVT4", "VLID3", "VSPT3", "VSPT4", "VULC3", "VVAR3", "WEGE3", "WEST3", "WHRL3", "WHRL4", "WIZS3", "WLMM3", "WLMM4", "WSON33", "YDUQ3"]

total = len(ticker)
posicao = 0

# array com todas as ações que queira avaliar
#ticker = ["LWSA3", "CSNA3", "PETR4"]

browser = webdriver.Chrome(ChromeDriverManager().install())

for c in range (0, total):
    try:
        browser.get('https://statusinvest.com.br/acoes/'+ticker[posicao])
        try:
            #DESCRIÇÃO DA AÇÃO
            acao = browser.find_element_by_xpath('//*[@id="main-header"]/div/div/div[1]/h1/small').text
            print('____________________________________________________________________')
            print('Analisando ação', ticker[posicao], '-', acao)
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
    posicao = posicao + 1