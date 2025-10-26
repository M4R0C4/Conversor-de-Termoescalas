import os

def lin():
    print('~' * 60)
    print('''
░█▀▀█ ░█▀▀▀█ ░█▄─░█ ░█──░█ ░█▀▀▀ ░█▀▀█ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀█ 　 ── 　 ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ ░█▀▄▀█ ░█▀▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▀▀█ ─█▀▀█ ░█─── ─█▀▀█ ░█▀▀▀█ 
░█─── ░█──░█ ░█░█░█ ─░█░█─ ░█▀▀▀ ░█▄▄▀ ─▀▀▀▄▄ ░█──░█ ░█▄▄▀ 　 ▀▀ 　 ─░█── ░█▀▀▀ ░█▄▄▀ ░█░█░█ ░█──░█ ░█▀▀▀ ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█─── ░█▄▄█ ─▀▀▀▄▄ 
░█▄▄█ ░█▄▄▄█ ░█──▀█ ──▀▄▀─ ░█▄▄▄ ░█─░█ ░█▄▄▄█ ░█▄▄▄█ ░█─░█ 　 ── 　 ─░█── ░█▄▄▄ ░█─░█ ░█──░█ ░█▄▄▄█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█▄▄█ ░█─░█ ░█▄▄▄█''')


def exibir_mensagem_de_erro():
    print('\n⚠️ Opção inválida. Tente novamente!\n')

def voltar_ao_menu_principal():
    input('\nPressione Enter para voltar ao Menu Principal...')
    main()

'''Função para criar o termômetro'''

def criar_termometro():
    nome_termometro = input("Qual é o nome desse termômetro? ")
    unidade_medida = input("Qual letra acompanhará a unidade de medida? ")
    ponto_vapor = float(input(f"Ponto de vapor da água mostrado no {nome_termometro}ômetro: "))
    ponto_gelo = float(input(f"Ponto de gelo da água mostrado no {nome_termometro}ômetro: "))
    os.system('cls')
    print(f"O termômetro {nome_termometro}, unidade {unidade_medida}.")
    print(f"Fusão: {ponto_gelo}º{unidade_medida} | Ebulição: {ponto_vapor}º{unidade_medida}.")
    exibir_opcoes_conversoes(unidade_medida, ponto_vapor, ponto_gelo)

'''Exibe as opções para o novo termômetro'''

def exibir_opcoes_conversoes(unidade_medida, ponto_vapor, ponto_gelo):        
    print('''
    [1] Converter para Celsius 
    [2] Converter para Kelvin
    [3] Converter para Fahrenheit
    ''')
    try:
        escolha_conversao = int(input('Qual a conversão que você deseja escolher: '))
        if escolha_conversao == 1:
            criado_para_celsius(unidade_medida, ponto_vapor, ponto_gelo)
        elif escolha_conversao == 2:
            criado_para_kelvin(unidade_medida, ponto_vapor, ponto_gelo)
        elif escolha_conversao == 3:
            criado_para_fahrenheit(unidade_medida, ponto_vapor, ponto_gelo)
        else:
            exibir_mensagem_de_erro()
            voltar_ao_menu_principal()
    except ValueError:
        exibir_mensagem_de_erro()
        voltar_ao_menu_principal()

'''converte o novo termomêtro para as escalas conhecidas'''

def criado_para_celsius(unidade_medida, ponto_vapor, ponto_gelo):
    tempnova = float(input(f"Quantos º{unidade_medida} você deseja converter para Célsius? "))
    celsius = 100 * (tempnova - ponto_gelo) / (ponto_vapor - ponto_gelo)
    print(f"{tempnova}º{unidade_medida} corresponde a {celsius:.2f}ºC!")
    voltar_ao_menu_principal()

def criado_para_kelvin(unidade_medida, ponto_vapor, ponto_gelo):
    tempnova = float(input(f"Quantos º{unidade_medida} você deseja converter para KELVIN? "))
    kelvin = 100 * (tempnova - ponto_gelo) / (ponto_vapor - ponto_gelo) + 273.15
    print(f"{tempnova}º{unidade_medida} equivale a {kelvin:.2f}K")
    voltar_ao_menu_principal()

def criado_para_fahrenheit(unidade_medida, ponto_vapor, ponto_gelo):
    tempnova = float(input(f"Quantos º{unidade_medida} você deseja converter para FAHRENHEIT? "))
    fahrenheit = 180 * (tempnova - ponto_gelo) / (ponto_vapor - ponto_gelo) + 32
    print(f"{tempnova}º{unidade_medida} equivale a {fahrenheit:.2f}ºF")
    voltar_ao_menu_principal()

'''Menu Principal e Menu Secundário'''

def exibir_menu_principal():
    lin()
    print('''O que deseja fazer?
    [1] Criar um termômetro
    [2] Converter temperaturas em termômetros conhecidos''')

def escolher_menu_principal():
    try:
        escolha = int(input("Sua opção: "))
        if escolha == 1:
            criar_termometro()
        elif escolha == 2:
            exibir_converter_temperaturas_conhecidas()
            escolha_temperaturas_conhecidas()
        else:
            exibir_mensagem_de_erro()
            voltar_ao_menu_principal()
    except ValueError:
        exibir_mensagem_de_erro()
        voltar_ao_menu_principal()

def exibir_converter_temperaturas_conhecidas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Qual das opções abaixo você deseja? 
    [1] KELVIN para CELSIUS
    [2] FAHRENHEIT para CELSIUS
    [3] FAHRENHEIT para KELVIN
    [4] Voltar ao Menu Principal''')

def escolha_temperaturas_conhecidas():
    try:
        escolha = int(input("Qual será a sua opção: "))
        if escolha == 1:
            kelvin_para_celsius()
        elif escolha == 2:
            fahrenheit_para_celsius()
        elif escolha == 3:
            fahrenheit_para_kelvin()
        elif escolha == 4:
            voltar_ao_menu_principal()
        else:
            exibir_mensagem_de_erro()
            voltar_ao_menu_principal()
    except ValueError:
        exibir_mensagem_de_erro()
        voltar_ao_menu_principal()

'''Conversores conhecidos'''

def kelvin_para_celsius():
    kelvin = float(input("Temperatura em KELVIN: "))
    celsius = kelvin - 273.15
    print(f"{kelvin}K equivale a {celsius:.2f}ºC")
    voltar_ao_menu_principal()

def fahrenheit_para_celsius():
    fahrenheit = float(input("Temperatura em FAHRENHEIT: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}ºF equivale a {celsius:.2f}ºC")
    voltar_ao_menu_principal()

def fahrenheit_para_kelvin():
    fahrenheit = float(input("Temperatura em FAHRENHEIT: "))
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    print(f"{fahrenheit}ºF equivale a {kelvin:.2f}K")
    voltar_ao_menu_principal()

'''Corpo Principal do Programa'''

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_menu_principal()
        escolher_menu_principal()

if __name__ == '__main__':
    main()
