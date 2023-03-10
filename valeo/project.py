class Project:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.tasks = []
    
    def __str__(self) -> str:
        return self.name    