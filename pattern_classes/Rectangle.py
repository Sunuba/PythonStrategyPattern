import StrategyPattern.pattern_classes.CalculatorAbstractClass as calc_abs_class


class Rectangle(calc_abs_class.CalculatorAbstractClass):
    def calculate(self, width, height):
        return width*height
