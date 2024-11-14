def display_results(room_data, bulb_counts, total_cost):
    # Display header for the results section
    print("\nLighting calculation results:")

    # Loop through each room in room_data and its corresponding bulb count
    for i, room in enumerate(room_data):
        # Print the room's details: type, size, required lighting level, and the number of bulbs needed
        print(
            f"{room['type'].capitalize()} (size: {room['size']}, required level: {room['level']} lumens): {bulb_counts[i]} bulbs"
        )

    # Display the total number of bulbs required across all rooms
    print(f"\nTotal number of bulbs: {sum(bulb_counts)}")

    # Display the total cost of all bulbs in Czech currency (CZK)
    print(f"Total cost: {total_cost} cz")
