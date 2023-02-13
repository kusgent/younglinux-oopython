from random import randint


class Warrior:
    def make_health(self, value):
        self.health = value

    def make_kick(enemy):
        enemy.health -= 20


first_unit = Warrior()
second_unit = Warrior()
first_unit.make_health(100)
second_unit.make_health(100)

while first_unit.health > 0 and second_unit.health > 0:
    n = randint(1, 2)
    if n == 1:
        Warrior.make_kick(second_unit)
        print("Первый бьет второго")
        print("У второго осталось", second_unit.health)
    else:
        Warrior.make_kick(first_unit)
        print("Второй бьет первого")
        print("У первого осталось", first_unit.health)

if first_unit.health > second_unit.health:
    print("ПЕРВЫЙ ПОБЕДИЛ")
else:
    print("ВТОРОЙ ПОБЕДИЛ")
