from sqlalchemy import create_engine, exc, func
from sqlalchemy.orm import sessionmaker
from models import FoodItem, Meal, MealFood
from datetime import datetime
import pytz

DATABASE_URI = 'sqlite:///calories_tracker.db'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)


def add_food_item(name, calories):
    session = SessionLocal()
    try:
        new_item = FoodItem(name=name, calories=calories)
        session.add(new_item)
        session.commit()
        return True, "Food item added successfully!"
    except exc.IntegrityError:
        session.rollback()
        return False, "A food item with this name already exists."
    finally:
        session.close()


def add_meal(name, calories):
    session = SessionLocal()
    try:
        food_item = session.query(FoodItem).filter_by(name=name).first()
        if not food_item:
            food_item = FoodItem(name=name, calories=calories)
            session.add(food_item)
        
        # Get the current date without the time
        today_date = datetime.today().date()

        meal = Meal(name=name, date=today_date)
        session.add(meal)
        session.flush()

        meal_food = MealFood(meal_id=meal.id, food_item_id=food_item.id)
        session.add(meal_food)
        session.commit()

        return True, "Meal added successfully!"
    except exc.IntegrityError:
        session.rollback()
        return False, "An error occurred while adding the meal."
    finally:
        session.close()


def view_food_items():
    session = SessionLocal()
    try:
        items = session.query(FoodItem).all()
        return items
    finally:
        session.close()


def view_meals():
    session = SessionLocal()
    try:
        meals = session.query(Meal).all()
        if not meals:
            return "No meals available. Please add a meal."
        return meals
    finally:
        session.close()


def update_food_item(food_id, new_name, new_calories):
    session = SessionLocal()
    try:
        item = session.query(FoodItem).filter_by(id=food_id).first()
        if item:
            item.name = new_name
            item.calories = new_calories
            session.commit()
            return True, "Food item updated successfully!"
        else:
            return False, "Food item not found."
    except exc.IntegrityError:
        session.rollback()
        return False, "An error occurred during the update."
    finally:
        session.close()


def delete_food_item(food_id):
    session = SessionLocal()
    try:
        item = session.query(FoodItem).filter_by(id=food_id).first()
        if item:
            # Delete or update associated MealFood instances
            meal_foods = session.query(MealFood).filter_by(food_item_id=food_id).all()
            for meal_food in meal_foods:
                session.delete(meal_food)

            # Update or delete associated Meal instances
            meals_with_deleted_food = session.query(Meal).filter(Meal.food_items.any(food_item_id=food_id)).all()
            for meal in meals_with_deleted_food:
                meal.food_items = [mf for mf in meal.food_items if mf.food_item_id != food_id]

            session.delete(item)
            session.commit()
            return True, "Food item deleted successfully!"
        else:
            return False, "Food item not found."
    except exc.IntegrityError:
        session.rollback()
        return False, "An error occurred during the deletion."
    finally:
        session.close()




def add_food_to_meal(meal_id, food_id, portion_size):
    session = SessionLocal()
    try:
        meal_food = MealFood(meal_id=meal_id, food_item_id=food_id, portion_size=portion_size)
        session.add(meal_food)
        session.commit()
        return True, "Food added to meal successfully!"
    except exc.IntegrityError:
        session.rollback()
        return False, "An error occurred while adding food to the meal."
    finally:
        session.close()


def view_foods_in_meal(meal_id):
    session = SessionLocal()
    try:
        foods = session.query(FoodItem).join(MealFood).join(Meal).filter(Meal.id == meal_id).all()
        return foods
    finally:
        session.close()


def remove_food_from_meal(meal_id, food_id):
    session = SessionLocal()
    try:
        meal_food = session.query(MealFood).filter_by(meal_id=meal_id, food_item_id=food_id).first()
        if meal_food:
            session.delete(meal_food)
            session.commit()
            return True, "Food removed from meal successfully!"
        else:
            return False, "Food not found in the meal."
    except exc.IntegrityError:
        session.rollback()
        return False, "An error occurred while removing food from the meal."
    finally:
        session.close()


def update_portion_in_meal(meal_id, food_id, new_portion_size):
    session = SessionLocal()
    try:
        meal_food = session.query(MealFood).filter_by(meal_id=meal_id, food_item_id=food_id).first()
        if meal_food:
            meal_food.portion_size = new_portion_size
            session.commit()
            return True, "Portion size updated successfully!"
        else:
            return False, "Food not found in the meal."
    except exc.IntegrityError:
        session.rollback()
        return False, "An error occurred during the update."
    finally:
        session.close()


def search_meal_by_name(name):
    session = SessionLocal()
    try:
        result = session.query(Meal).filter(Meal.name.like(f"%{name}%")).all()
        return result
    except exc.SQLAlchemyError:
        return []
    finally:
        session.close()




def total_calories_today():
    today = datetime.today().date()
    session = SessionLocal()
    try:
        meals_today = session.query(Meal).filter(func.date(Meal.date) == today).all()
        total_calories = sum([sum([meal_food.food_item.calories for meal_food in meal.food_items]) for meal in meals_today])
        return total_calories
    except exc.SQLAlchemyError as e:
        print("Error:", e)
        return None
    finally:
        session.close()



