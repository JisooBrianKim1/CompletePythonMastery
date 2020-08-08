
#private and public variables


class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        return self
    
    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old')


player1 = PlayerCharacter('brian', 22)
# player1.name = 'Jim'
# player1.speak = 'booooo'

print(player1.speak())
