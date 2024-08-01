# O programa deverá cadastrar infinitos usuário no sistema, Caso o usuário já esteja em uso, mande o cliente tentar novamente, o programa deverá efetuar o login com base nos usuários cadastrads. E encerrar o programa caso o cliente solicite.

#BIBLIOTECA
import os
import time
# AMAZENAR OS USUÁRIOS CADASTRADOS E SUAS RESPECTIVAS SENHAS
users = {}
#MENU INICIO
while True:
    print('1 - Cadastrar um novo usuário.\n2 - Efetuar o login.\n3 - Sair do programa.')
    opcao = str(input('Escolha uma das opçoes acima: '))
    print('Carregando o sistema...')
    time.sleep(1.5)
    os.system('clear')
#CADASTRAMENTO DE USUÁRIOS
    if opcao == '1':
        print('CADASTRO ESCOLHIDO')
        user = str(input('Insira o nome de usuário: '))
        if user in users:
            print('Usuário já existe! Tente novamente.')
        else:
            password = str(input('Insira sua senha: '))
            users[user] = password
            print('Cadastrando o usuário...')
            time.sleep(1.5)
            os.system('clear')
            print('Usuário cadastrado com sucesso!')
            time.sleep(1.5)
            os.system('clear')
# LOGIN
    elif opcao == '2':
        os.system('clear')
        print('LOGIN ESCOLHIDO')
        user = input('Insira o usuário: ')
        password = str(input('Insira sua senha: '))
        if user in users and users[user] == password:
            print('checando o banco de dados...')
            time.sleep(1.5)
            os.system('clear')
            print(f'Olá, {user}, Login efetuado com sucesso.')
            time.sleep(3)
            os.system('clear')
        else:
            os.system('clear')
            print('Usuário ou senha inválida!!!')
            time.sleep(1.5)
# O PROGRAMA SERÁ FINALIZADO.
    elif opcao == '3':
        print('Encerrando o programa...')
        os.system('clear')
        break
# OPÇÃO INVÁLIDA, USUÁRIO ESCOLHEU UM  NÚMERO UM INVÁLIDO.
    else:
        print('Nenhuma opção válida, tente novamente.')
        time.sleep(2)
        os.system('clear')
print('PROGRAMA FINALIZADO COM SUCESSO')
