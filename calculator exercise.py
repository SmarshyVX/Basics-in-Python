
def calculator():
    print("1. Division ")
    print("2. Multiplication ")
    print("3. Addition ")
    print("4. Subtraction ")
    print("5. Modulo ")
    print("6. Floor Division ")
    print("7. Power ")

    option = input("Select what you want to do: ").lower()

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if option in ('1', 'division'):
        if num2 == 0:
            print("Math Error: You tried dividing zero by zero,Restart the calculator and try again")
            return
        print("Answer:", num1 / num2)

    elif option in ('2', 'multiplication'):
        print("Answer:", num1 * num2)

    elif option in ('3', 'addition'):
        print("Answer:", num1 + num2)

    elif option in ('4', 'subtraction'):
        print("Answer:", num1 - num2)

    elif option in ('5', 'modulo'):
        if num2 == 0:
            print("Math Error: modulo by zero")
            return
        print("Answer:", num1 % num2)

    elif option in ('6', 'floor division' ):
        if num2 == 0:
            print("Math Error: floor division by zero")
            return
        print("Answer:", num1 // num2)

    elif option in ('7', 'power'):
        print("Answer:", num1 ** num2)

    else:
        print("Invalid Choice. Please try again.")


calculator()
