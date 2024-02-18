def get_valid_input(min_value, max_value):
    while True:
        try:
            user_input = int(input(f"Enter an integer between {min_value} and {max_value}: "))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Invalid input. Please enter an integer between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Let the user choose the valid range
min_value = int(input("Enter the minimum valid value: "))
max_value = int(input("Enter the maximum valid value: "))

# Call the function to get a valid input
user_choice = get_valid_input(min_value, max_value)

print("You entered:", user_choice)


