class EquationSolver():

    def second_degree_equation_solver(self, var_a, var_b, var_c):
        if type(var_a) not in [int, float] or type(var_b) not in [int, float] or type(var_c) not in [int, float]:
            raise TypeError('Int or float only.')

        d = (var_b * var_b) - (4 * var_a * var_c)
        if d < 0:
            return None, None
        sqrtd = d ** 0.5
        return (-var_b + sqrtd) / 2 / var_a, (-var_b - sqrtd) / 2 / var_a