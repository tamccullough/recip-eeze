from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import rr_main
from datetime import date
today = date.today()
current_year = date.today().strftime('%Y')

import numpy as np
import pandas as pd
import random

ratings = pd.read_csv('datasets/ratings-s.csv')
users = ratings.userid.unique()

recipeeze = Flask(__name__)
theme = 'cappucino'

@recipeeze.route('/')
def index():
    bg_image = 'static/images/emy-90710FOygrg-unsplash.jpg'
    bg_mobile = 'static/images/food-photographer-david-fedulov-h-R_D-zD8KQ-unsplash.jpg'
    #get the ingredients and search
    ingredients_list = ["What's in your fridge?","List a few things. example; cheddar, broccoli"]
    return render_template('index.html', bg_image = bg_image, bg_mobile = bg_mobile,
    ingredients = ingredients_list,theme = theme)

@recipeeze.route('/recipes', methods=['POST'])
#@login_required
def recipes():
    #posting the results
    bg_image = ''
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    ingredient_list = request.form['ingredients']

    recipe_list1 = rr_main.set_up_ml(user_1,ingredient_list) # generate a list of recommendations for each user
    recipe_list2 = rr_main.set_up_ml(user_2,ingredient_list)
    recipe_list3 = rr_main.set_up_ml(user_3,ingredient_list)

    final_recommendation = rr_main.get_final_recommendation(recipe_list1,recipe_list2,recipe_list3)
    return render_template('recipe.html',
    recipes_table = final_recommendation, bg_image = bg_image,
    ingredients = ingredient_list,theme = theme)

if __name__ == "__main__":
    recipeeze.run()
