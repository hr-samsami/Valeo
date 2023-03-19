from .scheduler import Scheduler
from typing import List
from .val_resource import Resource
from .project import Project



if __name__ == "__main__":
    num_resources = 5
    num_projects = 10
    resources = Resource.create_resources(num_resources)
    projects = Project.create_projects(num_projects)
    scheduler = Scheduler(resources, projects)
    scheduler.run()
    