# animals_to_html.py
import json
from pathlib import Path

DATA     = Path("animals_data.json")
TEMPLATE = Path("animals_template.html")
OUTPUT   = Path("animals.html")

def load_animals(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["animals"] if isinstance(data, dict) and "animals" in data else data

def make_animals_text(animals):
    """Return a text block: only existing fields; print all locations (comma-joined)."""
    blocks = []
    for a in animals:
        if not isinstance(a, dict):
            continue
        characteristic = a.get("characteristics") or {}
        lines = []
        if a.get("name"):
            lines.append(f"Name: {a['name']}")
        if characteristic.get("diet"):
            lines.append(f"Diet: {characteristic['diet']}")
        locs = a.get("locations")
        if isinstance(locs, (list, tuple)):
            cleaned = [str(x).strip() for x in locs if str(x).strip()]
            if cleaned:
                label = "Location" if len(cleaned) == 1 else "Locations"
                lines.append(f"{label}: {', '.join(cleaned)}")
        elif isinstance(locs, str) and locs.strip():
            lines.append(f"Location: {locs.strip()}")
        if characteristic.get("type"):
            lines.append(f"Type: {characteristic['type']}")
        if lines:
            blocks.append("\n".join(lines))

    return "\n\n".join(blocks)

def main():
    animals = load_animals(DATA)
    content = make_animals_text(animals)
    template = TEMPLATE.read_text(encoding="utf-8")
    html = template.replace("__REPLACE_ANIMALS_INFO__", content)
    OUTPUT.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
