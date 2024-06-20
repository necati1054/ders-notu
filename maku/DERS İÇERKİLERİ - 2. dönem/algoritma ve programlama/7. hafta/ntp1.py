class Car():    
    def __init__(self,name,color,years,sound,price=0):
        self.name=name
        self.color=color
        self.years=years
        self.sound=sound
        self.price=price
    
    def percentİncrease(self,ratio):
        before = self.price
        process = self.price*ratio/100
        after = before+process
        self.price=after 
        print(f"{self.name} is a new price = {self.price}")
        
    def bilgi():
        print("Car Class function")
        
        
class Insan(Car):
    def __init__(self,name,color,years,sound,price,nickname,userName):
        super().__init__(name,color,years,sound,price)
        self.nickname=nickname
        self.userName=userName

ToyataSupra=Car("Toyata Supraaaaaaaaaaa","black","1998","vutututututuuuuuuuu",100)

r34n = Car("nissan skyline gtr-34 vspec-2 nismo (custom)","midnight purple 2","2001","sutututuutuuuuuuuu",100)

rx7 = Car("Mazda Rx7","red","2002","brap brap brap brap braps",100)
    
# print(f"toyataSupraName = \n{ToyataSupra.name}")
# print(f"r34n = \n{r34n.name}")

a = Insan("Toyata Supraaaaaaaaaaa","black","1998","vutututututuuuuuuuu",100,"nickname","userName")

Insan.bilgi()

ToyataSupra.percentİncrease(10)