name=str(input("What is your name: "))

age=int(input("What is your age: "))

money=int(input("How much money do you have: "))

popcorn=str(input("Do you have popcorn? (yes or no): "))

if age < 18:
    print(f"Nice try, {name}! Go home and watch cartoons! 🍼📺😂")

elif age >= 18 and money < 15:
     print(f"Sorry {name}, ERROR 404: MONEY NOT FOUND! 💸😂")

elif age >= 18 and money >= 15 and popcorn == "yes":
    print(f"Welcome {name}! Ticket ✅ Popcorn ✅ Life is good! 🍿😎")

else: 
    print(f"Welcome {name}... but coming to the cinema without popcorn is VERY suspicious. 👀😂")

