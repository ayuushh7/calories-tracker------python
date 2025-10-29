import datetime
def main():
    
    print("=============================================")
    print("   Welcome to the Daily Calorie Tracker!   ")
    print("=============================================")
    print("This tool helps you log meals, track total calories,")
    print("and compare against your daily limit. [cite: 11, 25]\n")

   
    meal_names = []  
    calorie_amounts = [] 
    num_meals = 0

    
    while True:
        try:
            num_meals = int(input("How many meals would you like to enter?  "))
            if num_meals > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print() 

  
    for i in range(num_meals):
        print(f"--- Entering Meal #{i + 1} ---")
        
        
        meal_name = input("Enter meal name (e.g., Breakfast):  ")
        meal_names.append(meal_name)
        
        
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
        print() 

    
    total_calories = sum(calorie_amounts)
    
   
    if num_meals > 0:
        average_calories = total_calories / num_meals
    else:
        average_calories = 0

    
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

    
    
    print("=============================================")
    print("           YOUR DAILY SUMMARY                ")
    print("=============================================\n")
    
    
    print(f"Meal Name\t\tCalories\n----------------------------------------") 
    
   
    for i in range(len(meal_names)):
        
        print(f"{meal_names[i]:<15}\t\t{calorie_amounts[i]:>8.2f}") # Using formatting for alignment

    print("----------------------------------------")
    
    print(f"{'Total:':<15}\t\t{total_calories:>8.2f}")
    print(f"{'Average:':<15}\t\t{average_calories:>8.2f}")
    print(f"{'Your Limit:':<15}\t\t{daily_limit:>8.2f}")
    print("\n=============================================\n")

    
    if total_calories > daily_limit:
        
        print(f"*** WARNING! ***")
        print(f"You exceeded your daily limit of {daily_limit} by {total_calories - daily_limit:.2f} calories.")
    else:
        
        print(f"*** SUCCESS! ***")
        print(f"You are within your daily limit. You have {daily_limit - total_calories:.2f} calories remaining.")
    
    print("\n=============================================\n")

   
    save_report = input("Would you like to save this report to a file? (yes/no): ").strip().lower() # 
    
    if save_report in ['y', 'yes']:
        try:
           
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            filename = "calorie_log.txt" # 
            
            
            with open(filename, "a") as file: # [cite: 58]
                file.write("=====================================\n")
                file.write(f"SESSION LOG: {timestamp}\n") # [cite: 59]
                file.write("-------------------------------------\n")
                
                
                for i in range(len(meal_names)):
                    file.write(f"- {meal_names[i]}: {calorie_amounts[i]:.2f} calories\n")
                    
                file.write("-------------------------------------\n")
              
                file.write(f"Total Calories: {total_calories:.2f}\n")
                file.write(f"Average Calories: {average_calories:.2f}\n")
                file.write(f"Daily Limit: {daily_limit:.2f}\n")
                
                
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


if __name__ == "__main__":
    main()