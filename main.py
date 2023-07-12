import requests
from datetime import datetime as dt
import os


GENDER = "Your Gender"
WEIGHT = 0 # Your weight in kg
HEIGHT = 0 # Your height in cm
AGE = 0 # Your age in years

APP_ID = "Nutritionix App ID"
API_KEY = "Nutritionix API Key"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=nutritionix_endpoint, json=exercise, headers=headers)
response.raise_for_status()
exercise_data = response.json()

sheety_endpoint = "https://api.sheety.co"

USERNAME = "Sheety Username"
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"

new_sheety_data = {
    "workout": {
        "date": dt.now().strftime("%d/%m/%Y"),
        "time": dt.now().strftime("%H:%M:%S"),
        "exercise": exercise_data['exercises'][0]['name'].title(),
        "duration": float(exercise_data['exercises'][0]['duration_min']),
        "calories": int(exercise_data['exercises'][0]['nf_calories'])
    }
}

headers = {
    "Authorization": "Bearer Sheety API Key"
}

response = requests.post(url=f"{sheety_endpoint}/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}",
                         json=new_sheety_data,
                         headers=headers)
response.raise_for_status()
print(response.text)


# PROJECT NOT FINISHED - need to fix enviorment vars