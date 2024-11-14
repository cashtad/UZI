def calculate_bulbs(room_data, bulb_type):
    # Initialize an empty list to store the bulb count for each room
    bulb_counts = []

    # Define the lumen output per bulb type
    lumens_per_bulb = {"cheap": 415, "energy-saving": 480, "reliable": 1000}

    # Loop through each room in the room_data list
    for room in room_data:
        # Define the size factor for each room size to adjust the required lumens
        room_size_factor = {"small": 1, "medium": 1.5, "large": 2}

        # Calculate the total lumens required for the room based on its level and size
        required_lumens = room["level"] * room_size_factor[room["size"]]

        # Calculate the number of bulbs needed by dividing required lumens by the lumen output per bulb
        bulb_count = int(required_lumens / lumens_per_bulb[bulb_type])

        # If there is a remainder, add an additional bulb to meet the required lumens
        bulb_count += 1 if required_lumens % lumens_per_bulb[bulb_type] != 0 else 0

        # Append the calculated bulb count for this room to the bulb_counts list
        bulb_counts.append(bulb_count)

    # Return the list of bulb counts for each room
    return bulb_counts
