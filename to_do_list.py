#lista de tarefas
import os
import datetime

class Tarefa:
    def __init__(self, nome=None, prazo=None, status="Pendente"):
        self.nome = nome
        self.prazo = prazo
        self.status = status

    def alterar_status(self):
        
        if self.status == "Pendente":
            self.status = "Concluida"
            self.nome = f"[ ✅ ] {self.nome} "
        elif self.status == "[ ❌ ] Não Concluida":
            self.status = "Concluida"
            self.nome = f"[ ✅ ] {self.nome}"
        else:
            self.status = "Pendente"

    def checar_concluida(self):

        if self.prazo and datetime.datetime.now() > self.prazo and self.status == "Pendente":
            self.status = f"[ ❌ ] Não Concluida"

    def __str__(self):
        prazo_str = self.prazo.strftime("%d-%m-%Y %H:%M") if self.prazo else "Sem Prazo"
        return f'''
Tarefa: {self.nome}
Status: {self.status} 
Prazo: {prazo_str}'''
    
class ListaTarefa:
    def __init__(self):
        self.lista = []

    
    def adicionar_tarefa(self):
        print(f"""
{'=' * 30}
{'Adicionar Tarefa'.center(30)}
{'=' * 30}
""")
        print("[0] -> Retornar ao Menu: \n")

        
        try:
            data_f = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            tarefa = input("Digite a tarefa Aqui: ")
            prazo_str = input("Digite o prazo: ()")

            prazo = datetime.datetime.strptime(prazo_str, "%d-%m-%Y %H:%M") 

            if prazo_str:
                if prazo_str < data_f:
                    print(f"O Prazo {prazo_str} já passou.")
                    input()
                    return
                
                print(f"Prazo defino para {prazo}")
            else:
                print(f"Nenhum prazo definido: ")

            if tarefa == "0":
                return
            nova_tarefa = Tarefa(tarefa, prazo)
            self.lista.append(nova_tarefa)
            print(nova_tarefa)

            input("[Enter] -> Retornar ao Menu: ")
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido: ")
            input("[Enter] -> Retornar ao Menu: ")

    def marcar_concluida(self):
        print(f"""
{'=' * 30}
{'Marcar Como Concluida'.center(30)}
{'=' * 30}
""")

        self.ver_lista()
        print("\n[0] -> Retornar ao Menu\n")
        try:
            escolha = int(input("Selecione: "))

            if 1 <= escolha <= len(self.lista):
                tarefa_conc  = self.lista[escolha - 1]
                tarefa_conc.alterar_status()
                
            elif escolha == 0:
                return
            
            input("[Enter] -> Retornar ao Menu: ")

        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido:")

    def remover_tarefa(self):
        print(f"""
{'=' * 30}
{'Remover Tarefa'.center(30)}
{'=' * 30}
""")
        self.ver_lista()
        print(f"\n[0] -> Retornar ao Menu: \n")
        try:
            escolha = int(input("Selecione: "))

            if 1 <= escolha <= len(self.lista):
                remover_tarefa  = self.lista[escolha - 1]
                print(f"A tarefa {remover_tarefa.nome} foi Removida com Sucesso!")
                del self.lista[escolha - 1]

            elif escolha == 0:
                return
            
            input("[Enter] -> Retornar ao Menu: ")
        except (ValueError, TypeError):
            print("ERROR, Digite um valor válido")

    def ver_lista(self):
        if not self.lista:
            print("Nenhuma Tarefa Adicionada a lista")

        for i, tarefa in enumerate(self.lista, start=1):
            tarefa.checar_concluida()
            print(f'''
{'-' * 30}
ID: [{i}]{tarefa}''')

            print('-' * 30)
    
    def editar_lista(self):
        print(f"""
{'=' * 30}
{'Editar Tarefa'.center(30)}
{'=' * 30}
""")
        
        self.ver_lista()
        print("\n[0] -> Retornar ao Menu: \n")

        try:
            escolha = int(input("Selecione: "))
        
            if 1 <= escolha <= len(self.lista):
                editar_tarefa = self.lista[escolha - 1]
                editar_tarefa.nome = input("Digite um novo título para tarefa: ")
                prazo_str = input("Digite o Novo Prazo: ")

                prazo = datetime.datetime.strptime(prazo_str, "%d-%m-%Y %H:%M")
                editar_tarefa.prazo = prazo
                
            elif escolha == 0:
                return
            
            input("[Enter] -> Retornar ao Menu: ")
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido: ")

def main():
    lista_tarefa = ListaTarefa()
    tarefa = Tarefa()
    while True:
        try:
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
            tarefa.checar_concluida()

            opcao = int(input("Selecione uma opção: "))


            if opcao == 1:  
                os.system('cls')    
                lista_tarefa.adicionar_tarefa()
            elif opcao == 2:
                os.system('cls') 
                lista_tarefa.marcar_concluida()
            elif opcao == 3:
                os.system('cls') 
                lista_tarefa.remover_tarefa()
            elif opcao == 4:
                os.system('cls') 
                lista_tarefa.editar_lista()
            elif opcao == 5:
                os.system('cls')
                print(f"""
    {'=' * 30}
    {'Ver Lista'.center(30)}
    {'=' * 30}""")
                lista_tarefa.ver_lista()
                input("\n[Enter] -> Retornar ao Menu: ")
            else:
                break
        except (ValueError, TypeError):
            print("ERRO: Digite um valor válido")
            input("[Enter] -> Retornar ao Menu: ")
if __name__ == "__main__":
    main()

    