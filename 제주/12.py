class Wizart:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')


x = Wizart(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
