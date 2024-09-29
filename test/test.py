import pytest
from src.main import menu, adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa, tarefas
from unittest.mock import patch

#Teste do menu
def test_menu(capsys):
    # Chama a função que exibe o menu
    menu()
    
    # Captura a saída do print
    captured = capsys.readouterr()
    
    # Verifica se o menu foi impresso corretamente
    assert "\nMenu:" in captured.out
    assert "1. Adicionar tarefa" in captured.out
    assert "2. Listar tarefas" in captured.out
    assert "3. Marcar tarefa como concluída" in captured.out
    assert "4. Remover tarefa" in captured.out
    assert "5. Sair" in captured.out


# Função auxiliar para resetar a lista de tarefas antes de cada teste
@pytest.fixture(autouse=True)
def resetar_tarefas():
    global tarefas
    tarefas.clear()  # Limpa a lista de tarefas antes de cada teste

# Teste para a função de adicionar tarefa
@patch('builtins.input', return_value="Tarefa Teste")
def test_adicionar_tarefa(mock_input):
    adicionar_tarefa()
    assert len(tarefas) == 1
    assert tarefas[0]["nome"] == "Tarefa Teste"
    assert not tarefas[0]["concluida"]

# Teste para a função de listar tarefas com lista vazia
def test_listar_tarefas_vazia(capsys):
    listar_tarefas()
    captured = capsys.readouterr()
    assert "Nenhuma tarefa na lista." in captured.out

# Teste para a função de listar tarefas com tarefas adicionadas
def test_listar_tarefas(capsys):
    tarefas.append({"nome": "Tarefa Teste", "concluida": False})
    listar_tarefas()
    captured = capsys.readouterr()
    assert "1. Tarefa Teste [Pendente]" in captured.out

# Teste para a função de concluir tarefa
@patch('builtins.input', return_value="1")
def test_concluir_tarefa(mock_input):
    tarefas.append({"nome": "Tarefa Teste", "concluida": False})
    concluir_tarefa()
    assert tarefas[0]["concluida"]

# Teste para a função de concluir tarefa com índice inválido
@patch('builtins.input', return_value="5")
def test_concluir_tarefa_invalida(mock_input, capsys):
    tarefas.append({"nome": "Tarefa Teste", "concluida": False})
    concluir_tarefa()
    captured = capsys.readouterr()
    assert "Número inválido." in captured.out
    assert not tarefas[0]["concluida"]

# Teste para a função de remover tarefa
@patch('builtins.input', return_value="1")
def test_remover_tarefa(mock_input):
    tarefas.append({"nome": "Tarefa Teste", "concluida": False})
    remover_tarefa()
    assert len(tarefas) == 0

# Teste para a função de remover tarefa com índice inválido
@patch('builtins.input', return_value="5")
def test_remover_tarefa_invalida(mock_input, capsys):
    tarefas.append({"nome": "Tarefa Teste", "concluida": False})
    remover_tarefa()
    captured = capsys.readouterr()
    assert "Número inválido." in captured.out
    assert len(tarefas) == 1
