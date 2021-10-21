print ('')
aporte = float(input('Quanto você pretende investir por mês? (Ex.: Se R$ 500,00 por mês, digite apenas `500`): '))
rentabilidade = float(input('Qual porcentagem mensal você espera obter? (E.: Se 1 porcento ao mês, digite apenas `1`): '))
rentabilidade_mes = (rentabilidade + 100) / 100
duracao = int(input('Por quantos meses você pretende investir? (Ex.: Se durante 1 ano, digite apenas `12`): '))
saldo = 0
mes = 1

for c in range (0, duracao):
    saldo = (saldo + aporte) * rentabilidade_mes
    print('No mês', mes, 'você terá: R$', saldo)
    mes = mes + 1
print('')
print('Ao final de', mes-1, 'meses (aproximadamente', (mes-1)/12, 'anos) investindo mensalmente R$', aporte, 'com uma rentabilidade média de', rentabilidade, '%' ' ao mês, você terá R$', saldo, 'em seu saldo. Seja um investidor!')
print('')