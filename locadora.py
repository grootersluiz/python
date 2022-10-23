carros = [["BMW 320i", 130.00, True],
          ["Mercedes C180", 110.00, True],
          ["BMW X6", 350.00, True],
          ["Porsche Cayenne", 350.00, True],
          ["Ferrari PuroSangue", 550.00, True],
          ["Volvo XC60", 150.00, True],
          ["Audi Q8", 350.00, True],
          ["Porsche Macan", 250.00, True],
          ["Jaguar F-Pace", 350.00, True]]

disponiveis = []
alugados = []

def atualizaLista():

    for i in range(len(carros)):
        if carros[i][2] == True:
            disponiveis.append(carros[i])
        elif carros[i][2] == False:
            alugados.append(carros[i])

def menuPrincipal():

    print("==========  Bem-vindo à Lou Cars  ==========\n")
    print("(1) Alugar veículo.")
    print("(2) Devolver veículo.")
    print("(3) Sair.")
    opcao = int(input("Digite a opção desejada:\n"))
    while (opcao < 1) or (opcao > 3):
        opcao = int(input("Digite a opção desejada:\n"))
    return opcao

opc = menuPrincipal()

while opc != 3:

    if opc == 1:
        atualizaLista()
   
        for k, car in enumerate(disponiveis):
            print("{} - {} ============== {:.2f}".format(k, car[0], car[1]))

        carroEscolhido = int(input("Escolha o veículo:\n"))

        while (carroEscolhido < 0) or (carroEscolhido > len(disponiveis) - 1):    
            carroEscolhido = int(input("Escolha o veículo:\n"))

        dias = float(input("Digite a quantidade de dias de locação:\n"))
    
        for j, carEsc in enumerate(disponiveis):
            if j == carroEscolhido:
                print("Você selecionou o veículo {}, o valor total da locação é R$ {:.2f}.\n".format(carEsc[0], carEsc[1] * dias))
                for x in range(len(carros)):
                    if carros[x][0] == carEsc[0]:
                        carros[x][2] = False

        disponiveis = []
        alugados = []

        opc = menuPrincipal()

    elif opc == 2:
        atualizaLista()

        if len(alugados) == 0:
            print("Não há veículos a serem devolvidos!\n")
            alugados = []
            disponiveis = []
            opc = menuPrincipal()


        else:

            for l, carD in enumerate(alugados):
                print("{} - {} ============== {:.2f}".format(l, carD[0], carD[1]))

            carroEscolhidoD = int(input("Escolha o veículo:\n"))

            while (carroEscolhidoD < 0) or (carroEscolhidoD > len(alugados) - 1):    
                carroEscolhidoD = int(input("Escolha o veículo:\n"))

            for m, carDev in enumerate(alugados):
                if m == carroEscolhidoD:
                    print("O veículo {} foi devolvido com sucesso.\n".format(carDev[0]))
                    for y in range(len(carros)):
                        if carros[y][0] == carDev[0]:
                            carros[y][2] = True

            alugados = []
            disponiveis = []

            opc = menuPrincipal()

    


    