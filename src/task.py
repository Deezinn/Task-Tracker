from datetime import datetime

class Task:
    def __init__(self):
        self.tasks = []

    def get_all_tasks(self):  # Lista todas as tarefas
        for tasks in self.tasks:
            print(tasks)

    def get_completed_tasks(self):  # Lista tarefas concluídas
        for tasks in self.tasks:
            if tasks['status'] == 'done':
                print(tasks)

    def get_pending_tasks(self):  # Lista tarefas pendentes
        for tasks in self.tasks:
            if tasks['status'] == 'todo':
                print(tasks)

    def get_in_progress_tasks(self):  # Lista tarefas em andamento
        for tasks in self.tasks:
            if tasks['status'] == 'in-progress':
                print(tasks)

    def add_task(self):  # Adiciona uma nova tarefa
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

    def update_task(self):  # Atualiza uma tarefa existente
        task_a_modificar = int(input("Digite o id da task que deseja modificar: "))
        nova_descricao = input("Digite a nova descrição: ")
        for tasks in self.tasks:
            if tasks['id'] == task_a_modificar:
                tasks['description'] = nova_descricao

    def delete_task(self):  # Remove uma tarefa
        task_a_deletar = int(input("Digite o id da task que deseja deletar: "))
        for tasks in self.tasks:
            if tasks['id'] == task_a_deletar:
                tasks.clear()

task = Task()
count = 0
while True:
    task.add_task()
    count += 1
    if count > 2:
        break
task.get_completed_tasks()
task.update_task()
task.get_all_tasks()
task.delete_task()
task.get_all_tasks()
