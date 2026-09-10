

keep= "yes"

while keep == "yes":
    
    
    name=input("What is your name: ")

    age=int(input("What is your age: "))

    money=int(input("How much money do you have: "))

    snack=input("Did you buy snacks? (yes or no): ")


    if age < 18:
        print(f"Welcome {name}, you are {age} years old and have ${money}. You are not old enough to buy the ticket.")

    elif age >= 18 and money >= 15 and snack == "no":
        print(f"Welcome {name}, you are {age} years old and have ${money}. You can buy the ticket.")

    elif age >= 18 and money >= 15 and snack == "yes":
        print(f"Welcome {name}, you are {age} years old and have ${money}. You can buy the ticket and enjoy a 10% discount on your ticket price for buying snacks!")

    ask = input("Do you want to continue? (yes or no): ").lower()

    while ask != "yes" and ask != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")
        ask = input("Do you want to continue? (yes or no): ").lower()

    if ask == "no":
        print("Thank you for using the ticketing system. Goodbye!")
        keep="no"

    

    




 


    
        