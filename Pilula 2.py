import random
cotacao = float(input('Cotação atual do dolar: '))
variaçao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1+variaçao)
print(f'variacao simulada: {variaçao:.3%}')
print(f'nova cotacao: {nova_cotacao:.2f}')