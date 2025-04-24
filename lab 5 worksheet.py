#1
import random
# Create list of 5 odd integers
odd_integers = random.sample(range(1, 50, 2), 5)
print("Initial list of odd integers:", odd_integers)

# Create list of 4 even integers
even_integers = random.sample(range(2, 50, 2), 4)
print("List of even integers:", even_integers)

# Replace 3rd element of odd integers with even integers
odd_integers[2] = even_integers
print("List after replacing 3rd element with even integers:", odd_integers)

# Flatten, sort, and print the list
flattened_list = sorted([item for sublist in odd_integers for item in (sublist if isinstance(sublist, list) else [sublist])])
print("Flattened and sorted list:", flattened_list)

#2
# Generate 20 random integers
random_integers = [random.randint(1, 10) for _ in range(20)]
print("Generated list of integers:", random_integers)

# Accept a number from the user
number = int(input("Enter a number to find its positions: "))
# Find and print positions
positions = [i for i, x in enumerate(random_integers) if x == number]
print(f"Positions of {number} in the list:", positions if positions else "Number not found.")

#3
# Generate 50 random integers in the range 1 to 30
random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list with duplicates:", random_numbers)

# Remove duplicates
unique_numbers = list(set(random_numbers))
print("List after removing duplicates:", unique_numbers)

#4
# Generate 30 random integers
numbers = [random.randint(-50, 50) for _ in range(30)]
print("Generated list of integers:", numbers)

# Separate positive and negative numbers
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("List of positive numbers:", positive_numbers)
print("List of negative numbers:", negative_numbers)

#5
# List of 5 strings
string_list = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list of strings:", string_list)

# Convert to uppercase
uppercase_list = [string.upper() for string in string_list]
print("List of strings in uppercase:", uppercase_list)

#6
# List of Fahrenheit temperatures
fahrenheit_list = [32, 50, 68, 77, 104]
print("Temperatures in Fahrenheit:", fahrenheit_list)

# Convert to Celsius
celsius_list = [(temp - 32) * 5 / 9 for temp in fahrenheit_list]
print("Temperatures in Celsius:", celsius_list)

#7
stack = []
while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter element to push: "))
        stack.append(element)
    elif choice == 2:
        if stack:
            print("Popped element:", stack.pop())
        else:
            print("Stack is empty.")
    elif choice == 3:
        print("Stack contents:", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
#8
queue = []
while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter element to enqueue: "))
        queue.append(element)
    elif choice == 2:
        if queue:
            print("Dequeued element:", queue.pop(0))
        else:
            print("Queue is empty.")
    elif choice == 3:
        print("Queue contents:", queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
#9
# Input two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# List comprehension for numbers in list1 but not in list2
result_list = [x for x in list1 if x not in list2]
print("Numbers in list1 not in list2:", result_list)


