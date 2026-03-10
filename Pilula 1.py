import math
#leituras
assinantes = int(input('Digite a qtd de assinantes:'))
mensalidades = float(input('Digite o valor da mensalidade: '))
taxa = float(input('Digite a taxa de cressimento mensal %: '))/100
meses = int(input('Digite a qnt de meses de projeção: '))
#processamentos
assinantes_finais = assinantes * math.pow((1+ taxa) , meses)
receita_final = assinantes_finais * mensalidades
#saída
print(f'Assinantes estimados: {assinantes_finais:0f}')
print(f'Receita estimada: R$ {receita_final: 2f}')