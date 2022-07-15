#Paying Bills Randomly
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give meeveybody's name seperated by a comma.\n")
names = namesAsCSV.split(",")


num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")

#OR
#random_person = random.choice(names)
#print(f"{random_person} is going to buy the meal today!")