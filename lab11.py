while True:
    user_input = input("Enter an integer: ")
    if user_input.lstrip('-').isdigit():
        number = int(user_input)
        print("You entered the integer:", number)
        break
    else:
        print("Error: Please enter a valid integer.")
