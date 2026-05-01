# class Palindrom():
#     def __init__(self,number):
#         self.number=number
    
#     def palindrom_number(self):
#         self.number= str(self.number)
#         if self.number ==self.number[::-1]:
#             return True
#         else : 
#             return False
# num1 = Palindrom(999)
# print (num1.palindrom_number())



    


class Two_sum():
     def __init__(self,numbers,target):
         self.numbers = numbers
         self.target = target
     def summ(self):
        for x in self.numbers:
            a = self.target-x 
            if a in self.numbers and a != x :
                    return ([self.numbers.index(x),self.numbers.index(a)])    
        
        return "your target not found"         
num1 = Two_sum(numbers = [100,56,234,89,90],target = 200)
print(num1.summ())


# class Last_name:
#     def __init__(self,sentence):
#         self.sentence=sentence
    
#     def cherche_last_name(self):
#         words=self.sentence.split()
#         return words[-1]
        
       
# s1=Last_name(sentence='a malk a jmi hassan k7icha')      
# print(s1.cherche_last_name())

# class same_thing:
#     def __init__(self,thing):
#         self.thing=thing
        
#     def solution(self,list):
#         self.list=list
      
#         for i in list:
#             for x in list:
#                 if x==i:
#                     self.list.remove
# s=same_thing(['aa','zz','cc','aa'])
# print(s.solution(['aa','zz','cc','aa']))


