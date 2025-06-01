def adicionar_tarefa(lista_de_tarefas,tarefa):
    """Adiocionar nova tarefa a uma lista pré-existente"""
    lista_de_taferas.append(tarefa)
    print("--> Tarefa adicionada com sucesso!")
    return lista_de_taferas

def listar_terefas(lista_de_tarefas):
    """Exibe lista de tarefas numerada"""
    print('\n')
    print("-" * 50)
    print(f"{' ' * 15}Lista de Tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_taferas:
        print(f"{n} - {tarefa}")
        n += 1
    print("-" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Deleta tarefa de uma lista pré-existente a partir do numero dela"""
    lista_de_taferas.pop((tarefa - 1))
    return lista_de_taferas

def exibir_menu():
    """Exibe menu com opções para o usuario escolher"""
    print("-" * 50)
    print("Escolha uma opção:\n" \
        "1 - Escolha uma nova tarefa\n"
        "2 - Listar tarefas\n" \
        "3 - Deletar tarefa\n" \
        "4 - Sair"
    )
    print('-' * 50)
    print('\n')

#Inicialização de variáveis
lista_de_taferas = []
continuar = True

# Cabeçalho do programa
print("-" * 50)
print("Bem-vindos à sua lista de Tarefas!")
print("-" * 50)

# Loop principal
while continuar:
    exibir_menu()
    opcao = input('Insira o que deseja fazer: ')

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_taferas = adicionar_tarefa(lista_de_taferas, tarefa)
    elif opcao == "2":
        listar_terefas(lista_de_taferas)
    elif opcao == "3":
        # A validação verifica se o valor é númerico, se é menor do que o limite da lista ou maior que zero
        tarefa = input('Insira o numero da tarefa que deseja deletar: ')
        if not tarefa.isnumeric():
            print("Número invalido! Tente novamente.")
        if int(tarefa) > len(lista_de_taferas):
            print("Número invalido! Tente novamente.")
        elif int(tarefa) <= 0:
            print("Número invalido! Tente novamente.")
        else:
            deletar_tarefa(lista_de_taferas,int(tarefa))
    elif opcao == "4":
            continuar = False
else:
    print("Opção Invalida! Por favor tente novamente.")
print('\n')