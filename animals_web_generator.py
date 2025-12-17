import json
from pathlib import Path

DATA = Path("animals_data.json")
TEMPLATE = Path("animals_template.html")
OUTPUT = Path("animals.html")

def load_animals(path: Path):
    """ Loading JSON file"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["animals"] if isinstance(data, dict) and "animals" in data else data

def make_animals_text(animals):
    """Return HTML <li> blocks for each animal, printing only existing fields.
    - Name, Diet, Type
    - Locations: prints all if more than one
    """
    if isinstance(animals, dict) and isinstance(animals.get("animals"), list):
        animals_iter = animals["animals"]
    else:
        animals_iter = animals
    parts = []
    for animal in animals_iter or []:
        if not isinstance(animal, dict):
            continue
        ch = animal.get("characteristics") or {}
        name = animal.get("name")
        diet = ch.get("diet")
        a_type = ch.get("type")
        loc_text = ""
        locs = animal.get("locations")
        if isinstance(locs, (list, tuple)):
            loc_text = human_join(locs)
        elif isinstance(locs, str) and locs.strip():
            loc_text = locs.strip()
        meta_items = []
        if diet:
            meta_items.append(
                '          <li class="card__meta-item"><strong class="card__meta-label">Diet:</strong> '
                f'{diet}</li>\n'
            )
        if loc_text:
            meta_items.append(
                '          <li class="card__meta-item"><strong class="card__meta-label">Location:</strong> '
                f'{loc_text}</li>\n'
            )
        if a_type:
            meta_items.append(
                '          <li class="card__meta-item"><strong class="card__meta-label">Type:</strong> '
                f'{a_type}</li>\n'
            )
        if not name and not meta_items:
            continue
        parts.append('<li class="cards__item">\n')
        if name:
            parts.append(f'  <div class="card__title">{name}</div>\n')
        parts.append('  <div class="card__text">\n')
        parts.append('    <ul class="card__meta">\n')
        parts.extend(meta_items)
        parts.append('    </ul>\n')
        parts.append('  </div>\n')
        parts.append('</li>\n')
    return "".join(parts)

def main():
    animals = load_animals(DATA)
    content = make_animals_text(animals)
    template = TEMPLATE.read_text(encoding="utf-8")
    html = template.replace("__REPLACE_ANIMALS_INFO__", content)
    OUTPUT.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
