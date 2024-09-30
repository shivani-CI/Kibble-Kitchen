import requests
import logging
import sys
import os
sys.path.append(os.path.abspath('/workspace/Kibble-Kitchen'))
import env

logging.basicConfig(level=logging.INFO)
NUTRIENTS_OF_INTEREST = ['calories', 'protein', 'fat', 'carbs', 'fiber']
LABEL_RENAME_DICT = {
    'calories': 'ENERC_KCAL',
    'protein': 'PROCNT',
    'fat': 'FAT',
    'carbs': 'CHOCDF',
    'fiber': 'FIBER'
}

def extract_nutrition_data(nutrition_info, nutrition_type):
    try:
        edamam_label = LABEL_RENAME_DICT[nutrition_type]
        nutrition_amount = nutrition_info[edamam_label]['quantity']
    except KeyError:
        nutrition_amount = 0
    return nutrition_amount

def get_nutrition_info(recipe_title, recipe_ingredients):
    """
    Fetch nutrition information for a given ingredient with quantity/unit using Edamam's Nutrition API.
    recipe_ingredients should be a list of ingredients with quantity and unit
    """
    app_id = os.getenv("EDAMAM_APP_ID")
    app_key = os.getenv("EDAMAM_KEY_ID")
    url = f'https://api.edamam.com/api/nutrition-details?app_id={app_id}&app_key={app_key}'
    recipe_data = {
        'title': recipe_title,
        'ingr': recipe_ingredients
    }
    
    try:   
        response = requests.post(url, json=recipe_data)
        response.raise_for_status()
        
        nutrition_info = response.json().get('totalNutrients', {})
        nutrition_output = {
            nutrition_type: extract_nutrition_data(nutrition_info, nutrition_type)
            for nutrition_type in NUTRIENTS_OF_INTEREST}
        return nutrition_output
    
    except requests.exceptions.RequestException as exc:
        logging.error(f'Error getting nutrition info from edamam api: {exc}')
        empty_dict = {
            nutrition_type: 0 for nutrition_type in NUTRIENTS_OF_INTEREST}
        return empty_dict
        