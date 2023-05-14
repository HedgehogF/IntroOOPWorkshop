from Principles.Inheritance.person.person import Person

class Student(Person):

    def __init__(self, name, age, address, faculty, year_of_study):
        super().__init__(name, age, address)
        self.faculty = faculty
        self.year_of_study = year_of_study

    def description(self):
        super().description()
        print(f"Faculty: {self.faculty} \nYear_of_study: {self.year_of_study}")