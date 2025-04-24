#lower case to upper case 
words = [" ayaan", "het", "goa", "hey", "dad ","mom"]
uppercase_words = {word.upper() for word in words}
print(uppercase_words)
# Create a set containing 10 random numbers in the range 15 to 45
import random
random_numbers = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Numbers less than 30: {count_less_than_30}")
random_numbers = {num for num in random_numbers if num <= 35}
print(random_numbers)

#Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it
names_set = set()
names_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("After adding names:", names_set)
names_set.discard("Charlie")
names_set.add("Chris")
print("After modifying a name:", names_set)
names_set.discard("Alice")
names_set.discard("Eve")
print("After deleting two names:", names_set)
#A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.
# Create a set containing names starting with A or B
names_set = {"Alice", "Bob", "Andrew", "Bryan", "Anna", "Ben"}
print("Original set:", names_set)
names_A = {name for name in names_set if name.startswith("A")}
names_B = {name for name in names_set if name.startswith("B")}
print("Names starting with A:", names_A)
print("Names starting with B:", names_B)
