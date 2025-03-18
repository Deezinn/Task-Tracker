import os


from task import Task

class Menu:
    def __init__(self):
        self.Task = Task()

    def opcoes(self):
        print("---------------------------------")
        print("Bem vindo a to-do list")
        print("---------------------------------")


    def escolhas(self):
        os.system('cls || clear')
        self.opcoes()
        print("Escolha alguma das opções abaixo:\n")
        print("Listar todas as tasks [1]")
        print("Listar tasks concluídas [2]")
        print("Listar tasks pendentes [3]")
        print("Listar tasks em progresso [4]")
        print("Adicionar task [5]")
        print("Modificar task [6]")
        print("Deletar task [7]")
        print("Sair [8]\n")
        while True:
            escolha = int(input("Digite a sua opção: "))
            match escolha:
                case 1:
                    self.Task.get_all_tasks()
                case 2:
                    self.Task.get_completed_tasks()
                case 3:
                    self.Task.get_pending_tasks()
                case 4:
                    self.Task.get_in_progress_tasks()
                case 5:
                    self.Task.add_task()
                case 6:
                    self.Task.update_task()
                case 7:
                    self.Task.delete_task()
                case 8:
                    break
                case _:
                    print("opção invalida")


menu = Menu()
menu.escolhas()
