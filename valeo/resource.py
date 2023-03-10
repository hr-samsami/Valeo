import random

class Resource:
    
    def __init__(self, id):
        self.id = id
        self.task = None
        self.busy_until = 0
        
    def is_available(self, current_time):
        return self.busy_until <= current_time
    
    def assign_task(self, task, current_time):
        self.task = task
        self.busy_until = current_time + random.randint(1, 60) # assume task takes 1-60 seconds to complete
        print(f"Resource {self.id} started task for project {task.project} at time {current_time}")
        
    def release_task(self, current_time):
        print(f"Resource {self.id} finished task for project {self.task.project} at time {current_time}")
        self.task = None
        self.busy_until = 0