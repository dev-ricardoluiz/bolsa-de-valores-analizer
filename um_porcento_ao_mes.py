aporte = float(input('Quanto você pretende investir por mês? (Ex.: Se R$ 500,00 por mês, digite apenas `500`): '))
rentabilidade = float(input('Qual porcentage mensal você espera obter? (E.: Se 1 porcento ao mês, digite apenas `1`):'))
rentabilidade_mes = (rentabilidade + 100) / 100
duracao = int(input('Por quanto tempo você pretende investir? (Ex.: Se durante 1 ano, digite apenas `12`): '))
saldo = 0
mes = 1

for c in range (0, duracao):
    saldo = (saldo + aporte) * rentabilidade_mes
    print('No mês', mes, 'você terá: R$', saldo)
    mes = mes + 1
print('')
print('Ao final de', mes, 'meses (aproximadamente', mes/12, 'anos, investindo mensalmente R$', aporte, 'com uma rentabilidade média de', rentabilidade, '%' ' ao mês, você terá R$', saldo, 'em seu saldo. Seja um investidor!')

ações	cotação	qtd	qtd	total
wizs3	12,15	100	64	1992,6
beef3	9,49	200	10	1992,9
cebr3	192,33	0	11	2115,63
trpl4	26,19	0	76	1990,44
csmg3	17,48	100	15	2010,2
