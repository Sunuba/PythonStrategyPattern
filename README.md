# Strategy Pattern in Python

__In our PHP version we implemented area calculator,
we will do the same with Python.__

Python supports multiple inheritance, that is why interface is not used
in python(Actually, you can use interfaces in python, but we will not).

We will replace interface with abstract class. We will create a 
CalculatorAbstractClass:

    from abc import ABC, abstractmethod

    class CalculatorAbstractClass(ABC):
        @abstractmethod
        def calculate(self, width, height):
            raise NotImplementedError("You must implement calculate() method")

Then we create Rectangle and Triangle classes. We will create Engineer
to use calculator to calculate the area :)


    import StrategyPattern.pattern_classes.Engineer as Engineer
    import StrategyPattern.pattern_classes.Triangle as Tri
    import StrategyPattern.pattern_classes.Rectangle as Rect
    
    
    engineer = Engineer.Engineer(10, 20, Tri.Triangle).calculate()
    print(engineer)
    engineer = Engineer.Engineer(10, 20, Rect.Rectangle).calculate()
    print(engineer)

The result will be:
    
    100.0
    200


>I have done a lot of research before implementing this, I have checked a
lot of code samples and at the end decided that my way is easier to
understand. I tried to seriously implement the easiest way to achieve
the same result that I achieved in PHP version of this pattern. 