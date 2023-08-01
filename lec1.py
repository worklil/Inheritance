class Person:
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def display_name(self):
        print("You must be", self.first_name, self.surname)

class Student(Person):
    def __init__(self, first_name, surname, university):
        # allows us to define a class that inherits all the methods
        super().__init__(first_name, surname)
        self.university = university

    def welcome(self):
        print("Well, welcome to", self.university, self.first_name)

student1 = Student("Eric", "Idle", "UWS")
student1.display_name()
student1.welcome()
# -------------------------------------------------------------------------------------------------


class Team:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name