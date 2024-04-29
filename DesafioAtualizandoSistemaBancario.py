menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuario
[5] Criar Conta
[6] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

while True:

    def criando_usuario(usuarios):
        cpf = input("Informe o numero do seu cpf somente números: ")
        usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        print(usuario_filtrado)
    
        if usuario_filtrado:
            print("CPF já cadastrado")
            
        else:
            nome = input("Informe o seu nome: ")
            nascimento = input("Informe a data de seu nascimento: ")
            logradouro = input("Informe o seu logradouro: ")
            numero = input("Informe o número de seu logradouro: ")
            bairro = input("Informe o seu Bairro:" )
            cidade = input("Informe a sua cidade:" )
            sigla = input("Informe a sigla do seu estado: ")
            usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "sigla": sigla})
            print(usuarios)
        return usuarios

    def deposito(deposito, saldo, extrato,/):

        deposito = float(input("Informe o valor do depósito:"))
        if deposito > 0:
            saldo += deposito
            print(f"O valor depositado foi de R${deposito:.2f}")
            print(f"Seu saldo atual é de R${saldo:.2f}")
            extrato += f"Depóstio de: R$ {deposito:.2f}\n"
        else:
            print("O valor precisa ser maior do que 0")
        return saldo, extrato

    def saque(*, saque, saldo, extrato, limite, numero_saques, limite_saques):

        saque = float(input("Informe o valor a ser sacado:"))
        if saque <= limite:
            if saque <= saldo:
                if saque >= 0  and numero_saques != limite_saques:
                    saldo -= saque
                    print(f"O valor sacado foi de R${saque:.2f}")
                    print(f"O saldo atual é de R${saldo:.2f}")
                    extrato += f"Saque de: R$ {saque:.2f}\n"
                    numero_saques = numero_saques + 1
                    print (numero_saques) 
                elif saque < 0 and numero_saques != limite_saques:
                    print("O valor precisa ser maior do que 0")
                elif saque >= 0 and numero_saques == limite_saques:
                    print("Você superou o limite de 3 saques por dia, por favor entrar em contato com a agência")
            else:
                print("Saldo insulficiente")
        else:
            print("O Valor do saque não pode ser maior do que R$500,00")
        return numero_saques, saldo, extrato


    def criar_conta(agencia, numero_conta, usuarios):
        cpf = input("Informe o CPF do usuário: ")
        usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        print(usuario_filtrado)

        if usuario_filtrado:
            print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def gerar_extrato(saldo, /, *, extrato):

        print("=====EXTRATO=====")
        print(extrato)
        print(f"Saldo:R$ {saldo:.2f}")
        print("=================")


    print("Bem Vindo! Por favor selecione uma opção!")

    opcao = input(menu)

    if opcao == "1":
        print("A opção escolida foi a de depósito" )
        saldo, extrato = deposito(deposito, saldo, extrato,)

    elif opcao == "2":
        print("A opção escolida foi a de saque")
        numero_saques, saldo, extrato = saque(saque=saque, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
    elif opcao == "3":
        gerar_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        usuarios = criando_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "6":
        print("Obrigado pela preferencia volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")