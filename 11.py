def my_printer(prefix, amount_of_times):
    for i in range(amount_of_times):
        print(prefix + str(i))

my_printer("Hello ", 5)
my_printer("You are number ", 10)

def mul_five(my_number):
    result = my_number * 5
    return result

the_result = mul_five(10)
print(the_result)