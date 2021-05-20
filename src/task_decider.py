def get_preferred_option(task1, task2):
    if task1 == task2:
        return task1.description
    
    task_holder = [task1.description, task2.description]
    if task_holder.count("wash dishes") > 0:
        if task_holder.count("cook dinner") > 0:
            return "wash dishes"
        else:
            return "clean windows"
    
    return "cook dinner"

