import requests
import os
from dotenv import load_dotenv

# Load .env once when the module is imported
load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    }
    """
    if not API_KEY:
        print("Error: API_KEY not found in environment variables.")
        return []

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []
