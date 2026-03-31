def calcular_media(prod, qual, pont):
    return (prod + qual + pont) / 3 

def classificar(media):
    if media >= 8:
        return 'Excelente'
    elif media >= 6:
        return 'Bom'
    else:
        return 'critico'
    
def avaliar_funcionario():
    total = 0 
    exc = 0 
    bom = 0 
    crit = 0 
    melhorNome = ''
    melhorMedia = -1
    while True:
        nome = input('Nome: ')
        if nome == 'fim':
            break
        prod = float(input('produtividade: '))
        qual = float(input('Qualidade: '))
        pont = float(input('Pontualidade: '))
        
        media = calcular_media(prod,qual,pont)
        categoria = classificar(media)
        print(f'{nome}, {media, {categoria}} ')
        
        total += 1
        if categoria == 'Excelente':
            exc += 1 
        elif categoria == 'Bom':
            bom += 1
    else:
         crit += 1
            
    if media > melhorMedia:
        melhorMedia = media 
        melhorNome = nome 
    if total == 0:
        print('nada para calcular')
        return
    print('-' * 50)
    print('relatorio')
    print('-' * 50)
    print(f'Total de func: {total}')
    print('Excelente: {exc}')
    print(f'bom: {bom}')
    print(f'Critico: {crit}')
    print(f'Melhor func: {melhorNome}')
    print(f'Melhor func média: {melhorMedia}')
        
avaliar_funcionario()