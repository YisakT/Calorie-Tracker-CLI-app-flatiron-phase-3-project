from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models import FoodItem, Meal, MealFood
from datetime import datetime
from sqlalchemy import exc


DATABASE_URI = 'sqlite:///calories_tracker.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


def add_food_item(name, calories):
    session = Session()
    try:
        new_item = FoodItem(name=name, calories=calories)
        session.add(new_item)
        session.commit()
    except exc.IntegrityError:  # Handles unique constraint
        session.rollback()
        return False
    finally:
        session.close()
    return True


def add_meal(name, date):
    session = Session()
    try:
        new_meal = Meal(name=name, date=date)
        session.add(new_meal)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()
    return True

def view_food_items():
    session = Session()
    items = session.query(FoodItem).all()
    session.close()
    return items

def view_meals():
    session = Session()
    meals = session.query(Meal).all()
    session.close()
    return meals

def update_food_item(food_id, new_name, new_calories):
    session = Session()
    try:
        item = session.query(FoodItem).filter_by(id=food_id).first()
        if item:
            item.name = new_name
            item.calories = new_calories
            session.commit()
        else:
            return False
    except exc.IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()
    return True


def delete_food_item(food_id):
    session = Session()
    try:
        item = session.query(FoodItem).filter_by(id=food_id).first()
        if item:
            session.delete(item)
            session.commit()
        else:
            return False
    except exc.IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()
    return True


def add_food_to_meal(meal_id, food_id, portion_size):
    session = Session()
    try:
        meal_food = MealFood(meal_id=meal_id, food_item_id=food_id, portion_size=portion_size)
        session.add(meal_food)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()
    return True


def view_foods_in_meal(meal_id):
    session = Session()
    foods = session.query(FoodItem).join(MealFood).join(Meal).filter(Meal.id == meal_id).all()
    session.close()
    return foods

def remove_food_from_meal(meal_id, food_id):
    session = Session()
    try:
        meal_food = session.query(MealFood).filter_by(meal_id=meal_id, food_item_id=food_id).first()
        if meal_food:
            session.delete(meal_food)
            session.commit()
        else:
            return False
    except exc.IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()
    return True

def update_portion_in_meal(meal_id, food_id, new_portion_size):
    session = Session()
    try:
        meal_food = session.query(MealFood).filter_by(meal_id=meal_id, food_item_id=food_id).first()
        if meal_food:
            meal_food.portion_size = new_portion_size
            session.commit()
        else:
            return False
    except exc.IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()
    return True


def search_meal_by_name(name):
    try:
        result = session.query(Meal).filter(Meal.name.like(f"%{name}%")).all()
        for meal in result:
            print(f"ID: {meal.id} - Name: {meal.name} - Calories: {meal.calories}")
    except exc.SQLAlchemyError as e:
        print(f"An error occurred: {str(e)}")


def total_calories_today():
    today = datetime.today().date()
    try:
        meals_today = session.query(Meal).filter(Meal.date == today).all()
        total_calories = sum([meal.calories for meal in meals_today])
        print(f"Total calories consumed today: {total_calories}")
    except exc.SQLAlchemyError as e:
        print(f"An error occurred: {str(e)}")