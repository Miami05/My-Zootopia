
# My-Zootopia

Interactive, data-driven animal encyclopedia site. Uses Python and HTML/CSS to let you explore a rich catalog of animals, their types, diets, and habitats—automatically generated from a structured JSON dataset.

## Features

- **Comprehensive Animal Catalog**: Explore a variety of animals with essential details (name, type, diet, location)
- **Auto HTML Generation**: Uses a Python script to convert animal data into stylish HTML
- **Easy to Update**: Add or edit animals in a single JSON file
- **Neat UI**: Responsive layout and clear organization for browsing animal facts
- **Apache 2.0 License**: Free and open source

## Tech Stack

- **Python 3**: For data processing and HTML generation
- **HTML/CSS**: Presentation/layout of animal catalog

## Project Structure

My-Zootopia/  
├── animals_data.json # Animal data (edit this to update encyclopedia)  
├── animals_template.html # HTML template (with placeholder)  
├── animals_web_generator.py # Python script to generate output HTML  
├── animals.html # Output: animal encyclopedia (generated)  
├── LICENSE # Apache 2.0 License  
└── ... (settings/config files)


## Usage

1. **Install Python 3** (if needed)

2. **Edit Data:**
   - Make changes or add new animals in `animals_data.json` (structure: name, type, diet, locations).

3. **Generate the Website:**
```bash
python animals_web_generator.py
```
- This will create/update `animals.html` using the latest data.

4. **Open the Encyclopedia:**
- Double-click `animals.html` or open it in a web browser to explore!

## Example Animal Data

```
{  
"animals": [  
{  
"name": "Lion",  
"characteristics": {  
"diet": "Carnivore",  
"type": "Mammal"  
},  
"locations": ["Africa", "India"]  
},  
...  
]  
}
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enrich the animal catalog or site features.

## License

This project is licensed under the Apache-2.0 License—see the [LICENSE](LICENSE) file for details.

Enjoy your adventure in My-Zootopia!
