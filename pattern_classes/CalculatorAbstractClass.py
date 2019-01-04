from abc import ABC, abstractmethod


class CalculatorAbstractClass(ABC):
    @abstractmethod
    def calculate(self, width, height):
        raise NotImplementedError("You must implement calculate() method")