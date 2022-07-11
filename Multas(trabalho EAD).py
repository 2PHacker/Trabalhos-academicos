import pickle
import os

def limpa_Tela():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def CadMoto(motoristas,veiculos,infracao,naturezas):
    CNH_nova= input(("Digite a CNH do motorista:"))
    if CNH_nova in motoristas:
        print("CNH JA CADASTRADA, retornando ao menu")
        main()
    else:
        Nome_motorista = input(("Digite o nome do motorista:"))
        data = input("Digite a data de nascimento do motorista(separando com barra):")
        dia,mes,ano = data.split("/")
        motoristas[CNH_nova]=(Nome_motorista,(int(dia),int(mes),int(ano)))
        with open("multas.bin","wb") as arq:
            pickle.dump(motoristas,arq)
            pickle.dump(veiculos, arq)
            pickle.dump(infracao, arq)
            pickle.dump(naturezas, arq)
            limpa_Tela()
        main()
        
def CadVeiculo(motoristas,veiculos,infracao,naturezas):
    placa_nova = input("Digite a placa do veiculo a ser cadastrado:")
    if placa_nova in veiculos:
        print("Placa ja cadastrada, retornando ao menu")
        main()
    else:
        CNH_proprietario = input("Digite a CNH do dono do veiculo:")
        modelo = input("Digite o modelo do veiculo:")
        cor = input("Digite a cor do veiculo:")
        veiculos[placa_nova]= (CNH_proprietario,modelo,cor)
        with open("multas.bin","wb") as arq:
            pickle.dump(motoristas, arq)
            pickle.dump(veiculos, arq)
            pickle.dump(infracao, arq)
            pickle.dump(naturezas, arq)
            limpa_Tela()
        main()

def Alterar_dono(motoristas,veiculos,infracao,naturezas):
    placa_veiculo = input("Digite a placa do veiculo a ser analisado:")
    if placa_veiculo not in veiculos:
        print("Placa nao cadastrada,retornando ao menu")
        main()
    CNH_novo_prop = input("Digite CNH do proprietario em questao:")
    if CNH_novo_prop not in motoristas:
        print("CNH nao cadastrada, retornando ao menu")
        main()
    else:
        modelo = veiculos[placa_veiculo][1]
        cor = veiculos[placa_veiculo][2]
        tupla = (CNH_novo_prop,modelo,cor)
        veiculos[placa_veiculo] = tupla
        with open("multas.bin","wb") as arq:
            pickle.dump(motoristas, arq)
            pickle.dump(veiculos, arq)
            pickle.dump(infracao, arq)
            pickle.dump(naturezas, arq)
            limpa_Tela()
        main()

def CadInfra(motoristas,veiculos,infracao,naturezas):
    quant = len(infracao) + 1
    data_evento = input("Digite a data em que a infracao ocorreu:")
    dia,mes,ano = data_evento.split("/")
    placa_carro = input(("Digite a placa do carro envolvido na infracao:"))
    nivel_infracao = int(input("Digite o nivel da infracao ( 1 a 4, correspondendo de Leve ate Gravissima):"))
    for item in naturezas:
        if item == "Leve" and nivel_infracao == 1:
            nivel = item
        if item == "Media" and nivel_infracao == 2:
            nivel = item
        if item == "Grave" and nivel_infracao == 3:
            nivel = item
        if item == "Gravissima" and nivel_infracao == 4:
            nivel = item
    tupla = (quant,(int(dia),int(mes),int(ano)),placa_carro,nivel)
    infracao.append(tupla)
    with open("multas.bin", "wb") as arq:
        pickle.dump(motoristas, arq)
        pickle.dump(veiculos, arq)
        pickle.dump(infracao, arq)
        pickle.dump(naturezas, arq)
        limpa_Tela()
    main()

def main():
    with open("multas.bin","rb") as arq:
        motoristas = pickle.load(arq)
        veiculos = pickle.load(arq)
        infracao = pickle.load(arq)
        naturezas = pickle.load(arq)
    menu ='''Bem vindo ao menu:
    1 -Cadastrar Motorista
    2- Cadastrar Veiculo
    3 - Alterar proprietario do veiculo
    4 - Cadastrar nova Infracao
    5 - Sair do sistema'''
    print(menu)
    escolha = int(input("Digite a sua escolha:"))
    limpa_Tela()
    while escolha > 5 or escolha == 0 :
        print("Escolha invalida, escolha novamente")
        menu = '''Bem vindo ao menu:
        1 -Cadastrar Motorista
        2- Cadastrar Veiculo
        3 - Alterar proprietario do veiculo
        4 - Cadastrar nova Infracao
        5 - Sair do sistema'''
        print(menu)
        escolha = int(input("Digite a sua escolha:"))
        limpa_Tela()
    if escolha == 1 :
        CadMoto(motoristas,veiculos,infracao,naturezas)
    if escolha == 2:
        CadVeiculo(motoristas,veiculos,infracao,naturezas)
    if escolha == 3:
        Alterar_dono(motoristas,veiculos,infracao,naturezas)
    if escolha == 4:
        CadInfra(motoristas,veiculos,infracao,naturezas)
    if escolha == 5:
        print("Obrigado por usar o sistema")

main()