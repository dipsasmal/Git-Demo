class course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings

    def average(self):
        numberofratings=len(self.ratings)
        avg=sum(self.ratings)/numberofratings
        print("avrage rating of ", self.name , "is",avg)


c1=course('python corse',[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2=course('Java course',[2,3,4,5])
print(c2.name)
print(c2.ratings)
c2.average()