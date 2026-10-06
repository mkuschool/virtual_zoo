# virtual zoo organisation program v1
# made by mku
# computer science is pretty awesome
# (=^・^=)

import csv
import time
import random

animal_name = ""
species = ""
age = 0
age_months = 0
weight = 0
full_age = []
health = ""
fed = False
animal_dict = {
    
}
enclosure = [[None, None, None],
            [None, None, None],
            [None, None, None]]

def save_data():
    with open("saved_data.csv", "w", newline="") as file:  
        writer = csv.writer(file)

        writer.writerow(["name","species","age","weight","health","fed"])

        for name, data in animal_dict.items():
            writer.writerow([
                name,
                data["species"],
                data["age"],
                data["weight"],
                data["health"],
                data["fed"],
            ])
    l_b()

def load_data():
    global animal_dict

    with open("saved_data.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]

            animal_dict[name] = {
                "name": name,
                "species": row["species"],
                "age": int(row["age"]),
                "weight": int(row["weight"]),
                "health": row["health"],
                "fed": row["fed"]
            }
    l_b()

def l_b():
    print("-" * 35)
    time.sleep(0.3)

def add_item(item):
    global enclosure
    for row in range(3):
        for col in range(3):
            if enclosure[row][col] is None:
                enclosure[row][col] = item
                return

    print("Error: Enclosure is full!")

def view_enclosure_map():
    print("\n=== Enclosure Map ===")
    for row in range(3):
        for col in range(3):
            animal = enclosure[row][col]
            label = animal if animal else "----"
            print(f"[{label:^10}]", end="")  # centre in 10 chars
        print()  # newline after each row


def validation(x):
    if x == "name":
        animal_name = str.lower(input("Enter the animal's name: "))
        while True:
            if animal_name != "":
                return animal_name
                break
            else:
                animal_name = str.lower(input("Error: Nothing written, enter the animal's name again: "))
    elif x == "species":
        species = input("Enter the animal's species: ")
        while True:
            if species != "":
                return species
                break
            else:
                species = input("Error: Nothing written, enter the animal's species again: ")
    elif x == "age":
        age = int(input("Enter the animal's age: "))
        while True:

            if age == "old":
                age = int(input("Enter the animal's age (no restrictions): "))
                return age
                break
            elif 0 < age < 100:
                return age
                break
            else:
                age = input("Error: Age out of range, enter the animal's age again, or write [old] to bypass the age limit: ")
    elif x == "weight":
        while True:
            weight = input(
                "Enter the animal's weight (kg), or type [heavy] if over 1000kg: "
            )

            if weight.lower() == "heavy":
                weight = int(input("Enter the animal's weight (no restrictions): "))
                return weight

            weight = int(weight)

            if 0 < weight < 1000:
                return weight

            else:
                print("Error: Weight out of range.")
    
    elif x == "health":
        health = str.lower(input("Enter the animal's health status (Healthy, Sick, Injured, Hospitalized): "))
        while True:
            if health in ["healthy", "sick", "injured", "hospitalized"]:
                return health
                break
            else:
                health = input("Error: Health Status not in List, Enter the animal's health status again (Healthy, Sick, Injured, Hospitalized): ")
    elif x == "fed":
        fed = str.lower(input("Has the animal been fed?(Y/N) "))
        while True:
            if fed == "y":
                fed = True
                return fed
            elif fed == "n":
                fed == False
                return fed
            else:
                fed = str.lower(input("Error: Answer isn't Y(yes) or N(no), Try again: Has the animal been fed?(Y/N) "))
   
    


        

def animal_stats(animal):
    my_list = ["name","species","age","weight","health","fed"]
    l_b()
    print(f"{animal}'s statistics card: ")
    for x in my_list:
        l_b()
        print(animal_dict[animal][x])
    l_b()    

def input_animal():
    global animal_name
    global age
    global weight
    global species
    global health
    global animal_dict
    global fed
    if len(animal_dict) > 10:
        print("Error: Too many animals already added!")
    else:
            animal_name = validation("name")
            l_b()
            species = validation("species")
            l_b()
            age = validation("age")
            l_b()
            weight = validation("weight")
            l_b()
            health = validation("health")
            l_b()
            fed = validation("fed")
        
            animal_dict[animal_name] = {
            "name": animal_name,
            "species": species,
            "age": age,
            "weight": weight,
            "health": health,
            "fed": fed
            }
        
            animal_stats(animal_name)

            ans = str.lower(input(f"Do you want to add {animal_name} to the enclosure?(Y/N) "))
            if ans == "y":
                add_item(animal_name)
                print(f"{animal_name} added!")
                view_enclosure_map()
                
def rebuild_enc():
    for i, name in enumerate(animal_dict):
        if i >= 9:
            break

        row = i // 3
        col = i % 3

        enclosure[row][col] = name

def remove_animal(animal):
    global animal_dict
    confirm = str.lower(input(f"Are you sure you want to remove {animal} from the zoo?(Y/N) "))
    time.sleep(random.randint(1,10)/10)
    if confirm == "y":
        removed_animal = animal_dict.pop(animal)
        print(f"{removed_animal} was removed.")
    else:
        print(f"{animal} was not removed.")


def view_all():
    for animal in animal_dict:
        animal_stats(animal)

def zoo_summary():
    global animal_dict
    ages = [animal["age"] for animal in animal_dict.values()]
    weights = [animal["weight"] for animal in animal_dict.values()]

    print("Zoo Summary")
    l_b()
    print(f"Amount of animals in the zoo: {len(animal_dict)}")
    l_b()
    print("Average age: ", sum(ages) / len(ages))
    l_b()
    print("Youngest: ", min(ages))
    l_b()
    print("Oldest: ", max(ages))
    l_b()
    print("Heaviest: ", max(weights))
    l_b()
    print("Lightest: ", min(weights))
    l_b()


def feed_animal(animal):
    animal_dict[animal]["fed"] = True
    print(f"{animal} has been fed!")

def health_check(animal):
    print(f"{animal}'s health status is:")
    print(animal_dict[animal]["health"])
    time.sleep(0.5)
    change = str.lower(input("Do you want to change the animal's health status?(Y/N) "))
    if change == "y":
        new_health = validation("health")
        animal_dict[animal]["health"] = new_health

while True:
    load_data()
    rebuild_enc()
    print("What do you want to do today?")
    todo = int(input(" Add Animal(1) | Check Animal Stats(2) | View All Animals(3) | Zoo Summary(4) | Feed Animal(5) | Health Check(6) | Remove Animal(7) | View Enclosure Map(8) |Quit(9) "))
    if todo == 1:
        input_animal()
    elif todo == 2:
        while True:
            name = str.lower(input("What is the name of the animal you want to check? "))
            if name in animal_dict:
                animal_stats(name)
                break
            else:
                print("Sorry, that animal is not in the list of animals, check the spelling of the name.")
    elif todo == 3:
        view_all()
    elif todo == 4:
        zoo_summary()
    elif todo == 5:
        animal = str.lower(input("What animal do you want to feed?"))
        feed_animal(animal)
    elif todo == 6:
        animal = str.lower(input("What animal do you want to check?"))
        health_check(animal)
    elif todo == 7:
        animal = str.lower(input("What animal do you want to remove?"))
        remove_animal(animal)
    elif todo == 8:
        view_enclosure_map()
    elif todo == 9:
        break
    save_data()
