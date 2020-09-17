
import random

# random() produces numbers in range [0.0, 1.0)
for i in range(3):
    print(random.random())

# randint(10, 20) produces random integers in the range [10, 20)
for i in range(3):
    print(random.randint(10, 20))

team_members = ["Moritz", "Manuel", "Marvin", "Viktor"]
leader = random.choice(team_members)
print(leader)


class Dice:
    def roll(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        return (self.x, self.y)


dice = Dice()
print(dice.roll())