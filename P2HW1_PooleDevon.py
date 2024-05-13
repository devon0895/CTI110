#DevonPoole
#2/20/24
#P1HW2
#Doing basic math in python

budget = int(input("\nEnter budget: ", ))

area = input("\nEnter your travel destination? ", )

gas = int(input("\nHow much do you think you will spend on gas? ", ))

lodge = int(input("\nApproximately, How much will you need for accomodation/hotel? "))

food = int(input("\nLast, how much do you need for food? "))

#--------Travel Expenses--------
print("Location: ", area)
print(f"Initial Budget: {budget:.1f}")
print(f"Fuel: {gas:.1f}")
print(f"Accomodation: {lodge:.1f}")
print(f"Food: {food:.1f}")

exp = gas + lodge + food 
print(f"\nRemaining Balance: {budget - exp:.1f}")
