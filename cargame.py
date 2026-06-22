#with boolean for repeated messages
import unicodedata

prompt = unicodedata.lookup("GREATER-THAN SIGN") + " "

car_started = False

while True:
    user_input = input(prompt).strip().lower()

    if user_input == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - to exit")

    elif user_input == "start":
        if car_started:
            print("Car is already started!")
        else:
            print("Car started... Ready to go!")
            car_started = True

    elif user_input == "stop":
        if not car_started:
            print("Car is already stopped!")
        else:
            print("Car stopped.")
            car_started = False

    elif user_input == "quit":
        print("Exited the game.")
        break

    else:
        print("I don't understand that...")

        # with set for repeated messages
        import unicodedata

        prompt = unicodedata.lookup("GREATER-THAN SIGN") + " "

        processed_input = set()

        while True:
            user_input = input(prompt).strip().lower()

            if user_input == "help":
                print("start - start the car")
                print("stop - stop the car")
                print("quit - to exit")

            elif user_input == "start":
                if "start" in processed_input:
                    print("You already started the car")
                else:
                    print("Car started... Ready to go!")
                    processed_input.add("start")
                    processed_input.discard("stop")

            elif user_input == "stop":
                if "stop" in processed_input:
                    print("You already stopped the car")
                else:
                    print("Car stopped.")
                    processed_input.add("stop")
                    processed_input.discard("start")

            elif user_input == "quit":
                print("Exited the game.")
                break

            else:
                print("I don't understand that...")