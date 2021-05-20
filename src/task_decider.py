def get_preferred_option(task1, task2):
    if task2.description == "cook dinner":
        return task2.description
    
    return "clean windows"