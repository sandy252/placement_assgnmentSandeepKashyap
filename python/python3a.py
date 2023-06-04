import requests
import pandas as pd

def download_and_convert_to_excel(url):
    # Download data from the provided link
    response = requests.get(url)
    data = response.json()

    # Convert data to properly structured data
    formatted_data = []
    for pokemon in data["pokemon"]:
        multipliers = pokemon.get("multipliers")
        if multipliers is None:
            multipliers = []
        else:
            multipliers = list(map(str, multipliers))
        
        pokemon_data = {
            "id": pokemon["id"],
            "num": pokemon["num"],
            "name": pokemon["name"],
            "img": pokemon["img"],
            "type": ", ".join(pokemon["type"]),
            "height": pokemon["height"],
            "weight": pokemon["weight"],
            "candy": pokemon.get("candy", ""),
            "candy_count": pokemon.get("candy_count", ""),
            "egg": pokemon.get("egg", ""),
            "spawn_chance": pokemon.get("spawn_chance", ""),
            "avg_spawns": pokemon.get("avg_spawns", ""),
            "spawn_time": pokemon.get("spawn_time", ""),
            "multipliers": ", ".join(multipliers),
            "weakness": ", ".join(pokemon.get("weaknesses", []))
        }
        
        if "next_evolution" in pokemon:
            pokemon_data["next_evolution"] = ", ".join(
                [evolution["num"] + " - " + evolution["name"] for evolution in pokemon["next_evolution"]]
            )
        else:
            pokemon_data["next_evolution"] = ""
        
        if "prev_evolution" in pokemon:
            pokemon_data["prev_evolution"] = ", ".join(
                [evolution["num"] + " - " + evolution["name"] for evolution in pokemon["prev_evolution"]]
            )
        else:
            pokemon_data["prev_evolution"] = ""
        
        formatted_data.append(pokemon_data)

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(formatted_data)

    # Save DataFrame to Excel
    excel_filename = "updated_pokemon_data.xlsx"
    df.to_excel(excel_filename, index=False)

    return excel_filename

# Provide the URL for the data
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# Call the function to download, convert, and export the data to Excel
excel_file = download_and_convert_to_excel(url)
print(f"Data downloaded and exported to {excel_file}.")
