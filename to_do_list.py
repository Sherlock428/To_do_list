#Lista de Tarefas
import os 

def lista_tarefas():
    return []

def concluida():
    return []
def adicionar_tarefas(lista):
    try:
        os.system('cls')
        print(f"""
{'=' * 30}
{'Adicionar Tarefa'.center(30).upper()}
{'=' * 30}
""")
        nova_tarefa = {
            "titulo": input("Digite um título para tarefa: "),
            "descricao": input("Digite uma descrição para tarefa: ")
        }

        lista.append(nova_tarefa)
    except (ValueError, Exception):
        print("ERROR, Digite um valor válido")

def tarefa_concluida(lista, concluida):
    os.system('cls')
    print(f"""
{'=' * 30}
{'MARCAR COMO CONCLUIDA'.center(30)}
{'=' * 30}
""")
    ver_lista(lista)
    try:
        escolha = int(input("Seleciona:  "))

        if 1 <= escolha <= len(lista):
            tarefa_conc = lista[escolha - 1]
            concluida.append(tarefa_concluida)

            print(f"A tarefa {tarefa_conc} foi marcada como concluída ")
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")

def remover_tarefa(lista): 
    os.system('cls')
    print(f"""
{'=' * 30}
{'REMOVER TAREFA'.center(30)}
{'=' * 30}
""")
    ver_lista(lista)
    
    escolha = int(input("Selecione: "))

    if 1 <= escolha <= len(lista):
        tarefa_remover = lista[escolha - 1]
        print(f"A tarefa {tarefa_remover['titulo']} foi removida com sucesso")
        lista.pop(tarefa_remover)

def ver_lista(lista):
    if not lista:
        print("Nenhuma Tarefa Encontrada")
        print("\n[Enter] -> Retornar ao Menu\n")
        return
    
    for i, tarefa in enumerate(lista, start=1):
        print(f"[{i}] {tarefa['titulo']}")


def editar_tarefa(lista):
    os.system('cls')
    print(f"""
{'=' * 30}
{'EDITAR TAREFA'.center(30)}
{'=' * 30}
""")
    ver_lista(lista)

    
    escolha = int(input("Selecione:  "))

    if 1 <= escolha <= len(lista):
        lista[escolha - 1] = {"titulo": input("Digite um titulo: "),
                              "descricao": input("Digite uma descrição: ")}
        


def main():
    lista = lista_tarefas()
    lista_c = concluida()
    
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
""")
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                adicionar_tarefas(lista)
            elif opcao == 2:
                tarefa_concluida(lista, lista_c)
            elif opcao == 3:
                remover_tarefa(lista)
            elif opcao == 4:
                editar_tarefa(lista)
            elif opcao == 5:
                print(f"{'=' * 30}\n"
                      f"{'VER LISTA DE TAREFAS'.center(30)}\n"
                      f"{'=' * 30}\n")
                ver_lista(lista)
                input("[Enter] -> Retornar Menu")
            else:
                break
        except (ValueError, TypeError):
            print("ERROR, Escolha um valor válido")

main()