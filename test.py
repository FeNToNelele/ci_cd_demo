#https://docs.python.org/3/library/unittest.html
import unittest
from seconddegreeequationsolver import second_degree_equation_solver

class testEquationSolverClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        #Building up the test environment
        print("setUp test class")
        self.tst = EquationSolver()

    @classmethod
    def tearDown(self):
        #Garbage collection
        print("tearDown.")

    def test_secondDegreeEquation_case_for_solutions(self):
        print("running test 1")
        self.assertEqual(self.tst.secondDegreeEquationSolver(1, 2, 8), (None, None), msg="D<0 hiba")
        print("running test 2")
        self.assertEqual(self.tst.secondDegreeEquationSolver(1, -14, 49), (7, 7), msg="D=1 hiba")
        print("running test 3")
        self.assertEqual(self.tst.secondDegreeEquationSolver(1, 6, 8), (-2, -4), msg="D=2 hiba")

    #TypeError visszadobásának tesztelése
    def test_secondDegreeEquation_case_TypeError(self):
        print("running TypeError test")
        with self.assertRaises(TypeError):
            result = self.tst.secondDegreeEquationSolver(True, 2, 4)

if __name__ == '__main__':
    unittest.main()
