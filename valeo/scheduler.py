import time
from typing import List
from .task import Task
from .val_resource import Resource
from .project import Project
from .producer import Producer


class Scheduler:
    resources: List[Resource] = []
    projects: List[Project] = []
    tasks: List[Task] = []

    def __init__(self, resources: List[Resource], projects: List[Project]) -> None:
        self.resources = resources
        self.projects = projects

    def get_first_tasks(self) -> List[Task]:
        ts = []
        for project in self.projects:
            if project.tasks:
                ts.append(project.tasks.pop(0))
        return ts

    def run(self) -> None:
        current_time = 0
        while True:
            Producer.check_for_new_task(self.projects)
            if ts := self.get_first_tasks():
                self.tasks.extend(ts)
            self.process_tasks(current_time)
            current_time += 1
            time.sleep(1)  # assume one second per iteration

    def process_tasks(self, current_time):
        for res in self.resources:
            if res.is_available(current_time):
                if res.task is not None:
                    res.release_task(current_time)
                if self.tasks:
                    res.assign_task(self.tasks.pop(0), current_time)
