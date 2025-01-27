while True:
    try:
        number = int(input("Which multiplication table do you want to see? "
                           "(1-10). Enter 0 to exit the program.\n"))
        if number == 0:
            break
        elif number <= 0 or number > 10:
            print("The number must be between 1 and 10.")
            continue
        else:
            for i in range(1, 11):
                product = i * number
                print(f"{number} x {i} = {product}")
    except ValueError:
        print("The input must be a number.")

