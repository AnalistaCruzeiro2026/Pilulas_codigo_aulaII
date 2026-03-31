def notasLiberadas(valor):
    for notas in (100,50,20,10):
        qtd = valor // notas
        valor = valor % notas
        if qtd > 0:
            print (f'{qtd} de notas de {notas}')

valor = int(input('Digite o valor: '))
notasLiberadas(valor)
