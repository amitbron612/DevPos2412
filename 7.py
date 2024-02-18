my_list = list(range(1,101))

for i in my_list:
    if ("7" not in str(i) and i % 7 !=0):
        print(i)
    else:
        print("Boom")