print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def entrada():

    print('1. Cadastrar restaurante \n')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    print("Erro de digitação \n");
    opcao_voltar = input("Aperte 1 para voltar: \n")
    if opcao_voltar == 1:
        entrada()

opcao_escolhida = input('Escolha uma opção: \n')
if opcao_escolhida == '1':
    nome_do_restaurante = input('Digite o nome do restaurante: \n')
    if nome_do_restaurante == '':
        nome_do_restaurante = nome_do_restaurante
elif opcao_escolhida == '2':
    print(f"Nome de restaurantes cadastrados: \n")
elif opcao_escolhida == '3':
    print("Ativando restaurante..")
elif opcao_escolhida == '4':
    print("Saindo..")
else:
    finalizar_app()