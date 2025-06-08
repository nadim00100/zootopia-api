import json


def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Generate HTML list item for a single animal."""
    name = animal_obj.get('name', 'Unknown')
    diet = animal_obj.get('characteristics', {}).get('diet', 'Unknown')
    locations = ', '.join(animal_obj.get('locations', []))
    animal_type = animal_obj.get('characteristics', {}).get('type', 'Unknown')

    return f"""
    <li class="cards__item">
        <div class="card">
            <div class="card__content">
                <h2 class="card__title">{name}</h2>
                <p><strong>Diet:</strong> {diet}</p>
                <p><strong>Locations:</strong> {locations}</p>
                <p><strong>Type:</strong> {animal_type}</p>
            </div>
        </div>
    </li>
    """


def main():
    # Load JSON data
    animals_data = load_data('animals_data.json')

    # Load HTML template
    with open('animals_template.html', 'r') as fileobj:
        content = fileobj.read()

    # Build the output string with animal info
    output = ''.join(serialize_animal(animal) for animal in animals_data)

    # Replace the placeholder with the actual animal info
    html_content = content.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write to a new HTML file
    with open('animals.html', 'w') as fileobj:
        fileobj.write(html_content)


if __name__ == '__main__':
    main()
