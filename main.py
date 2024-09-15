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