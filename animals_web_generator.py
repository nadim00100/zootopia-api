import requests


def fetch_animal_data(name):
    """Fetch animal data from the API."""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    headers = {'X-Api-Key': 'oesLxIwq+McVd7lwocWkxw==TsdRlaC9UShkQgsa'}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []


def serialize_animal(animal_obj):
    """Generate HTML list item for a single animal."""
    name = animal_obj.get('name', 'Unknown')
    diet = animal_obj.get('characteristics', {}).get('diet', 'Unknown')
    locations = animal_obj.get('locations', [])
    location = locations[0] if locations else 'Unknown'
    animal_type = animal_obj.get('characteristics', {}).get('type', 'Unknown')

    return f"""
    <li class="cards__item">
        <div class="card">
            <div class="card__content">
                <h2 class="card__title">{name}</h2>
                <p><strong>Diet:</strong> {diet}</p>
                <p><strong>Location:</strong> {location}</p>
                <p><strong>Type:</strong> {animal_type}</p>
            </div>
        </div>
    </li>
    """


def main():
    # Ask the user for the animal name
    animal_name = input("Enter a name of an animal: ").strip()

    # Fetch data from the API for the user-entered animal
    animals_data = fetch_animal_data(animal_name)

    # Load HTML template
    with open('animals_template.html', 'r') as fileobj:
        content = fileobj.read()

    if animals_data:
        # Build the output string with animal info
        output = ''.join(serialize_animal(animal) for animal in animals_data)
    else:
        # Generate a nice error message if no animals found
        output = f"""
        <div style="text-align:center; margin-top: 50px;">
            <h2 style="color: #cc0000;">The animal "{animal_name}" doesn't exist.</h2>
            <p>Please try a different animal name.</p>
        </div>
        """

    # Replace the placeholder with the actual animal info or error message
    html_content = content.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write to a new HTML file
    with open('animals.html', 'w') as fileobj:
        fileobj.write(html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == '__main__':
    main()
