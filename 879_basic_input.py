while True:
    name = input("Please enter your name: ")

    # Throw an error if age is not numerical
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Error: Only numbers allowed.")
        break
    
    if((age < 25) and (age > 0)):
        msg = "Enjoy your pre-back ache years!"
    elif((age < 100) and (age > 0)):
        msg = "Getting old aren't you?"
    else:
        msg = "How are you alive?"

    print(f"Hello, {name}! {msg}")

    option = input("Enter 'y' to exit: ").lower()
    if option == 'y':
        break