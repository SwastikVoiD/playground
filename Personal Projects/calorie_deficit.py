# Function to calculate the deficit
def calculate_deficit(tdee, total_intake, target_deficit):
    target_calories = tdee - target_deficit
    calories_left = target_calories - total_intake
    return calories_left

# Function to track food intake
def track_intake():
    total_intake = 0
    print("Enter your food items for today:")
    while True:
        food_item = input("Enter food item (or 'done' to finish): ").strip()
        if food_item.lower() == 'done':
            break
        calories = input(f"Enter the calories for {food_item}: ").strip()
        try:
            calories = int(calories)
            total_intake += calories
        except ValueError:
            print("Invalid input. Please enter a valid number for calories.")
    
    return total_intake

# Main function
def main():
    # User's data
    tdee = 3045  # Total Daily Energy Expenditure (TDEE)
    target_deficit = 1500  # Desired calorie deficit for the day
    
    # Track food intake
    total_intake = track_intake()
    
    # Calculate remaining calories to maintain the deficit
    calories_left = calculate_deficit(tdee, total_intake, target_deficit)
    
    # Output results
    print(f"\nYour total calorie intake so far: {total_intake} calories")
    print(f"You can eat {calories_left} more calories to maintain your {target_deficit} kcal deficit today.")
    if calories_left < 0:
        print("You've exceeded your target deficit. Consider adjusting your intake to stay within your goal.")

# Run the program
if __name__ == "__main__":
    main()