import random

# her kan man velge om man skal bytte dør eller ikke
switch = False

# teller antall gevinster
wins = 0

# antall simuleringer som skal kjøres
n = 100000


# vi lager en funksjon som skal kjøres n-antall ganger:
def monty_hall():
    # oppretter tre dører:
    doors = ["A", "B", "C"]

    # deltakeren velger en av dørene tilfeldig:
    choice = random.choice(["A", "B", "C"])

    # velger tilfeldig hvilken dør som skal ha gevinst:
    correct_door = random.choice(doors)

    # vi fjerner vinnerdøra fra lista, slik at to dører uten gevinst gjenstår:
    doors.remove(correct_door)

    # dersom deltakeren har valgt rett dør:
    if choice == correct_door:
        
        # deltakerens valg + en av dørene uten gevinst:
        remaining_doors = [choice, random.choice(doors)]

        # bytt eller ikke bytt:
        if switch == True:
            return 0 # ikke gevinst hvis man bytter
        if switch == False:
            return 1 # premie hvis man ikke bytter


    # dersom deltakeren opprinnelig har valgt feil dør:
    if choice != correct_door:

        remaining_doors = [choice, correct_door]

        if switch == True:
            return 1
        if switch == False:
            return 0  


# vi kjører funksjonen monty_hall() n-antall ganger:        
for i in range(n):
    
    # teller resultatet for hver n:
    wins = wins + monty_hall()







# vi printer data i konsollen:
print("MONTY HALL")
print("Bytte dør: ", switch)
print("Forsøk: ", n)
print("Gevinst: ", wins)
print("Gevinst / Forsøk: ", wins / n)



# vi plotter data:
import matplotlib.pyplot as plt

data = [wins, n - wins]
plt.title("MONTY HALL-simulering \n n = " + str(n) + ", bytte dør = " + str(switch))
plt.bar(["Gevinst", "Ikke gevinst"], data)
plt.show()




