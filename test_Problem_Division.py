
import random
import unittest
from Problem_Division import DivisionProblem


class TestDivisitionProblem(unittest.TestCase):
    def setUp(self) -> None:
        pass


    def test_problem_a_no_remainder(self):   
        self.num1, self.num2 = TestDivisitionProblem.generate_num1_num2(True)  
        result_computed, remainder_computed = DivisionProblem.divideNumbers(self.num1, self.num2)
        result_actual, remainder_actual = TestDivisitionProblem.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )
     
    def test_problem_a_no_restrictions(self):
        self.num1, self.num2 = TestDivisitionProblem.generate_num1_num2(False)  
        result_computed, remainder_computed = DivisionProblem.divideNumbers(self.num1, self.num2)
        result_actual, remainder_actual = TestDivisitionProblem.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )

    def test_problem_b_no_remainder(self):
        self.num1, self.num2 = TestDivisitionProblem.generate_num1_num2(True)    
        result_computed, remainder_computed = DivisionProblem.divideNumbersIteratively(self.num1, self.num2)
        result_actual, remainder_actual = TestDivisitionProblem.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )
     
    def test_problem_b_no_restrictions(self):
        self.num1, self.num2 = TestDivisitionProblem.generate_num1_num2(False)  
        result_computed, remainder_computed = DivisionProblem.divideNumbersIteratively(self.num1, self.num2)
        result_actual, remainder_actual = TestDivisitionProblem.computeActuals(self.num1, self.num2)        
        self.assertEqual(
            result_actual, result_computed
        )
        self.assertEqual(
            remainder_actual, remainder_computed
        )

    def generate_num1_num2(divisable = True):
        num2 = random.randint(1, 1000)
        if divisable:
            divisor = random.randint(1, 10)
            num1 = num2 * divisor
        else:
            num1 = random.randint(1, 1000)
        return num1, num2
    
    def computeActuals(num1, num2):
        result_actual = num1 // num2
        remainder_actual = num1 % num2
        return result_actual, remainder_actual
