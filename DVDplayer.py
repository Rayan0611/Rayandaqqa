class DVDPlayer:
    def __init__(self):
        # Initial state of the DVD player
        self.power = False        # Starts off
        self.playing = False      # Not playing anything
        self.tray_open = False    # Tray is closed
        self.chapter = 1          # Start at chapter 1

    def turn_on(self):
        # Turn the DVD player on
        if not self.power:
            self.power = True
            print("DVD Player is now ON.")
        else:
            print("DVD Player is already ON.")

    def turn_off(self):
        # Turn the DVD player off
        if self.power:
            self.power = False
            self.playing = False  # Stop playback if turning off
            print("DVD Player is now OFF.")
        else:
            print("DVD Player is already OFF.")

    def play(self):
        # Start playing the DVD
        if self.power:
            if not self.playing:
                self.playing = True
                print(f"Playing chapter {self.chapter}.")
            else:
                print("Already playing.")
        else:
            print("Cannot play. DVD Player is OFF.")

    def stop(self):
        # Stop playing the DVD
        if self.power:
            if self.playing:
                self.playing = False
                print("Playback stopped.")
            else:
                print("Already stopped.")
        else:
            print("Cannot stop. DVD Player is OFF.")

    def open_tray(self):
        # Open the tray if it's closed
        if self.power:
            if not self.tray_open:
                self.tray_open = True
                print("Tray opened.")
            else:
                print("Tray is already open.")
        else:
            print("Cannot open tray. DVD Player is OFF.")

    def close_tray(self):
        # Close the tray if it's open
        if self.power:
            if self.tray_open:
                self.tray_open = False
                print("Tray closed.")
            else:
                print("Tray is already closed.")
        else:
            print("Cannot close tray. DVD Player is OFF.")

    def skip_chapter(self):
        # Go to the next chapter
        if self.power:
            self.chapter += 1
            print(f"Skipped to chapter {self.chapter}.")
        else:
            print("Cannot skip chapter. DVD Player is OFF.")


# Create a DVDPlayer 
player = DVDPlayer()

# User interaction loop
while True:
    print("\nDVD Player Menu:")
    print("1. Turn ON")
    print("2. Turn OFF")
    print("3. Play")
    print("4. Stop")
    print("5. Open Tray")
    print("6. Close Tray")
    print("7. Skip Chapter")
    print("8. Quit")

    choice = input("Choose an option (1-8): ")

   
    if choice == "1":
        player.turn_on()
    elif choice == "2":
        player.turn_off()
    elif choice == "3":
        player.play()
    elif choice == "4":
        player.stop()
    elif choice == "5":
        player.open_tray()
    elif choice == "6":
        player.close_tray()
    elif choice == "7":
        player.skip_chapter()
    elif choice == "8":
        print("Exiting DVD Player.")
        break
    else:
        print("Invalid choice. Please try again.")