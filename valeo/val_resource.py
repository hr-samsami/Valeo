import random
from typing import List


class Resource:

    def __init__(self, id):
        self.id = id
        self.task = None
        self.busy_until = 0

    @classmethod
    def create_resources(cls, num: int = 1) -> List['Resource']:
        return [cls(i) for i in range(num)]

    def is_available(self, current_time):
        return self.busy_until <= current_time

    def assign_task(self, task, current_time):
        self.task = task
        self.busy_until = current_time + random.randint(1, 60)  # assume task takes 1-60 seconds to complete
        print(f"Resource {self.id} started task for project {task.project_id} at time {current_time}")

    def release_task(self, current_time):
        print(f"Resource {self.id} finished task for project {self.task.project_id} at time {current_time}")
        self.task = None
        self.busy_until = 0
