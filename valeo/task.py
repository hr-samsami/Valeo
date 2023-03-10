import uuid

class Task:
    def __init__(self, project_id):
        self.id = str(uuid.uuid4())
        self.project_id = project_id
     