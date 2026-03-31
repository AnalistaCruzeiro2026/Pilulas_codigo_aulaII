import random
import datetime

def menu():
    nome_arquivo = 'log.txt'
    while True:
        print('\nMonitor LogPy')
        print('1 - Gerar logs')
        print('2 - Analisar Logs')
        print('3 - Gerar e analisar Logs')
        print('4 - Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            try:
                qnt = int(input('Quantidade de logs: '))
                gerar_arquivo(nome_arquivo, qnt)
            except ValueError:
                print('Quantidade incorreta')
        elif opcao == '2':
            print('Funcionalidade de análise não implementada.')
        elif opcao == '3':
            print('Funcionalidade não implementada.')
        elif opcao == '4':
            print('Até mais')
            break
        else:
            print('Opção errada')

def gerar_arquivo(nome_arq, qnd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qnd):
            log = montar_log(i)
            arq.write(log + '\n')
    print('Logs gerados com sucesso!')

def montar_log(i):
    data = gerar_data_hora(i)
    ip = "127.0.0.1"
    metodo = "GET"
    status = "200"
    recurso = "/index.html"
    tempo = random.randint(10, 500)
    agente = "Mozilla/5.0"
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 500mb - HTTP/1.1 - {agente} - /home'

def gerar_data_hora(i):
    base = datetime.datetime(2026, 3, 30, 22, 8, 0)
    delta = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + delta).strftime('%d/%m/%Y %H:%M:%S')


        