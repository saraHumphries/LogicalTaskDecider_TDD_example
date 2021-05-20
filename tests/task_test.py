from src.task import Task
import unittest
from src.task_decider import get_preferred_option


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_clean_windows = Task("clean windows")
        self.task_wash_dishes = Task("wash dishes")
        self.task_cook_dinner = Task("cook dinner")
        self.task_wash_clothes = Task("wash clothes")
        self.task_do_ironing = Task("do ironing")
    
    def test_task_has_description(self):
        self.assertEqual("clean windows", self.task_clean_windows.description)

    


    def test_cw_over_wd(self):
        self.assertEqual("clean windows", get_preferred_option(self.task_clean_windows, self.task_wash_dishes))

    def test_cw_over_wd_2(self):
        self.assertEqual("clean windows", get_preferred_option(self.task_wash_dishes, self.task_clean_windows))


    def test_cd_over_cw(self):
        self.assertEqual("cook dinner", get_preferred_option(self.task_clean_windows, self.task_cook_dinner))

    def test_wd_over_cd__1(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_wash_dishes, self.task_cook_dinner))
    
    def test_wd_over_cd__2(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_cook_dinner, self.task_wash_dishes))

    def test_returns_task_if_tasks_same(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_wash_dishes, self.task_wash_dishes))
    
    # -----------
    # Extension 
    
    def test_wc_over_cw(self):
         self.assertEqual("wash clothes", get_preferred_option(self.task_clean_windows, self.task_wash_clothes))

    def test_di_over_wc(self):
        self.assertEqual("do ironing",get_preferred_option(self.task_do_ironing, self.task_wash_clothes))

    def test_di_over_wd(self):
        self.assertEqual("do ironing", get_preferred_option(self.task_wash_dishes, self.task_do_ironing))

    def test_wd_over_wc(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_wash_dishes, self.task_wash_clothes))
