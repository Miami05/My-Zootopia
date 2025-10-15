import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def print_animals_data(animals_data):
    """Print a simple report for each animal in `animals_data`.
    Only prints fields that exist and are non-empty."""
    if not animals_data:
        return
    if isinstance(animals_data, dict) and "animals" in animals_data:
        animals_data = animals_data["animals"]
    for animal in animals_data:
        if not isinstance(animal, dict):
            continue
        characteristics = animal.get("characteristics") or {}
        if animal.get("name"):
            print(f"Name: {animal['name']}")
        if characteristics.get("diet"):
            print(f"Diet: {characteristics['diet']}")
        locs = animal.get("locations")
        if isinstance(locs, (list, tuple)):
            cleaned = [str(x).strip() for x in locs if str(x).strip()]
            if cleaned:
                label = "Location" if len(cleaned) == 1 else "Locations"
                print(f"{label}: {', '.join(cleaned)}")
        elif isinstance(locs, str) and locs.strip():
            print(f"Location: {locs.strip()}")
        if characteristics.get("type"):
            print(f"Type: {characteristics['type']}")
        print()


def main():
    animals_data = load_data('animals_data.json')
    print_animals_data(animals_data)

if __name__ == "__main__":
    main()