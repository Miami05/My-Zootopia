import json
from pathlib import Path

DATA = Path("animals_data.json")
TEMPLATE = Path("animals_template.html")
OUTPUT = Path("animals.html")

def load_animals(path: Path):
    """ Loading JSON file"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["animals"] if isinstance(data, dict) and "animals" in data else data


def human_join(items):
    items = [item for item in items if isinstance(item, str) and item.strip()]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])} and {items[-1]}"

def make_animals_text(animals):
    """Return a text block: only existing fields; print all locations (comma-joined)."""
    parts = []
    for a in animals:
        if not isinstance(a, dict):
            continue
        ch = a.get("characteristics") or {}
        name = a.get("name")
        diet = ch.get("diet")
        a_type = ch.get("type")
        locs = a.get("locations")
        loc_text = None
        if isinstance(locs, (list, tuple)):
            loc_text = human_join(locs)
        elif isinstance(locs, str) and locs.strip():
            loc_text = locs.strip()
        lines = []
        if diet:
            lines.append(f'      <strong>Diet:</strong> {diet}<br/>\n')
        if loc_text:
            lines.append(f'      <strong>Location:</strong> {loc_text}<br/>\n')
        if a_type:
            lines.append(f'      <strong>Type:</strong> {a_type}<br/>\n')
        if name or lines:
            item = ['<li class="cards__item">\n']
            if name:
                item.append(f'  <div class="card__title">{name}</div>\n')
            item.append('  <p class="card__text">\n')
            if lines:
                item.extend(lines)
            item.append('  </p>\n')
            item.append('</li>\n')
            parts.append("".join(item))
    return "".join(parts)

def main():
    animals = load_animals(DATA)
    content = make_animals_text(animals)
    template = TEMPLATE.read_text(encoding="utf-8")
    html = template.replace("__REPLACE_ANIMALS_INFO__", content)
    OUTPUT.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
