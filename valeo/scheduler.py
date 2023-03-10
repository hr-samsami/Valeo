import time
import random
from typing import List
from resource import Resource
from project import Project
from pipeline import Pipeline

class Scheduler:
    resources: List[Resource] = []
    projects: List[Project] = []
    
    def __init__(self, num_resources, num_projects):
        self.resources = [Resource(i) for i in range(num_resources)]
        self.projects = [[] for _ in range(num_projects)]
        
    def run(self):
        current_time = 0
        while True:
            Pipeline.check_for_new_task()
            if Pipeline.check_for_new_task():
                self.process_tasks(current_time)
            current_time += 1
            time.sleep(1) # assume one second per iteration
        
    def process_tasks(self, current_time):
        for project_tasks in self.projects:
            available_resources = [resource for resource in self.resources if resource.is_available(current_time)]
            if available_resources and project_tasks:
                selected_resource = random.choice(available_resources)
                selected_task = project_tasks.pop(0)
                selected_resource.assign_task(selected_task, current_time)
                if not project_tasks:
                    print(f"All tasks for project {selected_task.project} have been completed")
            for resource in self.resources:
                if not resource.is_available(current_time) and resource.task is not None and resource.task.project == selected_task.project:
                    resource.release_task(current_time)