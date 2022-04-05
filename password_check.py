while True:
    Minimum_password = input("Password: ")

    password = len(Minimum_password)

    if password >= 4:
        print(password* "*")
        break

    elif password < 4:
        print("Invalid Password, Try again!")
        continue