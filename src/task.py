from datetime import datetime

class Task:
    def __init__(self):
        self.tasks = []

    def get_all_tasks(self):
        if not self.tasks:
            print("Não há tarefas registradas")
        else:
            for tasks in self.tasks:
                print(tasks)

    def get_completed_tasks(self):
        if not self.tasks:
            print("Não há tarefas registradas")
        ## atribuir um elif caso nao tenha task completadas
        else:
            for tasks in self.tasks:
                if tasks['status'] == 'done':
                    print(tasks)

    def get_pending_tasks(self):
        if not self.tasks:
            print("Não há tarefas registradas")
        ## atribuir um elif caso nao tenha task pendentes
        else:
            for tasks in self.tasks:
                if tasks['status'] == 'todo':
                    print(tasks)

    def get_in_progress_tasks(self):
        if not self.tasks:
            print("Não há tarefas registradas")
        ## atribuir um elif caso nao tenha task em progress
        else:
            for tasks in self.tasks:
                if tasks['status'] == 'in-progress':
                    print(tasks)

    def add_task(self):
        id = len(self.tasks)
        description = input("Digite a descrição da tarefa: ")
        status = int(input("Digite o status da tarefa 1 para (todo) 2 para (in-progress) 3 para (done): "))

        if status == 1:
            status = 'todo'
        elif status == 2:
            status = 'in-progress'
        elif status == 3:
            status = 'done'
        else:
            print("Nenhuma das opções foram selecionadas.")

        created_at = datetime.now().date()
        updated_at = None

        self.tasks.append({
            'id': id,
            'description': description,
            'status': status,
            'created_at': created_at,
            'updated_at': updated_at
        })

    def update_task(self):
        if not self.tasks:
            print("Não há tarefas registradas")
        else:
            status_ou_descricao = input("Deseja modificar o status ou a descrição da atividade? [status/descrição]")
            if status_ou_descricao == 'status':
                task_a_modificar = int(input("Digite o id da task que deseja modificar: "))
                novo_status = int(input("Digite o status da tarefa 1 para (todo) 2 para (in-progress) 3 para (done): "))

                if novo_status == 1:
                    novo_status = 'todo'
                elif novo_status == 2:
                    novo_status = 'in-progress'
                elif novo_status == 3:
                    novo_status = 'done'
                else:
                    print("Nenhuma das opções foram selecionadas.")

                for tasks in self.tasks:
                    if tasks['id'] == task_a_modificar:
                        tasks['status'] = novo_status
                        tasks['updated_at'] = datetime.now().date()

            elif status_ou_descricao == 'descrição':
                task_a_modificar = int(input("Digite o id da task que deseja modificar: "))
                nova_descricao = input("Digite a nova descrição: ")
                for tasks in self.tasks:
                    if tasks['id'] == task_a_modificar:
                        tasks['description'] = nova_descricao
                        tasks['updated_at'] = datetime.now().date()
            else:
                print("Você não digitou [status/descrição]")

    def delete_task(self):
        if not self.tasks:
            print("Não há tarefas registradas")
        else:
            task_a_deletar = int(input("Digite o id da task que deseja deletar: "))
            for tasks in self.tasks:
                if tasks['id'] == task_a_deletar:
                    tasks.clear()
