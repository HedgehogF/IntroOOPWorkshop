import datetime

from Principles.Inheritance.person.employee import Employee


class SoftwareEngineer(Employee):

    def __init__(self, name, age, address, company, salary, years_of_experience):
        if "Telenav" in company and \
                datetime.datetime.today().month >= 5 and \
                datetime.datetime.today().year >= 2023:
            raise Exception("You are sure? I don't think so.")
        super().__init__(name,age,address,company,salary)
        self.years_of_experience = years_of_experience

    def description(self):
        super().description()
        print(self.years_of_experience)
