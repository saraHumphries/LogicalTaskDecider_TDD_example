class Task:
    def __init__(self, description):
        self.description = description
        self.lookup = {
            "wash dishes" : ["cook dinner", "wash clothes"],
            "cook dinner" : ["clean windows", "do ironing"],
            "clean windows" : ["wash dishes", "do ironing"],
            "do ironing" : ["wash clothes", "wash dishes"],
            "wash clothes" : ["cook dinner", "clean windows"]
        }

    



