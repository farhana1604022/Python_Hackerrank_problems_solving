class user:
    def __init__(self,name,age,varsity):
        self.name=name
        self.age=age

    def greeting(self):
       return f'I am {self.name} and my age is {self.age} my balance  is {self.balance}'
    def ripa(self):
        return f' my name is {self.name} and i am {self.age} years old'
#here brad is a object of user class 
        
    
#customer class:extend class of user:
class customer(user):
    def __init__(self,name,age,varsity):
        self.varsity=varsity
        self.name=name
        self.age=age
    def set_balance(self,balance):
        self.balance= balance
        
    
    
brad=user('Farhana Akter',22,'CUET')
ob2=customer('ripa',22,'Cuet')
ob2.set_balance(500)
print(ob2.greeting())
print(brad.greeting())
print(brad.ripa())
         
        