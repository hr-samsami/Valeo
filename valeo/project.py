from typing import List
from .task import Task


class Project:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.tasks: List[Task] = []

    @classmethod
    def create_projects(cls, num: int = 1) -> List['Project']:
        return [cls(i, f"project-{i}") for i in range(num)]

    def __str__(self) -> str:
        return self.name
