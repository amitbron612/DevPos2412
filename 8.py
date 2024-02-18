details = ["Amit", "Bronshtein", 31, True]
details_dic = {"fname": "Amit",
             "lname": "Bronshtein",
             "age": 31,
             "ismarried": True}
my_class = [
    {"fname": "Or", "lname": "Bronshtein"},
    {"fname": "KAKA", "lname": "KATZ"}
]
for student in my_class:
    print(student["fname"])
print(details_dic.keys())
print(details_dic.values())