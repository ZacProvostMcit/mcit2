name=input("What is your name: ")

tripdistance=input("How many km is your trip: ")

fuelconsumption=input("What is your car's fuel consumption in L/100km: ")

fuelprice=input("What is the price of fuel per liter: ")

numberofpeople=input("How many people are going on the trip: ")

totalcost=(float(tripdistance)/100)*float(fuelconsumption)*float(fuelprice)

gasneeded=(float(tripdistance)/100)*float(fuelconsumption)

costperperson=totalcost/int(numberofpeople)

print(f"Gas needed: {gasneeded} liters")

print(f"Total cost of the trip {totalcost}")

print (f"Cost per person: {costperperson}")