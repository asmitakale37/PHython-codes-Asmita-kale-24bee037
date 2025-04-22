#1.Write a program that converts words present in a list into uppercase and stores them in a set.
Names={"Abhi","Asmita","Het","aayan"}
uppercase={words.upper()for word in Names}
print(Names)
#2
import random
random_numbers = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Numbers less than 30: {count_less_than_30}")
random_numbers = {num for num in random_numbers if num <= 35}
print(random_numbers)
#3
names_set = set()
names_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("After adding names:", names_set)
names_set.discard("Charlie")
names_set.add("Chris")
print("After modifying a name:", names_set)
names_set.discard("Alice")
names_set.discard("Eve")
print("After deleting two names:", names_set)
#4
names_set = {"Alice", "Bob", "Andrew", "Bryan", "Anna", "Ben"}
print("Original set:", names_set)
names_A = {name for name in names_set if name.startswith("A")}
names_B = {name for name in names_set if name.startswith("B")}
print("Names starting with A:",names_A)
print("Names starting with B:",names_B)

