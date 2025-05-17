class TVRemote:
    def __init__(self):
        # TV settings
        self.power = False     # TV starts off
        self.volume = 10       # Default volume level
        self.channel = 1       # Default channel

    def turn_on(self):
        # Turns the TV on
        if not self.power:
            self.power = True
            print("TV is now ON.")
        else:
            print("TV is already ON.")

    def turn_off(self):
        # Turns the TV off
        if self.power:
            self.power = False
            print("TV is now OFF.")
        else:
            print("TV is already OFF.")

    def increase_volume(self):
        # Increases the volume if TV is on and volume is below max
        if self.power:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
            else:
                print("Volume is at maximum.")
        else:
            print("TV is OFF. Turn it on first.")

    def decrease_volume(self):
        # Decreases the volume if TV is on and volume is above 0
        if self.power:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
            else:
                print("Volume is at minimum.")
        else:
            print("TV is OFF. Turn it on first.")

    def next_channel(self):
        # Goes to the next channel if TV is on
        if self.power:
            self.channel += 1
            print(f"Switched to channel {self.channel}.")
        else:
            print("TV is OFF. Turn it on first.")

    def previous_channel(self):
        # Goes to the previous channel if TV is on and not already on the first
        if self.power:
            if self.channel > 1:
                self.channel -= 1
                print(f"Switched to channel {self.channel}.")
            else:
                print("You're on the first channel.")
        else:
            print("TV is OFF. Turn it on first.")


# Create an instance of TVRemote
remote = TVRemote()

# Loop to interact with the user
while True:
    print("\nTV Remote Menu:")
    print("1. Turn ON TV")
    print("2. Turn OFF TV")
    print("3. Increase Volume")
    print("4. Decrease Volume")
    print("5. Next Channel")
    print("6. Previous Channel")
    print("7. Quit")

    choice = input("Select an option (1-7): ")

    # Call the appropriate method based on user input
    if choice == "1":
        remote.turn_on()
    elif choice == "2":
        remote.turn_off()
    elif choice == "3":
        remote.increase_volume()
    elif choice == "4":
        remote.decrease_volume()
    elif choice == "5":
        remote.next_channel()
    elif choice == "6":
        remote.previous_channel()
    elif choice == "7":
        print("Exiting TV Remote.")
        break
    else:
        print("Invalid choice. Try again.")
