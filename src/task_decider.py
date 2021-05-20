def get_preferred_option(task1, task2):
    if task2.description in task1.lookup[task1.description]:
        return task1.description
    return task2.description

