#ATP - DevOps - PUCPR
#Otavio Luigi Paiola

# Lista de tarefas vazia
tarefas = []

# Exibe o menu
def menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"nome": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada.")

# Função para listar tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i + 1}. {tarefa['nome']} [{status}]")

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    listar_tarefas()
    if tarefas:
        num = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]["concluida"] = True
            print(f"Tarefa '{tarefas[num]['nome']}' marcada como concluída.")
        else:
            print("Número inválido.")

# Função para remover uma tarefa
def remover_tarefa():
    listar_tarefas()
    if tarefas:
        num = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if 0 <= num < len(tarefas):
            removida = tarefas.pop(num)
            print(f"Tarefa '{removida['nome']}' removida.")
        else:
            print("Número inválido.")

# Programa principal
while True:
    menu()
    
    escolha = input("Escolha uma opção (1/2/3/4/5): ")

    if escolha == '1':
        adicionar_tarefa()
    
    elif escolha == '2':
        listar_tarefas()
    
    elif escolha == '3':
        concluir_tarefa()
    
    elif escolha == '4':
        remover_tarefa()
    
    elif escolha == '5':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")