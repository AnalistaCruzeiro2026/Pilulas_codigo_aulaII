def simular_crescimento(populacao, taxa, limite):
    anos = 0
    while populacao < limite:
        populacao += populacao * taxa
        anos += 1
    return anos

# main
p = float(input('Populacao inicial: '))
t = float(input('Taxa (%): ')) / 100
i = float(input('Limite: '))

resultado = simular_crescimento(p, t, i)
print(f'Anos = {resultado}')