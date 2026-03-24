import math
import random

# Função para ler números com validação
def ler_numero(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


# Função para ler opção do menu
def ler_opcao():
    while True:
        opcao = input("\nDigite o número da opção: ")
        if opcao in ["1", "2", "3", "4"]:
            return opcao
        else:
            print("Opção inválida. Escolha entre 1 e 4.")


# Menu principal
def mostrar_menu():
    print("\n=== BEM-VINDO AO CONVERSOR DE UNIDADES ===\n")
    print("Escolha uma categoria:")
    print("1 - Temperatura (Celsius para Fahrenheit)")
    print("2 - Medidas (Metros para Centímetros)")
    print("3 - Moedas Fictícias (Créditos Galácticos)")
    print("4 - Sair")


# Conversão de temperatura
def converter_temperatura():
    celsius = ler_numero("\nDigite a temperatura em Celsius: ")
    fahrenheit = (celsius * 9/5) + 32
    print(f"Resultado: {celsius}°C equivalem a {fahrenheit:.2f}°F")


# Conversão de medidas
def converter_medidas():
    metros = ler_numero("\nDigite o valor em metros: ")
    centimetros = metros * 100
    print(f"Resultado: {metros} m equivalem a {centimetros} cm")


# Conversão fictícia usando math e random
def converter_moeda():
    print("\n=== CONVERSÃO GALÁCTICA ===")

    valor = ler_numero("Digite o valor em créditos terrestres: ")

    taxa = random.uniform(1.5, 5.0)

    convertido = valor * taxa
    convertido_final = math.ceil(convertido)

    print(f"\nTaxa galáctica atual: {taxa:.2f}")
    print(f"Você terá aproximadamente {convertido_final} créditos galácticos")

    print("\nSimulação de valores futuros:")
    for i in range(3):
        variacao = random.uniform(0.8, 1.2)
        futuro = convertido_final * variacao
        print(f"Simulação {i + 1}: {math.floor(futuro)} créditos")


# Programa principal
while True:
    mostrar_menu()
    opcao = ler_opcao()

    if opcao == "1":
        converter_temperatura()

    elif opcao == "2":
        converter_medidas()

    elif opcao == "3":
        converter_moeda()

    elif opcao == "4":
        print("\nEncerrando o programa. Até mais.")
        break
