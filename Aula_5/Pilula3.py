def verificarCrescimento():
  anterior = float(input('Leitura 1: '))
  crescente = True

  for i in range(4):
    atual = float(input(f'Leitura {i+2}: '))
    if atual < anterior:
      crescente = False
    anterior = atual # Atualiza para a próxima comparação
  
  return crescente

# main
if verificarCrescimento():
  print('crescimento')
else:
  print('Não crescimento')