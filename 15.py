import requests
while True:
    try:
        a = int(input("Enter a first number: "))
        b = int(input("Enter a Second number: "))
        result = a / b
        print(result)
        break
    except ValueError:
        print("Enter a correct number")
    except ZeroDivisionError:
        print("Couldn't divide by zero")
    except BaseException as e:
        print(e.args)
