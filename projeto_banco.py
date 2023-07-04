import random
import time

# Dicionário para armazenar as informações de usuário
usuarios = {}

# Dicionário para armazenar as informações das contas
contas = {}

# Dicionário para armazenar as informações dos extratos
extratos = {}

# Função para gerar um número de conta aleatório
def gerar_numero_conta():
    while True:
        numero_conta = str(random.randint(100000, 999999))
        if numero_conta not in contas:
            return numero_conta

# Função para criar uma nova conta
def criar_conta():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha desejada: ")

    numero_conta = gerar_numero_conta()
    contas[numero_conta] = {'nome': nome, 'senha': senha, 'saldo': 500, 'tipo': 'corrente'}

    print("Conta criada com sucesso!")
    print("Seu número de conta é:", numero_conta)

# Função para fazer login na conta
def realizar_login():
    numero_conta = input("Digite o número da conta ou nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica se o número da conta existe no dicionário de contas
    if numero_conta in contas:
        # Verifica se a senha está correta
        if contas[numero_conta]['senha'] == senha:
            print("Login bem-sucedido!")
            menu_bancario(numero_conta)
        else:
            print("Senha incorreta.")
    else:
        # Verifica se o nome de usuário existe no dicionário de contas
        for conta in contas.values():
            if conta['nome'] == numero_conta:
                if conta['senha'] == senha:
                    print("Login bem-sucedido!")
                    menu_bancario(conta['numero_conta'])
                    break
                else:
                    print("Senha incorreta.")
                    break
        else:
            print("Número da conta ou nome de usuário inválidos.")

# Função para exibir o menu bancário
def menu_bancario(numero_conta):
    while True:
        print("\n== Banco dos Amigos ==")
        print("\n== Menu Bancário ==")
        print("1. Depositar")
        print("2. Extrato")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Upgrade")
        print("6. Empréstimo")
        print("7. Cartão de Crédito")
        print("8. Deslogar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            depositar(numero_conta)
        elif opcao == "2":
            extrato(numero_conta)
        elif opcao == "3":
            sacar(numero_conta)
        elif opcao == "4":
            transferir(numero_conta)
        elif opcao == "5":
            upgrade(numero_conta)
        elif opcao == "6":
            emprestimo(numero_conta)
        elif opcao == "7":
            cartao_credito(numero_conta)
        elif opcao == "8":
            print("Deslogando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para realizar um depósito na conta
def depositar(numero_conta):
    valor = float(input("Digite o valor do depósito: "))

    # Verifica o limite de depósito
    limite = 500
    tipo_conta = contas[numero_conta]['tipo']
    if tipo_conta == 'corrente':
        limite = 500
    elif tipo_conta == 'premium':
        limite = 1000
    elif tipo_conta == 'corporativa':
        limite = 2000

    if valor > limite:
        print("Limite de depósito excedido.")
        return

    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        print("Contando cédulas...")
        time.sleep(2)
        contas[numero_conta]['saldo'] += valor

        # Atualiza o extrato
        if numero_conta not in extratos:
            extratos[numero_conta] = []
        extratos[numero_conta].append(f"Depósito: +{valor}")
        print("Depósito realizado com sucesso.")
    else:
        print("Senha incorreta.")

# Função para exibir o extrato da conta
def extrato(numero_conta):
    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        print("Extrato:")
        if numero_conta in extratos:
            for movimento in extratos[numero_conta]:
                print(movimento)
        else:
            print("Nenhum movimento no extrato.")
        print("Saldo atual:", contas[numero_conta]['saldo'])
    else:
        print("Senha incorreta.")

# Função para realizar um saque na conta
def sacar(numero_conta):
    valor = float(input("Digite o valor do saque: "))

    # Verifica o saldo da conta
    saldo = contas[numero_conta]['saldo']
    if valor > saldo:
        print("Saldo insuficiente.")
        return

    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        print("Contando cédulas...")
        time.sleep(2)
        print("Erro: Cédulas insuficientes.")
    else:
        print("Senha incorreta.")

# Função para realizar uma transferência de uma conta para outra
def transferir(numero_conta):
    valor = float(input("Digite o valor da transferência: "))

    # Verifica o limite de transferência
    limite = 500
    tipo_conta = contas[numero_conta]['tipo']
    if tipo_conta == 'corrente':
        limite = 1000
    elif tipo_conta == 'premium':
        limite = 2000
    elif tipo_conta == 'corporativa':
        limite = 5000

    if valor > limite:
        print("Limite de transferência excedido.")
        return

    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        destino = input("Digite o número da conta de destino: ")
        if destino in contas:
            # Verifica o saldo da conta de origem
            saldo_origem = contas[numero_conta]['saldo']
            if valor > saldo_origem:
                print("Saldo insuficiente para transferência.")
                return

            contas[numero_conta]['saldo'] -= valor
            contas[destino]['saldo'] += valor

            # Atualiza o extrato da conta de origem
            if numero_conta not in extratos:
                extratos[numero_conta] = []
            extratos[numero_conta].append(f"Transferência para {destino}: -{valor}")

            # Atualiza o extrato da conta de destino
            if destino not in extratos:
                extratos[destino] = []
            extratos[destino].append(f"Transferência de {numero_conta}: +{valor}")

            print("Transferência realizada com sucesso.")
        else:
            print("Número de conta de destino inválido.")
    else:
        print("Senha incorreta.")

# Função para realizar o upgrade do tipo de conta
def upgrade(numero_conta):
    if contas[numero_conta]['tipo'] != 'corrente':
        print("Você já realizou o upgrade da sua conta.")
        return

    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        print("Parabéns! Sua conta foi atualizada para o tipo Premium.")
        contas[numero_conta]['tipo'] = 'premium'
    else:
        print("Senha incorreta.")

# Função para realizar um empréstimo na conta
def emprestimo(numero_conta):
    if contas[numero_conta]['tipo'] == 'corporativa':
        print("Você não pode solicitar um empréstimo para uma conta corporativa.")
        return

    if 'emprestimo' in contas[numero_conta]:
        print("Você já solicitou um empréstimo.")
        return

    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        valor = float(input("Digite o valor do empréstimo: "))
        contas[numero_conta]['saldo'] += valor
        contas[numero_conta]['emprestimo'] = valor
        print("Empréstimo concedido.")
    else:
        print("Senha incorreta.")

# Função para criar um cartão de crédito para a conta
def cartao_credito(numero_conta):
    senha = input("Digite a senha: ")
    if senha == contas[numero_conta]['senha']:
        if 'cartao_credito' in contas[numero_conta]:
            print("Você já possui um cartão de crédito.")
            return

        numero_cartao = str(random.randint(1000000000000000, 9999999999999999))
        limite = 500

        contas[numero_conta]['cartao_credito'] = {'numero': numero_cartao, 'limite': limite}
        print("Cartão de crédito criado com sucesso.")
        print("Número do cartão:", numero_cartao)
        print("Limite do cartão:", limite)
    else:
        print("Senha incorreta.")

# Função para deslogar da conta
def deslogar():
    print("Deslogando...")

# Função principal que exibe o menu de login
def menu_login():
    while True:
        print("\n== Banco dos Amigos ==")
        print("\n== Sistema Bancário ==\n")
        print("1. Criar conta")
        print("2. Logar conta")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            realizar_login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu de login
menu_login()
