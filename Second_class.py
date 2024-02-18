#A
x = input('Enter a number as X: ')
y = input('Enter a number as Y: ')
if int(x) > int(y):
    print("BIG")
elif int(x) < int(y):
    print("SMALL")
elif int(x) == int(y):
    print("EVEN")

#B
for i in range(5):
    print(i)

#C
numb = int(input("Enter a number: "))
if numb == 1:
    print("Summer")
elif numb == 2:
    print("Winter")
elif numb == 3:
    print("Fall")
elif numb == 4:
    print("Spring")
else:
    print("Error")

#D
# 1. 10 times
# 2. 10

#E
age = 31
first_letter_fname = "A"
shekel_dollar_cerrency = 0.2776
Isfly_aboard = True
apartment = 72
print(age)
print(first_letter_fname)
print(shekel_dollar_cerrency)
print(Isfly_aboard)
print(apartment)
print (age + shekel_dollar_cerrency)

#F
phone_number = input("Enter your phone: ")
print("phone number :" + phone_number)

#G
def printHello():
    print("Hello")
def calculate():
    print(5 + 3.2)

#H
def printYourName(YourName):
    print(YourName)
def div2(number):
    print(number / 2)

#I
def sumit(number1, number2):
    return number1 + number2
def sumstrings(string1, string2):
    return string1 + " " + string2
#K

def print_left_aligned_pyramid(rows):
    for i in range(rows):
        # Print stars
        for j in range(i + 1):
            print("*", end="")

        # Move to the next line after completing a row
        print()


# Example: Print a left-aligned pyramid with 5 rows
print_left_aligned_pyramid(5)

