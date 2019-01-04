import StrategyPattern.pattern_classes.Engineer as Engineer
import StrategyPattern.pattern_classes.Triangle as Tri
import StrategyPattern.pattern_classes.Rectangle as Rect


engineer = Engineer.Engineer(10, 20, Tri.Triangle).calculate()
print(engineer)
engineer = Engineer.Engineer(10, 20, Rect.Rectangle).calculate()
print(engineer)