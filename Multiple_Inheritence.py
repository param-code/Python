class Jee:
    no_of_students = "Bhut Saara"
    def __init__(self,sleep,main):
        self.neend = sleep
        self.jaruri = main
    def print_Details(self):
        return f"Main is {self.main}.Salary is {self.sleep}"
    @classmethod
    def change_students_no(cls ,new_students_no):
        cls.no_of_students = new_students_no
    @classmethod
    def from_str(cls ,string):
        #params = string.split("-")#Ek List bn Jata hai
        #print(params)
        #return cls(params[0],params[1])
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good" + string)
class Programmer(Jee):     #Programmer me Jee ke saare gunn(Material) aa chuke hai
        val = 8
        def print_prog(self):
             return f"The Programmer's name is {self.sleep} and main is {self.main}"
        def __init__(self, sleep, main):
             super().__init__(sleep, main)
class player:
     val = 9
     no_of_games = 4
     def __init__(self,name,game):
          self.name = name
          self.game = game
     def print_Details(self):
        return f"Name is {self.name}.Game is {self.game}"      
class CoolProgrammer(Programmer,player):
     val = 10
     language = "C++"
     def printlanguage(self):
          print(self.language)
Subject = Jee(7,"Consistency")#Ye Argument hamesha init ko jaata hai
Requirements = Jee(7,"Study")
Raj = player("Raj","Football")
Karan = CoolProgrammer(10,"C#")
# d = Karan.print_Details()
print(Karan.val)