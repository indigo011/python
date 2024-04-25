import os
import time

file = open("data.txt", )

def gerar_sequencia(caractere, qtd):
    print(caractere*qtd)

def config():
    global caractere, quantidade
    option = config_menu()

    if option == 0:
        menu()
    elif option == 1:
        os.system("cls")
        print(f"\nCaracte atual: {caractere}")
        caractere = input("Informe o caractere desejado: ")[0]
        print("\nCaractere definido com sucesso!")
        time.sleep(2)
        menu()
    else: 
        os.system("cls")
        print(f"Quantidade atual: {quantidade}")
        quantidade = int(input("Informe a quantidade desejada: "))
        print("\nQuantidade definida com sucesso!")
        time.sleep(2)
        menu()

def menu():
    os.system("cls")
    option = int(input("\n1. Gerar sequência\n2. Configurar\n0. Sair\n\n-> "))

    if not option:
        print("Encerrando programa...")
        time.sleep(2)

    elif option == 1:
        gerar_sequencia(caractere,quantidade)

    else:
        config()

def config_menu():
    os.system("cls")
    option = int(input("\n1. Configurar caractere\n2. Configurar quantidade\n0. Voltar ao menu\n\n-> "))
    return option

menu()


