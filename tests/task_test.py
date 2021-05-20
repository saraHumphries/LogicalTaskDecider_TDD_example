from src.task import Task
import unittest
from src.task_decider import get_preferred_option


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_clean_windows = Task("clean windows", 20)
        self.task_wash_dishes = Task("wash dishes", 10)
        self.task_cook_dinner = Task("cook dinner", 60)
    
    def test_task_has_description(self):
        self.assertEqual("clean windows", self.task_clean_windows.description)

    def test_task_has_duration(self):
        self.assertEqual(20, self.task_clean_windows.duration)


    def test_clean_window_chosen_over_wash_dishes(self):
        self.assertEqual("clean windows", get_preferred_option("clean windows", "wash dishes"))

    

    
