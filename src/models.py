from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class FoodItem(Base):
    __tablename__ = 'food_items'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    calories = Column(Integer, nullable=False)

    # Relationship with MealFood association table
    meals = relationship('MealFood', back_populates='food_item')

class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship with MealFood association table
    food_items = relationship('MealFood', back_populates='meal')

# Association table for many-to-many relationship
class MealFood(Base):
    __tablename__ = 'meal_food'

    meal_id = Column(Integer, ForeignKey('meals.id'), primary_key=True)
    food_item_id = Column(Integer, ForeignKey('food_items.id'), primary_key=True)

    # Relationship to the above tables
    meal = relationship('Meal', back_populates='food_items')
    food_item = relationship('FoodItem', back_populates='meals')
