import requests

def cotacoes(valor):
    if valor == 1:
        return 'USD-BRL'
    elif valor == 2:
        return 'EUR-BRL'
    elif valor == 3:
        return 'BTC-BRL'
    else:
        return 0

def resultados(cotacao):
    code = cotacoes(cotacao)
    resultado =  requests.get(f'https://economia.awesomeapi.com.br/json/last/{code}')
    if resultado.status_code == 200:
        resultado_json = resultado.json()
        code = code.replace('-', '')
        codigo = resultado_json[code]['code']
        name = resultado_json[code]['name']
        high = resultado_json[code]['high']
        low = resultado_json[code]['low']
        create_date = resultado_json[code]['create_date']
        print('Codigo: {}'.format(codigo))
        print('Nome: {}'.format(name))
        print('Maior cotação: {}'.format(high))
        print('Menor cotação: {}'.format(low))
        print('Data de atualização: {}\n'.format(create_date))
        return high, low
    else:
        print('Fora de escopo')

def calcular_valor(valor, moeda):
    resultado_maior = valor * float(moeda[0])
    resultado_menor = valor * float(moeda[1])
    print('Maior valor: {:.2f}'.format(resultado_maior))
    print('Menor valor: {:.2f}'.format(resultado_menor))