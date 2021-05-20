def get_preferred_option(task1, task2):
    if task1 == task2:
        return task1.description


    if task1.beats == task2.description:
        return task1.description
    return task2.description

#     for task in tasks["tasks"]:
#         if task == task1:
#             if task["beats"] == task2:
#                 return task1.description
#             return task2.description



    
    
    
#     if task_holder.count("wash dishes") > 0:
#         if task_holder.count("cook dinner") > 0:
#             return "wash dishes"
#         else:
#             return "clean windows"
    
    
#     return "cook dinner"
    



# tasks = {
#     "tasks": [
#     {
#         "description" : "wash dishes",
#         "it_beats" : "cook dinner",
#         "loses_to" : "clean windows"

#     },

#     {
#         "description" : "cook dinner",
#         "it_beats" : "clean windows",
#         "loses_to" : "wash dishes"
#     },

#     {
#        "description" : "clean windows",
#         "it_beats" : "wash dishes",
#         "loses_to" : "cook dinner"
#     }]
    
# }

