my_file = open("names.txt", "a")
def append_name ():
    for i in range(3):
        name = input("Enter a name: ")
        my_file.writelines(name + "\n")
append_name()

my_file = open("names.txt")
def print_file (my_file):
    for name in my_file.readlines():
        print("Hello " + name, end='')
print(print_file(my_file))