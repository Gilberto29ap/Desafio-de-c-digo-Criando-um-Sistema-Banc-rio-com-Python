import time
import os

LIMITE_POR_SAQUE = 500
NUMERO_MAX_SAQUE = 3
saldo = 1000
extrato = ""
saque_do_dia = 1

def menu_inicial():

    carregamento()

    os.system('cls' if os.name == 'nt' else 'clear') #limpa tela

    title = "Bem vindo ao BANCO PYTHON"

    for letter in title:
        
        print(letter, end=" ")

    print("""
    Digite a opção desejada e pressione ENTER
            [s] SAQUE
            [e] EXTRATO
            [d] DEPÓSITO
            [q] SAIR
    """)

def carregamento():
    tempo_carregamento = 8
    for i in range(tempo_carregamento):
        if i <= tempo_carregamento:
            print(".")
            time.sleep(0.25)

menu_inicial()



while True:

    opcao = input("Digite a opção desejada: ")

    os.system('cls' if os.name == 'nt' else 'clear') #limpa tela

    if opcao == "s":
        print("--------SAQUE--------")
        valor_saque = int(input("digite o valor: "))

        if valor_saque > 0: 
        
            if saque_do_dia <= NUMERO_MAX_SAQUE:
                if valor_saque <= LIMITE_POR_SAQUE:
                    if valor_saque <= saldo:
                        print("Efetuando saque, por favor aguarde!")
                        carregamento()
                        print("Saque efetuado com sucesso!")
                        input("Pressione enter para sair")
                        menu_inicial()
                        
                        saldo -= valor_saque
                        saque_do_dia += 1
                        extrato += f"\n Saque       -R$ {valor_saque:.2f}"
                    
                    else:
                        print(f"Saldo insuficiente, seu saldo atual é de: {saldo}")
                        input("Pressione enter para sair")
                        menu_inicial()

                else: 
                    print("O limite máximo para saques é R$ 500")
                    input("Pressione enter para sair")
                    menu_inicial()
                    
            else:
                print("Número de saques diários excedido. Tente Novamente amanhã")
                input("Pressione enter para sair")
                menu_inicial()

        else:
            print("Valor inválido")
            menu_inicial()
    

    elif opcao == "e":
        print("--------EXTRATO--------")
        print(extrato)
        input("Pressione enter para sair")
        menu_inicial()


    elif opcao == "d":
        print("--------DEPÓSITO-------")
        deposito_valor = int(input("Digite o valor a ser depositado: "))

        if deposito_valor > 0:
            print(f"depósito de R$ {deposito_valor:.2f} efetuado com sucesso!")
            extrato += f"\n Depósito    +R$ {deposito_valor:.2f}"
            input("Pressione enter para sair")
            menu_inicial()

        else:
            print("Valor inválido")
            input("Pressione enter para sair")
            menu_inicial()


    elif opcao == "q":
        print("Obrigado por utilizar o BANCO PYTHON!")
        time.sleep(1)
        break


    else:
        print("Opção inválida, tente novamente")
        menu_inicial()






    





