from crud_operations import (add_meal, view_food_items, view_meals, update_food_item, delete_food_item, search_meal_by_name, total_calories_today)
from config import SessionLocal



def get_valid_number(prompt_message):
    while True:
        try:
            value = int(input(prompt_message))
            return value
        except ValueError:
            print("Please enter a valid number!")

def get_valid_string(prompt_message):
    while True:
        value = input(prompt_message)
        if all(c.isalpha() or c.isspace() for c in value):  
            return value
        else:
            print("Please enter a valid string!")


def get_valid_choice(prompt_message, valid_choices):
    while True:
        value = input(prompt_message)
        if value in valid_choices:
            return value
        else:
            print(f"Invalid choice. Please select from {', '.join(valid_choices)}!")

def main():
    while True:
        print("\nCalorie Tracker CLI")
        print("1. Add a meal")
        print("2. View food items")
        print("3. View meals")
        print("4. Update food item")
        print("5. Delete food item")
        print("6. Search meal by name")
        print("7. View total calories for today")
        print("8. Exit")
        
        choice = get_valid_choice("Enter your choice: ", ["1", "2", "3", "4", "5", "6", "7", "8"])

        if choice == "1":
            name = get_valid_string("Enter meal name: ")
            calories = get_valid_number("Enter calories: ")
            add_meal(name, calories)
        elif choice == "2":
            view_food_items()
        elif choice == "3":
            view_meals()
        elif choice == "4":
            food_id = get_valid_number("Enter food item ID to update: ")
            new_name = get_valid_string("Enter new name for the food item: ")
            new_calories = get_valid_number("Enter new calorie count: ")
            update_food_item(food_id, new_name, new_calories)
        elif choice == "5":
            food_id = get_valid_number("Enter food item ID to delete: ")
            delete_food_item(food_id)
        elif choice == "6":
            name = get_valid_string("Enter the name of the meal to search: ")
            search_meal_by_name(name)
        elif choice == "7":
            total_calories_today()
        elif choice == "8":
            print("Exiting the Calorie Tracker CLI. Goodbye!")
            session.close()  
            break

if __name__ == "__main__":
    main()
