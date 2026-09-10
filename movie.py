name=input("What is your name: ")

age=int(input("What is your age: "))

money=int(input("How much money do you have: "))


if age >=18 and money >= 1000000:
    print(f"Welcome {name}, you are {age} years old and have ${money}. You could probably rent the room to yourself.")

elif age < 5:
    print(f"Welcome {name}, you are {age} years old, maybe you should not be paying that ticket by yourself!")

elif age >= 18 and money >= 15:
    print(f"Welcome {name}, you are {age} years old and have ${money}. You can buy the ticket.")

elif money < 15:
    print(f"Welcome {name}, you are {age} years old and have ${money}. You do not have enough money to buy the ticket.")

else:
    print(f"Welcome {name}, you are {age} years old and have ${money}. You are not old enough to buy the ticket.")