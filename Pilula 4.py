import statistics as St
lote1 = float(input('Produção lote 1 '))
lote2 = float(input('Produção lote 2 '))
lote3 = float(input('Produção lote 3 '))
media = St.mean( (lote1, lote2, lote3) )
desvio = St.mean( (lote1, lote2, lote3) )
print(f'Média {media:2f}')
print(f'desvio padrão {desvio:.2f}')