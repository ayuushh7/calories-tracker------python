# [Task 1] Header
# Name: [Your Name Here]
# Date: [Current Date]
# Project Title: Daily Calorie Tracker CLI [cite: 1, 24]

# Import datetime for the bonus task (timestamp) [cite: 59]
import datetime

def main():
    # --- Task 1: Setup & Introduction ---
    print("=============================================")
    print("   Welcome to the Daily Calorie Tracker!   ")
    print("=============================================")
    print("This tool helps you log meals, track total calories,")
    print("and compare against your daily limit. [cite: 11, 25]\n")

    # --- Task 2: Input & Data Collection ---
    meal_names = []  # [cite: 31]
    calorie_amounts = [] # [cite: 31]
    num_meals = 0

    # Ask how many meals to enter, with error handling
    while True:
        try:
            num_meals = int(input("How many meals would you like to enter?  "))
            if num_meals > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print() # Add a newline for spacing

    # Loop to collect meal data
    for i in range(num_meals):
        print(f"--- Entering Meal #{i + 1} ---")
        
        # Get meal name
        meal_name = input("Enter meal name (e.g., Breakfast):  ")
        meal_names.append(meal_name)
        
        # Get calorie amount with error handling
        while True:
            try:
                calorie_amount = float(input(f"Enter calorie amount for {meal_name}:  "))
                if calorie_amount >= 0:
                    calorie_amounts.append(calorie_amount)
                    break
                else:
                    print("Calories must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for calories.")
        print() # Add a newline

    # --- Task 3: Calorie Calculations ---
    total_calories = sum(calorie_amounts) # [cite: 35, 37]
    
    # Avoid division by zero if no meals were entered (though our loop prevents this)
    if num_meals > 0:
        average_calories = total_calories / num_meals # [cite: 36, 37]
    else:
        average_calories = 0

    # Get daily calorie limit with error handling 
    daily_limit = 0
    while True:
        try:
            daily_limit = float(input("What is your daily calorie limit? ")) # 
            if daily_limit > 0:
                break
            else:
                print("Please enter a positive number for your limit.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("\n... Calculating results ...\n")

    # --- Task 5: Neatly Formatted Output ---
    # This section is placed before Task 4's output for better flow
    
    print("=============================================")
    print("           YOUR DAILY SUMMARY                ")
    print("=============================================\n")
    
    # Print the formatted table header [cite: 46, 47, 48]
    # Using f-strings and tabs (\t) for alignment [cite: 17, 54]
    print(f"Meal Name\t\tCalories\n----------------------------------------") # [cite: 54]
    
    # Loop through lists to print meal data [cite: 49, 50, 51]
    for i in range(len(meal_names)):
        # \t\t for alignment
        print(f"{meal_names[i]:<15}\t\t{calorie_amounts[i]:>8.2f}") # Using formatting for alignment

    print("----------------------------------------")
    # Print Total and Average [cite: 52, 53]
    print(f"{'Total:':<15}\t\t{total_calories:>8.2f}")
    print(f"{'Average:':<15}\t\t{average_calories:>8.2f}")
    print(f"{'Your Limit:':<15}\t\t{daily_limit:>8.2f}")
    print("\n=============================================\n")

    # --- Task 4: Exceed Limit Warning System ---
    # Use comparison operators [cite: 16, 41]
    if total_calories > daily_limit:
        # Show warning message [cite: 42]
        print(f"*** WARNING! ***")
        print(f"You exceeded your daily limit of {daily_limit} by {total_calories - daily_limit:.2f} calories.")
    else:
        # Show success message [cite: 43]
        print(f"*** SUCCESS! ***")
        print(f"You are within your daily limit. You have {daily_limit - total_calories:.2f} calories remaining.")
    
    print("\n=============================================\n")

    # --- Task 6 (Bonus): Save Session Log to File ---
    save_report = input("Would you like to save this report to a file? (yes/no): ").strip().lower() # 
    
    if save_report in ['y', 'yes']:
        try:
            # Get current timestamp [cite: 59]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            filename = "calorie_log.txt" # 
            
            # Use 'a' (append) mode instead of 'w' (write) [cite: 58]
            # This prevents overwriting old logs.
            with open(filename, "a") as file: # [cite: 58]
                file.write("=====================================\n")
                file.write(f"SESSION LOG: {timestamp}\n") # [cite: 59]
                file.write("-------------------------------------\n")
                
                # Write meal details [cite: 59]
                for i in range(len(meal_names)):
                    file.write(f"- {meal_names[i]}: {calorie_amounts[i]:.2f} calories\n")
                    
                file.write("-------------------------------------\n")
                # Write summary [cite: 59]
                file.write(f"Total Calories: {total_calories:.2f}\n")
                file.write(f"Average Calories: {average_calories:.2f}\n")
                file.write(f"Daily Limit: {daily_limit:.2f}\n")
                
                # Write limit status [cite: 59]
                if total_calories > daily_limit:
                    file.write(f"Status: Exceeded limit by {total_calories - daily_limit:.2f} calories.\n")
                else:
                    file.write(f"Status: Within limit. {daily_limit - total_calories:.2f} calories remaining.\n")
                
                file.write("=====================================\n\n")
            
            print(f"\nSuccessfully saved report to {filename}!") # 
            
        except Exception as e:
            print(f"\nError: Could not save file. {e}")
    else:
        print("\nReport not saved.")

    print("\nThank you for using the Calorie Tracker!")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()