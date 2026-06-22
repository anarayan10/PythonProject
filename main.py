'''weight = input("Enter the weight in pounds : ")
conversion_to_kilograms = int(weight) / int(2.205)
print (conversion_to_kilograms)'''
from turtledemo.penrose import start
from turtledemo.round_dance import stop

'''price_of_the_house = 1000000
buyer_good_credit = True
if has buyer_good_credit:
    down_payment = 0.10 * price_of_the_house

else:
    down_payment = 0.20 * price_of_the_house

print(f"Pay the down payment: {down_payment} ")'''

'''length_of_the_name = input("Enter the name : ")
name = len(length_of_the_name)
print(name)
if name < 3:
    print("name must be atleast 3 character")
elif name > 50:
    print("name must be less than 50 character")
else:
    print("name looks good!")'''

'''weight = int(input ("Enter the weight: "))
choice = input (" L(bs) or (K)g : ")
if choice == "l":
    converted = weight * 0.45
    print(f"Weight in pounds {converted} kilos ")
else:
    converted = weight / 0.45
    print(f"Weight in kilograms {converted} pounds ")'''

import unicodedata

# 1. Generate the prompt symbol dynamically
prompt = unicodedata.lookup("GREATER-THAN SIGN") + " "

# 2. Start an infinite loop to keep the game running
while True:
    # Get user input, remove extra spaces, and make it lowercase
    user_input = input(prompt).strip().lower()

    # 3. Check the commands
    if user_input == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - to exit")

    elif user_input == "start":
        print("Car started... Ready to go!")
        processed_input = set()
        for start in user_input:
            if user_input in processed_input:
                print("You already started the car")

    elif user_input == "stop":
        print("Car stopped.")
        processed_input = set()
        for stop in user_input:
            if user_input in processed_input:
                print("You already stopped the car")

    elif user_input == "quit":
        print("Exited the game.")
        break  # This stops the loop and exits the program

    else:
        print("I don't understand that...")


