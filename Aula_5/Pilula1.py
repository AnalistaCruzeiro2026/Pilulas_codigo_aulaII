def Validarsenha(senha):
    if len(senha) <8:
        return 'senha invalida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    
    for c in senha:
        if c == ' ': 
            return 'senha Invalida,  não pode conter espaços'   
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
    
    
    if not temNumero:
        return 'senha Invalida, não tem numero'
    if not temMaiuscula:
        return 'senha invalida, não contem letra Maiuscula'
    return 'senha valida'


#main
senha = input('Digite sua senha:')
print(Validarsenha(senha))
