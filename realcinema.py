keepgoing = "yes"

while keepgoing == "yes":
    
    name=input("What is your name: ").strip()

    while name == "":
        print("Please enter your name.")
        name=input("What is your name: ").strip()

    
    age=input("What is your age: ")

    while not age.isdigit():
        print("Please enter a valid age.")
        age=input("What is your age: ")


    money=input("How much money do you have: ")

    while not money.replace(".", "", 1).isdigit():
        print("Please enter a valid amount of money.")
        money=input("How much money do you have: ")

    snack=input("Did you buy snacks? (yes or no): ").lower().strip()

    while snack != "yes" and snack != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")
        snack=input("Did you buy snacks? (yes or no): ").lower().strip()

    ticketprice = 15

    if snack == "yes":
        discount = ticketprice * 0.10
        ticketprice = ticketprice - discount
        print("You bought snacks! You get a 10% discount on your ticket price.")

    if int(age) >= 18 and float(money) >= ticketprice:
        print(f"Welcome {name}, you are {age} years old and have ${money}. You can buy the ticket for ${ticketprice:.2f}.")

    else:
        if int(age) < 18:
            print(f"Sorry {name}, you are {age} years old and cannot buy the ticket.")
        if float(money) < ticketprice:
            print(f"Sorry {name}, you have ${money} and cannot afford the ticket for ${ticketprice:.2f}.")

    ask = input("Do you want to continue for another person? (yes or no): ").lower()

    while ask != "yes" and ask != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")
        ask = input("Do you want to continue for another person? (yes or no): ").lower()

        if ask == "no":
            print("Thank you for using the ticketing system. Goodbye!")
            keepgoing="no"