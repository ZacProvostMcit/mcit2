firstname=input("What is your first name: ")

favoritedestination=input("What is your favorite destination: ")

numberofdays=input("How many days do you want to stay at your favorite destination: ")

dailybudget=input("What is your daily budget for your trip: ")

print(f"Hi {firstname}, your {numberofdays} day trip to {favoritedestination} will cost you a total of ${int(numberofdays)*int(dailybudget)}.")