Calorie Tracker CLI App

The Calorie Tracker CLI App is a command-line interface application that allows users to track their meals, food items, and daily calorie consumption. Users can add meals, view food items, update food items, delete food items, search for meals by name, and view their total calories consumed for the day.


Getting Started

Prerequisites

Before using the Calorie Tracker CLI App, make sure you have the following prerequisites installed:

Python 3.x
SQLite (for the database)

Installation
Clone the repository to your local machine:

bash
Copy code

git clone https://github.com/YisakT/Calorie-Tracker-CLI-app-flatiron-phase-3-project

Navigate to the project directory:

bash
Copy code
cd calorie-tracker-cli
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
To use the Calorie Tracker CLI App, follow these instructions:

Navigate to the src directory of the project:

bash
Copy code
cd src
Run the CLI app:

bash
Copy code
python cli.py

Adding a Meal
Choose option 1: "Add a meal."

Enter the meal name.
Enter the calorie count for the meal.

Viewing Food Items
Choose option 2: "View food items."

The app will display a list of available food items along with their IDs and calories.
Viewing Meals

Choose option 3: "View meals."
The app will display a list of recorded meals along with their IDs and dates.

Updating Food Item
Choose option 4: "Update food item."

Enter the ID of the food item you want to update.
Enter the new name and new calorie count for the food item.

Deleting Food Item
Choose option 5: "Delete food item."
Enter the ID of the food item you want to delete.

Searching Meal by Name
Choose option 6: "Search meal by name."
Enter the name (or part of the name) of the meal you want to search for.

Viewing Total Calories
Choose option 7: "View total calories for today."
The app will display the total calories consumed for the current day.

Contributing
Contributions are welcome! If you'd like to contribute to the Calorie Tracker CLI App, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.

