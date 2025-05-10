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

class HumanCreation:
    _humans = {}
    _created = 0

    @staticmethod
    def human_Create(name, gender, nationality):
        key = (name, gender, nationality)
        if key not in HumanCreation._humans:
            human = Human(name, gender, nationality)
            HumanCreation._humans[key] = human
            HumanCreation._created += 1
        return HumanCreation._humans[key]

if __name__ == "__main__":
    Humans = [
        HumanCreation.human_Create("James", 'male', 'Korea'),
        HumanCreation.human_Create("Sally", 'female', 'Korea'),
        HumanCreation.human_Create("James", 'male', 'Korea'),
        HumanCreation.human_Create("Steve", 'male', 'USA'),
        HumanCreation.human_Create("Steve", 'male', 'USA'),
        HumanCreation.human_Create("Alex", 'male', 'Japan')
    ]

    for num, human in enumerate(Humans, 1):
        print("Human Number : ", num)
        human.__printOut__()
        

    print("Total Humans : ", len(Humans))
    print("Total Objects : ", HumanCreation._created)