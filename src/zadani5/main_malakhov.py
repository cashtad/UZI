### TASK 5
### LEONID MALAKHOV
### 14.11.24

# Importing functions from separate modules
from user_input_malakhov import get_room_data, get_bulb_type
from lighting_calculator_malakhov import calculate_bulbs
from cost_calculator_malakhov import calculate_cost
from output_results_malakhov import display_results
from vysvetlovaci_modul_malakhov import explain_choices, display_explanations



# Main function that coordinates the lighting system logic
def main():
    # Introduction for the user
    print("A knowledge system to help you choose lighting for your apartment.")
    print("Answer the following questions to allow the system to determine the required number of bulbs for each room.")
    print("\n\n")

    # Collect user input on room characteristics and lighting preferences
    room_data = get_room_data()

    # Collect user preference for bulb type
    bulb_type = get_bulb_type()

    # Calculate the required number of bulbs for each room based on input
    bulb_counts = calculate_bulbs(room_data, bulb_type)

    # Calculate the total cost of bulbs based on the type and quantity needed
    total_cost = calculate_cost(bulb_counts, bulb_type)

    # Display the results including the required number of bulbs per room and total cost
    display_results(room_data, bulb_counts, total_cost)

    # После расчётов и отображения основных результатов:
    explanations = explain_choices(room_data, bulb_counts, bulb_type)
    display_explanations(explanations)

    # Pauses the program at the end so the user can see the output
    input("STOP")


# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
