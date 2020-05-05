import random

switch = True
wins = 0
n = 10000

def monty_hall(choice):
    doors = ["A", "B", "C"]
    correct_door = random.choice(doors)
    doors.remove(correct_door)

    if choice == correct_door:
        remaining_doors = [choice, random.choice(doors)]
        
        if switch == True:
            return 0
        if switch == False:
            return 1

    if choice != correct_door:
        remaining_doors = [choice, correct_door]
        
        if switch == True:
            return 1
        if switch == False:
            return 0        
        
for i in range(n):
    door_choice = random.choice(["A", "B", "C"])
    wins = wins + (monty_hall(door_choice))

print("Switch: ", switch)
print("Trials: ", n)
print("Wins: ", wins)
print("Wins / Trials: ", wins / n)



import matplotlib.pyplot as plt

data = [wins, n - wins]
plt.title("Monty Hall-sims \n n = " + str(n) + ", switch = " + str(switch))
plt.bar(["Wins", "Non-wins"], data)
plt.show()




