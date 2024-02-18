a = 50
b = 10
my_name = "Amit"

if a < 10:
     print("You Are AmitB")
elif my_name == "Amit":
    print("Found Your Name")
elif b > 5:
    print("B Is Good")
else:
    print("BlaBla")


my_list = [1]
if len(my_list) == 0:
    print("No Items In list")
else:
    print("Items In The List")

my_other_list = ["Or", "Tohar", "Adam"]
my_other_name = "Or"
if my_other_name in my_other_list:
    print("I Found You")
else:
    print("I Don't")


tt = [1,2,3]
rr = [1,2,3]
print(tt is rr)