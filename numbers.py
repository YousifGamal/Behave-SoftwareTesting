class Numbers():
    def __init__(self,a,b):
        self.a = a
        self.b = b

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
