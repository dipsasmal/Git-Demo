class calculator:
    num = 20


    def sum(self,a,b):
        self.firstNum = a
        self.secondNum = b
        return self.firstNum + self.secondNum + self.num

obj = calculator()
obj1 = calculator()

print(obj.sum(2,4))
print(obj1.sum(6,7))


