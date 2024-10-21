def lin():
    print('~'*60)

lin()    
print("{:=^30}".format(' CONVERSOR DE TEMPERATURA UNIVERSAL '))
lin()
fim=False
while not fim:
    print('''O que deseja fazer?
    [1] Criar um termômetro
    [2] Converter temperatura''')
    opção1=int(input("Sua primeira opção: ")) #CRIANDO O NOVO TERMÔMETRO#
    if opção1 == 1:
        nome=input("Qual é o nome desse termômetro? ")
        unid=input("Qual letra acompanhará a unidade de medida? ")
        pv=float(input("Ponto de vapor da água mostrado no {}ômetro: ".format(nome)))
        pg=float(input("Ponto de gelo da água mostrado no {}ômetro:: ".format(nome)))
        print('''
        [1] CONVERTENDO PARA CELSIUS 
        [2] CONVERTENDO PARA KELVIN
        [3] CONVERTENDO PARA FAHRENHEINT'''.format(unid))
        opção2=int(input("O que devo fazer: ")) #CONVERTENDO PARA CELSIUS O NOVO TERMÔMETRO#
        if opção2 == 1:
            tempnova=float(input("Quantos º{} você deseja converter para Célsius? ".format(unid)))
            cel=(100*(tempnova-pg)/(pv-pg))
            print("{}º do {}, corresponde a {:.2f}ºC!".format(tempnova,nome,cel))
        elif opção2 == 2:
            tempnova=float(input("Quantos º{} você deseja converter para KELVIN? ".format(unid)))
            k=(100*(tempnova-pg)/(pv-pg)+273)
            print("{}º{} equivale a {:.2f}K".format(tempnova,unid,k))
        else:
            tempnova=float(input("Quantos º{} você deseja converter para FAHRENHEIT? ".format(unid)))
            f=180*(tempnova-pg)/(pv-pg)+32
            print("{}º{} equivale a {:.2f}F".format(tempnova,unid,f))
    
    else: #CONVERTENDO AS ESCALAS FAMOSAS#
        print('''Qual das opções abaixo você deseja? 
        [1] KELVIN para CELSIUS
        [2] FAHRENHEINT para CELSIUS
        [3] KELVIN para FAHRENHEIT''')
        opção3=int(input("Qual é a sua opção: "))
        if opção3 == 1:
            k=float(input("Temperatura em KELVIN: "))
            celsius=k-273
            print("{}K equivale a {:.2f}ºC".format(k,celsius))
        elif opção3 == 2:
            f=float(input("Temperatura em FAHRENHEINT: "))
            celsius=(100*(f-32)/(180))
            print("{}ºF equivale a {:.2f}ºC".format(f,celsius))
        else:
            f=float(input("Temperatura em FAHRENHEINT: "))
            k=(100*(f-32)/(180)+273)
            print("{}ºF equivale a {}K.".format(f,k))
    res=str(input("Deseja começar outra vez [S/N] "))
    if res in "Nn":
        fim=True
    elif res in "Ss":
        fim=False
print("Fim")
