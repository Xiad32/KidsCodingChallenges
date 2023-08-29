
import random
import unittest
from Problem_Division import DivisionProblem


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.problem = DivisionProblem()
        self.num1, self.num2 = self.generate_num1_num2(False)


    def test_problem_a_no_remainder(self):     
        self.num1 = self.make_divisable(self.num1, self.num2)
        result_computed, remainder_computed = DivisionProblem.divideNumbers(self.num1, self.num2)
        result_actual, remainder_actual = self.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )
     
    def test_problem_a_no_restrictions(self):
        result_computed, remainder_computed = DivisionProblem.divideNumbers(self.num1, self.num2)
        result_actual, remainder_actual = self.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )

    def test_problem_b_no_remainder(self):
        self.num1 = self.make_divisable(self.num1, self.num2)
        result_computed, remainder_computed = DivisionProblem.divideNumbersIteratively(self.num1, self.num2)
        result_actual, remainder_actual = self.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )
     
    def test_problem_b_no_restrictions(self):
        
        self.num1 = self.make_divisable(self.num1, self.num2)
        result_computed, remainder_computed = DivisionProblem.divideNumbersIteratively(self.num1, self.num2)
        result_actual, remainder_actual = self.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )

    def generate_num1_num2():
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        return num1, num2

    def make_divisable(num1, num2):
        num1 -= num1 % num2
        return num1
    
    def computeActuals(num1, num2):
        result_actual = num1 / num2
        remainder_actual = num1 % num2
        return result_actual, remainder_actual
