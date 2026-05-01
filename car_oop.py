class Two_sum():
     def __init__(self,numbers,target):
         self.numbers = numbers
         self.target = target
     def summ(self):
        for x in self.numbers:
            a = self.target-x 
            if a in self.numbers and a != x :
                    return ([self.numbers.index(x),self.numbers.index(a)]
        return "your target not found"         
num1 = Two_sum(numbers = [100,56,234,89,90],target = 200)
print(num1.summ())
