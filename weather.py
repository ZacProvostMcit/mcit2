name=input("What is your name: ")

age=input("What is your age: ")

weather=input("What is the weather like today(good/bad): ")

friends=int(input("How many friends are coming with you: "))

budget=int(input("What is the budget per person for the trip: "))

total = friends*budget

if weather == "good" and total < 100:
  print(f"Welcome {name}, you are {age} years old. Your group has a total budget of ${total}. Go to the park and have a picnic!")

elif weather == "good" and total >= 100:
  print(f"Welcome {name}, you are {age} years old. Your group has a total budget of ${total}. Go to the amusement park!")

else:
    print(f"Welcome {name}, you are {age} years old. Your group has a total budget of ${total}. Stay home and watch a movie!")



