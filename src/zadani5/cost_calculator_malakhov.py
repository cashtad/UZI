def calculate_cost(bulb_counts, bulb_type):
    # Define the price per bulb for each bulb type
    prices = {"cheap": 20, "energy-saving": 150, "reliable": 80}

    # Calculate the total cost by multiplying the bulb count for each room with the price of the selected bulb type
    total_cost = sum(count * prices[bulb_type] for count in bulb_counts)

    # Return the calculated total cost
    return total_cost
