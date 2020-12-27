class Numbers:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        self.divisor = None
        self.result = None
        self.numbers = []

    def add(self):
        return self.a + self.b

    def divison(self):
        return self.a / self.b

    def divisonDecision(self):
        if self.divisor == "zero":
            return "skip"
        else:
            return "complete"

    def getMax(self):
        self.result = max(self.numbers)

    def getMin(self):
        self.result = min(self.numbers)

    def factorial(self):
        if self.a == 0:
            self.result = 1
            return
        else:
            result = 1
            for i in range(self.a):
                result = result * (i + 1)
            self.result = result
