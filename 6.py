for i in range(5):
    print("Hello " + str(i))
else:
    print("Finished")

class_mate = ["Amit", "Yoni", "Gilad", "Oren"]
for name in class_mate:
    if name == "Amit":
        name = "BlaBla"
    print(name)

for i in range(len(class_mate)):
    class_mate[i] = "Moshe"
print(class_mate)


your_name = input("Enter your name: ")
while your_name != "Amit":
    print("You are not Amit The King!")
    if your_name == "Haim":
        print("Oh My God!")
        break
    if your_name == "David":
        print("Wow!")
    continue
    your_name = input("Enter your name: ")