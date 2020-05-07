import random

# her kan man velge om man skal bytte dør eller ikke
switch = False

# teller antall gevinster
wins = 0

# antall simuleringer som skal kjøres
n = 100


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

    # dersom deltakeren opprinnelig har valgt rett dør:
    if choice == correct_door:
        
        # vi står igjen med deltakerens valg + en av dørene uten gevinst:
        remaining_doors = [choice, random.choice(doors)]

        # bytt eller ikke bytt:
        if switch == True:
            return 0 # ikke gevinst hvis man bytter dør
        if switch == False:
            return 1 # gevinst hvis man ikke bytter dør


    # dersom deltakeren opprinnelig har valgt feil dør blir det motsatt om man bytter:
    if choice != correct_door:

        # vi står igjen med deltakerens valg + døra med gevinsten
        remaining_doors = [choice, correct_door]

        if switch == True:
            return 1 # gevinst dersom man bytter dør
        if switch == False:
            return 0 # ikke gevinst dersom man velger å ikke bytte dør


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



# vi plotter data (forutsetter matplotlib):
import matplotlib.pyplot as plt

data = [wins, n - wins]
plt.title("MONTY HALL-simulering \n n = " + str(n) + ", bytte dør = " + str(switch))
plt.bar(["Gevinst", "Ikke gevinst"], data)
plt.show()


