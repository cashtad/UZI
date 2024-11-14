def get_room_data():
    # Initialize an empty list to store data about each room
    room_data = []

    # Define available room types
    room_types = {"kitchen", "bedroom", "living room", "bathroom"}

    # Define lighting levels with corresponding lumen values
    lighting_levels = {"low": 300, "medium": 600, "high": 900}

    # Loop through each room type to gather information on each one
    for room_type in room_types:
        # Ask the user how many rooms of this type are in the apartment
        while True:
            try:
                count = int(input(f"How many {room_type}s are in the apartment? Enter an integer number: "))
                if count < 0:
                    print("The number of rooms cannot be negative. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # For each room of this type, collect specific room settings
        for i in range(count):
            print(f"Settings for {room_type} {i + 1}:")

            # Ask the user to select the lighting level, and validate input
            while True:
                level = input("Select lighting level (low, medium, high): ").lower()
                if level in lighting_levels:
                    break
                else:
                    print("Invalid choice. Please choose 'low', 'medium', or 'high'.")

            # Ask the user to specify the room size and validate input
            while True:
                size = input("Choose room size (small, medium, large): ").lower()
                if size in ["small", "medium", "large"]:
                    break
                else:
                    print("Invalid input. Please choose 'small', 'medium', or 'large'.")

            # Append room details (type, lighting level in lumens, size) to the room_data list
            room_data.append({
                "type": room_type,
                "level": lighting_levels[level],
                "size": size
            })

        # Print a blank line for spacing between room types
        print("\n")

    # Return the list of all room data
    return room_data


def get_bulb_type():
    # Ask the user to select a bulb type, with input validation
    while True:
        bulb_type = input("Choose bulb type (cheap, energy-saving, reliable): ").lower()
        if bulb_type in ["cheap", "energy-saving", "reliable"]:
            return bulb_type
        else:
            print("Invalid choice. Please choose 'cheap', 'energy-saving', or 'reliable'.")
