class Numbers:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        self.divisor = None
        self.result = None
        self.numbers = []

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def working_merge_lists_sorted(self):
        pt1 = 0
        pt2 = 0
        result = []
        while(pt1 < len(self.a) and pt2 < len(self.b)):
            if self.a[pt1] < self.b[pt2]:
                result.append(self.a[pt1])
                pt1 += 1
            else:
                result.append(self.b[pt2])
                pt2 += 1
        
        for i in range(pt1, len(self.a)):
            result.append(self.a[pt1])
        
        for i in range(pt2, len(self.b)):
            result.append(self.b[pt2])
        return result

    def divison(self):
        return self.a / self.b
        return result
    
    def wrong_merge_lists_sorted(self):
        pt1 = 0
        pt2 = 0
        result = []
        while(pt1 < len(self.a) and pt2 < len(self.b)):
            if self.a[pt1] < self.b[pt2]:
                result.append(self.b[pt1])
                pt1 += 1
            else:
                result.append(self.b[pt2])
                pt2 += 1
        
        for i in range(pt1, len(self.a)):
            result.append(self.a[pt1])
        
        for i in range(pt2, len(self.b)):
            result.append(self.b[pt2])

        return result
    
    def get_total_sum(self):
        return sum(self.a) + sum(self.b)
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
