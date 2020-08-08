class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


# super()
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')

#dir()
print(dir(wizard1))



