menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("Bem Vindo! Por favor selecione uma opção!")

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        deposito = input()
        deposito = float(deposito)
        if deposito >= 0:
            saldo = saldo + deposito
            print(saldo)
            extrato = extrato + f"Depóstio de: R$ {deposito:.2f}\n"
        else:
            print("O valor precisa ser maior do que 0")

    elif opcao == "2":
        print("Saque")
        saque = input()
        saque = float(saque)
        if saque <= limite:
            if saque <= saldo:
                if saque >= 0  and numero_saques != LIMITE_SAQUES:
                    saldo = saldo - saque
                    print(saldo)
                    extrato = extrato + f"Saque de: R$ {saque:.2f}\n"
                    numero_saques = numero_saques + 1 
                elif saque < 0 and numero_saques != LIMITE_SAQUES:
                    print("O valor precisa ser maior do que 0")
                elif saque >= 0 and numero_saques == LIMITE_SAQUES:
                    print("Você superou o limite de 3 saques por dia, por favor entrar em contato com a agência")
            else:
                print("Saldo insulficiente")
        else:
            print("O Valor do saque não pode ser maior do que R$500,00")
    
    elif opcao == "3":
        print("=====EXTRATO=====")
        print(extrato)
        print("=================")

    elif opcao == "4":
        print("Obrigado pela preferencia volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
