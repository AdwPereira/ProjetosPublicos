import time
import random

usuários = {}
funcionários = {}
artistas = {}



def main():
    global nomeusuário
    funcionário = False
    admin = False
    print("\n \n __________Login__________ \n  \n")                            #########################   LOGIN   #####################
    print("Olá Usuário! Como deseja logar?")
    print("1- Login Usuário \n 2- Login Administrativo")
    asw = int(input("Digite Sua Opção de Login ao Lado: "))
    if asw == 1:
        login = False
        while login == False:
            nome = input("Digite seu nome completo ao Lado: ")
            senha = int(input("Digite ao lado sua senha: "))
            if nome in dict.keys(usuários):
                if senha == usuários[nome]:
                    print(f"Login Bem Sucedido!\n \n Seja Bem-Vindo {nome}")
                    login = True
                else:
                    print("Erro de Login")
            else:
                print("Erro de Login \n")
                

    elif asw == 2:
        login = False
        while login == False:
            nome = input("Digite seu nome completo ao Lado: ")
            ID = int(input("Digite ao lado o seu ID completo: "))
            if nome == "Admin" and ID == 123123:
                print(f"Login bem Sucedido!\n \n Seja Bem-Vindo {nome}")
                login = True
                admin = True

            elif nome in dict.keys(funcionários):
                if ID == funcionários[nome]:
                    print(f"Login Bem Sucedido!\n \n Seja Bem-Vindo {nome}")
                    funcionário = True
                    login = True
                else:
                    print("Erro de Login")
            else:
                print("Erro de Login \n")


    nomeusuário = nome

    if login == True and funcionário == False and admin == False:
        menuUsuários()
        

    elif login == True and funcionário == True and admin == False:
        print("O que deseja fazer? \n 1- Ir Para o Menu dos Funcionários /n 2- Acessar como Usuário")
        pergunta = int(input("Digite ao Lado sua Opção: "))
        if pergunta == 1:
            #cadastroL()
            menuFuncionarios()

    elif login == True and admin == True:
        print("O que deseja fazer? \n 1- Ir Para o Menu do Admin \n 2- Ir Para o Menu dos Funcionários \n 3- Acessar como Usuário")
        pergunta = int(input("Digite ao Lado sua Opção: "))
        if pergunta == 1:
            #gerenciar()
           menuAdmin()
        elif pergunta == 2:
            #cadastroL()
            menuFuncionarios()
        elif pergunta == 3:
            menuUsuários()



def menuAdmin():
    global usuários, funcionários
    usuários = {}
    funcionários = {}
    end = False
    print("Por Favor Aguarde...")

    while end != True:
        time.sleep(3)
        print("\n \n __________MENU DO ADMNISTRADOR__________ \n  \n") ##########################        ADMIN        ###########################

        escolha = int(input(f"Olá {nomeusuário}! O que Deseja fazer ? \n \n Cadastrar Novos Usuários = 1 \n Remover Usuários = 2 \n Listar Usuários = 3 \n Sair = 4 \n Digite sua Opção ao Lado: "))    
        if escolha == 1:    
            tipousuário = int(input("\n Será Usuário ou Funcionário? \n \n Usuário = 1 \n Funcionário = 2 \n Digite sua Opção ao Lado: "))
            if tipousuário == 1:    
                qusers = int(input("\n Digite ao Lado a quantidade de Usuários que Deseja Cadastrar no Sistema: "))
                cont = 1
                for i in range(qusers):
                    nome = input(f"Digite o Nome Completo do {cont}º Usuário que Deseja Cadastrar: ")
                    senha = int(input(f"Digite ao Lado a senha numérica do {cont}º Usuário ao lado :"))
                    usuários[nome] = senha
                    cont += 1

            if tipousuário == 2: 
                qusers = int(input("\n Digite ao Lado a quantidade de Funcionários que Deseja Cadastrar no Sistema: "))
                cont = 1
                for i in range(qusers):
                    nome = input(f"Digite o Nome Completo do {cont}º Funcionário que Deseja Cadastrar: ")
                    ID = int(input(f"Digite ao Lado a ID do {cont}º Funcionário ao lado :"))
                    funcionários[nome] = ID
                    cont += 1


        if escolha == 2:
            tipousuário = int(input("\n Será Usuário ou Funcionário? \n \n Usuário = 1 \n Funcionário = 2 \n Digite sua Opção ao Lado: "))
            if tipousuário == 1:
                print(f"\n \n Os Usuários No sistema são {usuários}.")
                nomer = input("\n Digite o Nome do Usuário que Deseja Remover do Sistema: ")
                usuários.pop(nomer)
                print("Usuário Removido com Sucesso! \n \n")

            elif tipousuário == 2:
                print(f"Os Funcionários No sistema são {funcionários}.")
                nomer = input("\n Digite o Nome do Funcionário que Deseja Remover do Sistema: ")
                funcionários.pop(nomer)                                
                print("Usuário Removido com Sucesso! \n \n")


        if escolha == 3:
            print(f"\n \n Os Usuários No sistema são {usuários}.")
            print(f"Os Funcionários No sistema são {funcionários}.")



        if escolha == 4:
            end = True
    
    main()




def CadastroPFuncionarios():
    global artistas #,obras

    #obras = {}
    print("\n \n ------ Menu de Cadastro ----- \n \n")
    print("O que você deseja fazer? \n 1- Cadastrar Artista \n 2- Cadastrar Obra \n 3- Sair")
    asw = int(input("Digite sua Opção ao lado: "))
    if asw == 1:
        nome = input("Digite o nome do artista para cadastra-lo: ")
        data_nascimento = input("Digite a data de nascimento do artista: ")
        local_nascimento = input("Digite o local de nascimento do artista: ")
        biografia = input("Digite a biografia do artista: ")
        estilos = input("Digite os estilos artísticos do artista (separados por vírgula): ").split(',')
        artista = [data_nascimento, local_nascimento, biografia, estilos, []]
        artistas[nome] = artista
    
    
    
    
    elif asw == 2:
        nome_artista = input("Digite o nome do artista da obra: ")
        if nome_artista in dict.keys(artistas):
                titulo = input("Digite o título da obra: ")
                data_criacao = input("Digite a data de criação da obra: ")
                tema = input("Digite o tema da obra: ")
                estilo = input("Digite o estilo da obra: ")
                descricao = input("Digite a descrição da obra: ")
                tecnica = input("Digite a técnica utilizada na obra: ")
                localizacao = input("Digite a localização da obra na sala de exposição: ")
                obra = [titulo, data_criacao, tema, estilo, descricao, tecnica, localizacao]
                #obras[nome_artista].append(obra)
                artistas[nome_artista][-1].append(obra)

                
        else:
            print("Artista não encontrado.")
    elif asw == 3:
        menuFuncionarios()






def menuFuncionarios():
    asw = 0
    end = False
    count = 0
    while end != True:
        time.sleep(3)
        print("\n \n __________MENU DOS FUNCIONÁRIOS__________ \n  \n")                             #################### MENU FUNCIONARIOS ######################
        print(f"Olá {nomeusuário}! O que você deseja fazer? \n 1- Cadastrar Obras ou Artistas \n 2- Remover Obras ou Artistas \n 3- Listar Obras e Artistas \n 4- Registrar Emprestimo de Obra Para Eventos \n 5- Gerenciar solicitações de visita \n 6- Sair")
        asw = int(input("Digite sua opção ao lado: "))

        if asw == 1:
            CadastroPFuncionarios()

        elif asw == 2:
            removertipo = int(input("\n Deseja Remover um Artista ou uma Obra? \n \n Artista = 1 \n Obra = 2 \n Digite sua Opção ao Lado: "))
            if removertipo == 1:
                print("\n \n Os Artistas No sistema são: ")
                for nome in artistas.keys():
                    print(nome)
                nomer = input("\n Digite o Nome do Artista que Deseja Remover do Sistema: ")
                artistas.pop(nomer)
                print("Artista Removido com Sucesso! \n \n")


            elif removertipo == 2:
                print("\n \n Os Artistas No sistema são: ")
                for nome in artistas.keys():
                    print(nome)
                nome_artista = input("\n Digite o Nome do Artista para ver as obras que Deseja Remover do Sistema: ")
                if nome_artista in artistas.keys():
                    print(f"\n \n As Obras do Artista {nome} no sistema são {artistas[nome_artista][-1]}.")
                    titulo_obra = input("\n Digite o Título da Obra que Deseja Remover do Sistema: ")
                    for obra in artistas[nome_artista][-1]:
                        if obra[0] == titulo_obra:
                            artistas[nome_artista][-1].remove(obra)  
                            print("Obra Removida com Sucesso! \n \n")

                        else:
                            print("Obra não encontrada. \n \n")



        elif asw == 3:
            print("\n \n Artistas e suas Obras: \n")
            for nome_artista, detalhes_artista in artistas.items():
                print(f"Artista: {nome_artista}")
                print("Obras:")
                for obra in detalhes_artista[-1]:
                    print(f"  - {obra[0]}")
                print("\n")
            
            time.sleep(3)


        elif asw == 4:
            dadosemprestimo = []
            adddado = input("Digite ao Lado o Período de Emprestimo da Obra: ")
            dadosemprestimo.append(adddado)
            adddado = input("Digite ao Lado o Nome do Evento do Emprestimo: ")
            dadosemprestimo.append(adddado)
            adddado = input("Digite ao Lado o Nome do Responsável do Evento: ")
            dadosemprestimo.append(adddado)
            adddado = input("Digite ao Lado o Tema do Evento: ")
            dadosemprestimo.append(adddado)
            print("\n \n Artistas e suas Obras: \n")
            for nome_artista, detalhes_artista in artistas.items():
                print(f"Artista: {nome_artista}")
                print("Obras:")
                for obra in detalhes_artista[-1]:
                    print(f"  - {obra[0]}")
                print("\n")
            adddado = input("Digite ao Lado a Obra Emprestada: ")
            dadosemprestimo.append(adddado)
            texto = f"Período de Emprestimo: {dadosemprestimo[0]} \n Nome do Evento: {dadosemprestimo[1]} \n Responsável pelo Evento: {dadosemprestimo[2]} \n Tema do evento: {dadosemprestimo[3]} \n Obra Emprestada: {dadosemprestimo[4]} \n \n"


            try:
                with open('C:\\Users\\Darth Kaida\\Desktop\\Programação\\Python\\Projeto Museu\\RegistroDeEmprestimos.txt', 'a') as file:
                    file.write(texto)
                
            except FileNotFoundError as e:
                print("Error: O Arquivo 'RegistroDeEmprestimos.txt' Não Foi Encontrado, Verifique Manualmente.")
            
            except Exception as e:
                print("Error: Algo de Errado não está certo...")

            else:
                print(" \n Dados de Empréstimo Adicionados Com Exito!")



        elif asw == 5:
            try:
                acabar = False
                while count < len(fila):
                    print(fila[count])
                    print("Aprovar ou Rejeitar Solicitação?")
                    statuspedido = int(input("1- Aprovar \n 2- Rejeitar \n Digite sua Opção ao Lado: "))
                    if statuspedido == 1:
                        aprovação = f"O pedido de Visita foi {fila[count]} Aprovado!"
                        try:
                            with open('C:\\Users\\Darth Kaida\\Desktop\\Programação\\Python\\Projeto Museu\\RegistroDeVisitas.txt', 'a') as visitfile:
                                visitfile.write(aprovação)
                            
                        except FileNotFoundError as e:
                            print("Error: O Arquivo 'RegistroDeVisitas.txt' Não Foi Encontrado, Verifique Manualmente.")
                        
                        except Exception as e:
                            print("Error: Algo de Errado não está certo...")

                        else:
                            count+=1

                    if statuspedido == 2:
                        aprovação = f"O pedido de Visita foi {fila[count]} Rejeitado!"
                        try:
                            with open('C:\\Users\\Darth Kaida\\Desktop\\Programação\\Python\\Projeto Museu\\RegistroDeVisitas.txt', 'a') as visitfile:
                                visitfile.write(aprovação)
                            
                        except FileNotFoundError as e:
                            print("Error: O Arquivo 'RegistroDeVisitas.txt' Não Foi Encontrado, Verifique Manualmente.")
                        
                        except Exception as e:
                            print("Error: Algo de Errado não está certo...")

                        else:
                            count+=1
            except Exception as e:
                print("Error: Algo de Errado não está certo...")

                                                ###########################################################################################
        elif asw == 6:
            end = True


    main()



def menuUsuários():
    global fila
    asw = 0
    end = False
    fila = []
    while end != True:
        print("\n \n __________MENU DOS USUÁRIOS__________ \n  \n")                             #################### MENU USUÁRIOS ######################
        print(f"Olá {nomeusuário}! O que deseja fazer? \n 1- Ver artistas e suas obras \n 2- Pesquisar Obras por Artistas \n 3- Solicitar Visita \n 4- Sair")

        asw = int(input("Digite ao Lado sua escolha: "))
        if asw == 1:
            print("\n \n Artistas e suas Obras: \n")
            for nome_artista, detalhes_artista in artistas.items():
                print(f"Artista: {nome_artista}")
                print("Obras:")
                for obra in detalhes_artista[-1]:
                    print(f"  - {obra[0]}")
                print("\n")
            
            time.sleep(3)

        elif asw == 2:
            print("\n \n Os Artistas No sistema são: ")
            for nome in artistas.keys():
                print(nome)
            nome_artista = input("\n Digite o Nome do Artista para ver as suas obras: ")
            if nome_artista in artistas.keys():
                print(f"\n \n As Obras do Artista {nome} no sistema são {artistas[nome_artista][-1]}.")
        
        elif asw == 3:
            lugarnafila = random.randint(sum(fila) +1,len(fila) +11)
            nomeprafila = input("Digite o seu nome para fila: ")
            emailprafila = input("Digite o seu email para o pedido de visita: ")
            temaprafila = input("Digite o tema do pedido de visita: ")
            descricaoprafila = input("Digite a descrição pro pedido de visita: ")
            obrasparavisitar = input("Digite as obras que deseja visitar (separados por vírgula): ").split(',')
            pedidodevisita = [lugarnafila, nomeprafila, emailprafila, temaprafila, descricaoprafila, obrasparavisitar]
            fila.append(pedidodevisita)
            bubble_sort(fila)
            print("Pedido Enviado com Sucesso! Aguarde o Retorno em seu Email em caso de Aprovação.")

        elif asw == 4:
            end = True    
        
    main()


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][0] > lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]



if __name__ == "__main__":
    main()


