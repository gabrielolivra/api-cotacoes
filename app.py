from functions import resultados, calcular_valor
print('Tabela de cotações\n')
print('[1] - USD-BRL \n[2] - EUR-BRL \n[3] - BTC-BRL\n')
cotacao = int(input('Digite o numero da cotação que deseja consultar? '))
print('')
resultados(cotacao)
calcular_moeda = input('Deseja calcular o preço da sua moeda? (S/N) ')
if calcular_moeda == 's':
    valor_calc = int(input("Digite o valor que deseja calcular: "))
    calcular_valor(valor_calc, resultados(cotacao))
else:
    pass