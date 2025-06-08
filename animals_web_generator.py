import data_fetcher


def serialize_animal(animal_obj):
    # ... (same as before)
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
    animal_name = input("Enter a name of an animal: ").strip()

    # Use the data fetcher module instead of fetching directly
    animals_data = data_fetcher.fetch_data(animal_name)

    with open('animals_template.html', 'r') as fileobj:
        content = fileobj.read()

    if animals_data:
        output = ''.join(serialize_animal(animal) for animal in animals_data)
    else:
        output = f"""
        <div style="text-align:center; margin-top: 50px;">
            <h2 style="color: #cc0000;">The animal "{animal_name}" doesn't exist.</h2>
            <p>Please try a different animal name.</p>
        </div>
        """

    html_content = content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open('animals.html', 'w') as fileobj:
        fileobj.write(html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == '__main__':
    main()
