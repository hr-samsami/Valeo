import time
import random
from typing import List
from .task import Task
from .val_resource import Resource
from .project import Project
from .producer import Producer

class Scheduler:
    resources: List[Resource] = []
    projects: List[Project] = []
    tasks: List[Task] = []
    
    def __init__(self, num_resources, num_projects):
        self.resources = [Resource(i) for i in range(num_resources)]
        self.projects = [Project(i, f"project-{i}") for i in range(num_projects)]
        
    def run(self):
        current_time = 0
        while True:
            if tasks := Producer.check_for_new_task(self.projects):
                self.tasks.extend(tasks)
                self.process_tasks(current_time)
            current_time += 1
            time.sleep(1) # assume one second per iteration
        
    def process_tasks(self, current_time):
        for resource in self.resources:
            if resource.is_available(current_time) and resource.task is not None:
                resource.release_task(current_time)
                
        if available_resources := [
            resource
            for resource in self.resources
            if resource.is_available(current_time)
        ]:
            while self.tasks and available_resources:
                selected_resource = available_resources.pop(0)
                selected_task = self.tasks.pop(0)
                selected_resource.assign_task(selected_task, current_time)
                