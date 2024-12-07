while True:
    try:
        age = int(input("AGE: "))
        income = int(input("INCOME: "))
        risk = income/age
        print(age)
    except ValueError:
        print("INVALID!")
    except ZeroDivisionError:
        print("AGE CANNOT BE ZERO")