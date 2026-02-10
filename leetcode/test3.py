class Person:
    def __init__(self,fname,sname,age):
        self.firstName = fname
        self.secondName = sname
        self.age = age
        self.details = {
            "FirstName" : fname,
            "SurName" : sname,
            "Age" : age
        }

    def __str__(self):
        return str(self.details)

p1 = Person('Naveen','Raj',25)
print(p1)

