import sys
from scheduler import Scheduler

if __name__ == "__main__":
    num_resources = 10
    num_projects = 10
    scheduler = Scheduler(num_resources, num_projects)
    scheduler.run()
    