menu = """ Bem Vindo
[1] depositar
[2] sacar
[3] extrato
[4] sair


"""

saldo = 0
limite = 500
extrado = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        valor = float(input("Valor a ser depositado: R$"))

        if valor >= 0:
            saldo += valor
            print("Saldo atual: R${}".format(saldo))

        else:
         print("O valor informado é invalido.")

    
    elif opcao == "2":
        valor = float(input("Valor do saque: R$"))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
           print("Operação falhou!Saldo insuficiente.")
        
        elif excedeu_limite or excedeu_saques:
            print("Limite de saques diários ou limite foi ultrapassado.")
        
        elif valor > 0:
            saldo -= valor
            extrado += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso!\n Novo Sald                  o: R${saldo:.2f}")
        else:
            print("O valor informado para o saque é inválido.")


    
    elif opcao == "3":
        print("\n ========= EXTRATO =========")
        print(extrado)
        print("Não foram realizadas movimentações" if not extrado else extrado)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================")

    elif opcao == "4":
      print ( "Obrigado por usar nosso sistema")
      break
    else:
       print ("Opção Inválida! Tente novamente.")
      

    
    
