import random
from scheduler import Scheduler
from task import Task

class Pipeline:
    @staticmethod
    def check_for_new_task():
        num = random.randint(1, 60)
        if num < 30:
            project = random.sample(Scheduler.projects)
            task = Task(project)
            project.tasks += [task]
            print(f"New task added for project {task.project}")
            return True
        return False
            