def explain_choices(room_data, bulb_counts, bulb_type):
    # Explanation of why the selected bulb type was chosen
    bulb_reasons = {
        "cheap": "Chosen for its low cost, suitable for temporary or low-priority lighting.",
        "energy-saving": "Chosen for efficiency and reduced electricity costs over time.",
        "reliable": "Chosen for long lifespan and stable lighting quality."
    }

    # Generate explanations for each room
    explanations = []
    for i, room in enumerate(room_data):
        explanation = (
            f"Room: {room['type'].capitalize()} (size: {room['size']}, "
            f"required level: {room['level']} lumens)\n"
            f"Bulbs required: {bulb_counts[i]}. Reason: Based on the room's size and required lumens, "
            f"{bulb_counts[i]} {bulb_type} bulbs were calculated."
        )
        explanations.append(explanation)

    # Add a summary explanation about bulb type choice
    explanations.append(f"\nReason for choosing '{bulb_type}' bulbs: {bulb_reasons[bulb_type]}")

    # Return the complete list of explanations
    return explanations


def display_explanations(explanations):
    print("\nExplanation of lighting decisions:")
    for explanation in explanations:
        print(f"\n{explanation}")
