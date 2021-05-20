def get_preferred_option(task1, task2):
    if task1 == task2:
        return task1.description

    if task2.description in task1.beats:
        return task1.description
    return task2.description

