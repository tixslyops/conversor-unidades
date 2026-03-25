import math
import random
# biblioteca math: matemática do python
# biblioteca random: números aleatórios

def ler_numero(mensagem):
    while True:
# While True - Código que solicita entrada até o usuário digitar algo válida
        entrada = input(mensagem)
        try:
# Try: Código que tenta executar um bloco de código que pode dar erro
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
# Validação da mensagem, se o usuário digitar uma entrada válida retorna o valor e encerra função.
# Caso inválida, retorna a mensagem de erro e repete o loop.

def ler_opcao():
    while True:
        opcao = input("\nDigite o número da opção: ")
        if opcao in ["1", "2", "3", "4"]:
            return opcao
        else:
            print("Opção inválida. Escolha entre 1 e 4.")
# Leitura e validação das opções, verifica se a opção digitada está entre as válidas. Se sim, retorna a opção,
# Se não, retorna erro e repete

def mostrar_menu():
    print("\n=== BEM-VINDO AO CONVERSOR DE UNIDADES ===\n")
    print("Escolha uma categoria:")
    print("1 - Temperatura (Celsius para Fahrenheit)")
    print("2 - Medidas (Metros para Centímetros)")
    print("3 - Moedas Fictícias (Créditos Galácticos)")
    print("4 - Sair")
# Exibição do menu

# Conversão de temperatura
def converter_temperatura():
# Função que faz a conversão
    celsius = ler_numero("\nDigite a temperatura em Celsius: ")
# Solicita número válido
    fahrenheit = (celsius * 9/5) + 32
# Faz cálculo da conversão
    print(f"Resultado: {celsius}°C equivalem a {fahrenheit:.2f}°F")
# Resultado


# Conversão de medidas
def converter_medidas():
# Função para conversão de metros
    metros = ler_numero("\nDigite o valor em metros: ")
# Recebe valor validado
    centimetros = metros * 100
# Converte metros para centímetros
    print(f"Resultado: {metros} m equivalem a {centimetros} cm")
#Resultado

# Conversão fictícia usando math e random
def converter_moeda():
# Função para a conversão
    print("\n=== CONVERSÃO GALÁCTICA ===")
# Título
    valor = ler_numero("Digite o valor em créditos terrestres: ")
# Recebe valor validado
    taxa = random.uniform(1.5, 5.0)
# Gera um número aleatório entre 1.5 e 5.0
    convertido = valor * taxa
    convertido_final = math.ceil(convertido)
# Faz conversão e arredonda (math)
    print(f"\nTaxa galáctica atual: {taxa:.2f}")
    print(f"Você terá aproximadamente {convertido_final} créditos galácticos")
# Retorna taxa e resultado
    print("\nSimulação de valores futuros:")
    for i in range(3):
# Introduz à simulação e retorna as três seguintes simulações:
        variacao = random.uniform(0.8, 1.2)
# Variação aleatória
        futuro = convertido_final * variacao
# Valor futuro
        print(f"Simulação {i + 1}: {math.floor(futuro)} créditos")
# Resultado arredondado (math)

# Programa principal
while True:
# Programa só para quando usuário solicita
    mostrar_menu()
    opcao = ler_opcao()
# Mostra menu e lê opções válidas
    if opcao == "1":
        converter_temperatura()

    elif opcao == "2":
        converter_medidas()

    elif opcao == "3":
        converter_moeda()
# Executa moedas
    elif opcao == "4":
# Encerra programa
        print("\nEncerrando o programa. Até mais.")
        break
# Break - sai do While
