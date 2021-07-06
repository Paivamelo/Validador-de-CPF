

while True:
    cpf = input("Digite seu cpf: ")
    novo_cpf = cpf[:-2] 
    contador = 10
    soma = 0    
    for i in range(19):
        if i > 8:
            i -=9

        soma += int(novo_cpf[i]) * contador


        contador -= 1
        if contador < 2:
            contador = 11
            digito = 11 - (soma % 11)

            if digito >= 9:
                digito = 0
            soma = 0
            novo_cpf += str(digito)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)




    if cpf == novo_cpf and not sequencia:
        print("Seu CPF é válido")
    else:
        print("CPF inválido")
    
