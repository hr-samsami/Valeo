import random
from .task import Task

class Producer:
    @staticmethod
    def check_for_new_task(projects):
        num = random.randint(1, 60)
        if num < 10:
            tasks=[]
            for _ in range(num):
                project = random.choice(projects)
                tasks.append(Task(project.id))    
            print(f"{num} New task added")
            return tasks