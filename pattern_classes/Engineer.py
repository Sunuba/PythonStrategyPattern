class Engineer:
    def __init__(self, height, width, method):
        self.method = method
        self.height = height
        self.width = width

    def calculate(self):
        return self.method().calculate(self.width, self.height)