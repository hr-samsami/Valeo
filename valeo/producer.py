import random
from .task import Task


class Producer:
    @staticmethod
    def check_for_new_task(projects) -> None:
        num = random.randint(1, 60)
        if num < 10:
            for _ in range(num):
                project = random.choice(projects)
                project.tasks.append(Task(project.id))
            print(f"{num} New task added")
