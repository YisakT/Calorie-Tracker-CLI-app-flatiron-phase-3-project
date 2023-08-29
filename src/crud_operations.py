from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models import FoodItem, Meal, MealFood

DATABASE_URI = 'sqlite:///calories_tracker.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


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
