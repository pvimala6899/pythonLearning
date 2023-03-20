class employee:
      def __init__(self,Name,Age):
            self.name = Name
            self.age = Age

      def coworker(self):
            print("my name is " + self.name + "age is " + str(self.age)) 

class company(employee):
      def __init__(self,Name,Age):
            super().__init(Name,Age)

emp = employee("vimal", 20) 
emp.coworker()           
                       