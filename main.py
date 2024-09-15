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