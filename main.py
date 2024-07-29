from database import Tarefa, conectar_banco
from datetime import datetime
import os

def criar_tarefa():
    os.system('cls')
    print(f"""
{'=' * 30}
{'Adicionar Tarefa'.center(30)}
{'=' * 30}
""")
    
    print("[0] Retornar ao Menu\n")
    try:
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        nome = input("Digite o nome da Tarefa: ")

        if nome == "0":
            return
        prazo_str = input("Digite o prazo da tarefa em ((formato: DD/MM/YYYY HH:MM): ")

        if prazo_str:
            if prazo_str < data_atual:
                print('-' * 30)
                print("O Prazo Já se Expirou: \n")
                input("\n[Enter] -> Retornar ao Menu: ")
                return

            prazo = datetime.strptime(prazo_str, "%d/%m/%Y %H:%M")

        else:
            print('-' * 30)
            prazo = "Sem Prazo"
            print("\nPrazo não foi adicionado")
            print('-' * 30)
        nova_tarefa = Tarefa.create(Nome=nome, Prazo=prazo)
        
        print(f"\nTarefa: {nome} Foi Adicionado Com Sucesso")

        input("[Enter] -> Retornar ao Menu: ")
    except (ValueError ,TypeError):
        print("ERROR: Digite um valor válido: ")
        input("[Enter] -> Retornar ao Menu: ")

def checar_concluida():
    tarefas = Tarefa.select()
    if tarefas is True:
        for tarefa in tarefas:
            if tarefa.Prazo and datetime.now() > tarefa.Prazo and tarefa.Status == "Pendente":
                tarefa.Status = "Não Concluido"
                tarefa.save()
    else:
        return

def marcar_concluida():
    os.system('cls')
    tarefas = Tarefa.select()
    print(f"""
{'=' * 30}
{'Marcar Como Concluida'.center(30)}
{'=' * 30}
""")
    ver_tarefa()
    print("[0] Retornar ao Menu\n")
    print('-' * 30)

    try:
        n = int(input("Selecione: "))

        if 1 <= n <= len(tarefas):
            conc = tarefas[n - 1]
            
            if conc.Status == "Pendente" or conc.Status == "[❌]Não Concluido":
                conc.Status = "[✅]Concluido"
                print(f"\nA Tarefa {conc.Nome} Foi Marcada como Concluida\n")

            else:
                conc.Status = "Pendente"

            conc.save()
            input("[Enter] -> Retornar ao Menu")
        elif n == 0:
            return
        
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido: ")
        input("[Enter] -> Retornar ao Menu")

def remover_tarefa():
    os.system('cls')
    tarefas = Tarefa.select()
    print(f"""
{'=' * 30}
{'Remover Tarefa'.center(30)}
{'=' * 30}
""")
    ver_tarefa()
    print("[0] Retornar ao Menu\n")
    try:
        n = int(input("Selecione: "))

        if 1 <= n <= len(tarefas):
            tarefa_removida = tarefas[n - 1]
            print(f"A tarefa {tarefa_removida.Nome} Foi Removida")
            tarefa_removida.delete_instance()
        elif n == 0:
            return
        input("[Enter] -> Retornar ao Menu: ")
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")
        input("[Enter] -> Retornar ao Menu: ")


def ver_tarefa():

    tarefas = Tarefa.select()
    checar_concluida()
    if not tarefas:
        print("Nenhum Tarefa Encontrada")

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"""{'-' * 30}
ID: [{i}]
Tarefa: {tarefa.Nome}
Status: {tarefa.Status}
Prazo: {tarefa.Prazo}""")
    print('-' * 30)
        

def editar_tarefa():
    os.system('cls')
    tarefas = Tarefa.select()
    print(f"""
{'=' * 30}
{'Editar Tarefa'.center(30)}
{'=' * 30}
""")
    ver_tarefa()
    print("[0] Retornar ao Menu\n")
    try:
        n = int(input("Selecione: "))

        if 1 <= n <= len(tarefas):
            editar = tarefas[n - 1]
            
            editar.Nome = input("Digite um novo nome para tarefa: ")
            editar.Prazo = input("Digite um novo prazo: ")

            print(f"Tarefa Atualizada {editar.Nome}")
            editar.save()
            input("[Enter] -> Retornar ao Menu: ")
        elif n == 0:
            return
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido: ")
        input("[Enter] -> Retornar ao Menu: ")

def main():
    conectar_banco()
    while True:
        os.system('cls')
        print(f"""
{'=' * 30}
{'Lista de Tarefas'.upper().center(30)}
{'=' * 30}

[1] Adicionar Tarefa
[2] Marcar Tarefa como Concluida
[3] Remover Tarefa
[4] Editar Tarefa
[5] Ver Tarefa

[0] Sair
""")
        opcao = int(input("Escolha: "))

        if opcao == 1:
            criar_tarefa()
        elif opcao == 2:
            marcar_concluida()
        elif opcao == 3:
            remover_tarefa()
        elif opcao == 4:
            editar_tarefa()
        elif opcao == 5:
            os.system('cls')
            print(f"""
{'=' * 30}
{'Ver Lista'.center(30)}
{'=' * 30}""")
            ver_tarefa()
            input("\n[Enter] -> Retornar ao Menu: ")
        elif opcao == 0:
            print("Obrigado por acessar a lista de Tarefas")
            break

main()

