
class Human:

    tribe = "Hominina"

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe(self):
        description = f"My name is {self.first_name} {self.last_name}  and I am {self.age} years old."
        print(description)

    @classmethod
    def getTribe(cls):
        return cls.tribe

    @staticmethod
    def human_wikipedia_definition():
        print("Humans (Homo sapiens) are the most common and widespread species of primate in the great ape family Hominidae.")


john = Human("John","Doe",30)
john.human_wikipedia_definition()

Human.human_wikipedia_definition()
