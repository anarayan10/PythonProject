try:
    Age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(Age)
except ValueError:
    print("Invalid input value")
except ZeroDivisionError:
    print("zero cannot be a input value")