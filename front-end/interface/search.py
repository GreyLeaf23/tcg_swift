#!/bin/usr/python3

pokemon_videos = {
    "palafin": "https://www.youtube.com/watch?v=video_id_for_palafin_deck",
    "charizard": "https://www.youtube.com/watch?v=video_id_for_charizard_deck",
    "pikachu": "https://www.youtube.com/watch?v=video_id_for_pikachu_deck"
}

def search_pokemon(pokemon_name):
    cleaned_name = pokemon_name.lower().replace(" ", "")  # Remove spaces and convert to lowercase
    return pokemon_videos.get(cleaned_name, "No video found for that Pokémon")

pokemon_names = ["palafin", "charizard", "pikachu"]
for name in pokemon_names:
    video_link = search_pokemon(name)
    print(f"{name.capitalize()}: {video_link}")