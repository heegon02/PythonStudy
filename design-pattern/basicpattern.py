import random

class Human:
    def __init__(self, name, gender, nationality):
        self.name = name
        self.gender = gender
        self.nationality = nationality
    
    def __printOut__(self):
        print(f"Name : {self.name}")
        print(f"gender : {self.gender}, nation : {self.nationality}")
        print()

if __name__ == "__main__":
    Humans = [
        Human("James", 'male', 'Korea'),
        Human("Sally", 'female', 'Korea'),
        Human("James", 'male', 'Korea'),
        Human("Steve", 'male', 'USA'),
        Human("Steve", 'male', 'USA'),
        Human("Alex", 'male', 'Japan')
    ]

    for num, human in enumerate(Humans, 1):
        print("Human Number : ", num)
        human.__printOut__()
        

    print("Total Humans : ", len(Humans))
    print("Total Objects : ", len(Humans))