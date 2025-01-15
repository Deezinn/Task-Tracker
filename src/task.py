from time import gmtime, strftime

class Task:
    def __init__(self):
        self.tasks = []


    def addTask(self):

        task = {}
        id_task = 1
        descricao_task = str(input("Digite a descrição da Task: "))
        status_task = str(input("Digite o status da task: "))
        created_at = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        updated_at = None

        task['id'] = id_task
        task['Descrição'] = descricao_task
        task['Status_task'] = status_task
        task['Created_at'] = created_at
        task['Updated_at'] = updated_at

        self.tasks.append(task)
        print(self.tasks)







    # def updateTask(self):


    # def delTask(self):


task = Task()
task.addTask()
