while True: #mantem o código funcionando infinitamente.
    valor=int(input("Digite o valor 1 ou 0 para encerrar: ")) #Lê o valor.
    if valor==1: #Caso o valor digitado seja 1.
        print("Valor Correto.")
    else: #Qualquer outro numero digitado.
        print("Valor para sair.")
        break