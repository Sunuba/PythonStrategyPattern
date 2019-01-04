import StrategyPattern.pattern_classes.CalculatorAbstractClass as calc_abs_class


class Triangle(calc_abs_class.CalculatorAbstractClass):
    def calculate(self, width, height):
        return 1/2*width*height
