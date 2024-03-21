import json

pokemon_names = [
    "Armarouge", "Artazon", "Charcadet", "Charizard", "Charmander", "Charmeleon", "Chinchou", "Clobbopus", "Cottonee",
    "Electric Generator", "Forretress Ex", "Frigibax", "Grapploct", "Iono", "Iron Treads Ex", "Lanturn", "Lapras",
    "Locked In Shiny Palafin", "Maushold", "Moonlit Hill", "Natu", "Nemona'S Backpack", "Nest Ball", "Noibat", "Noivern Ex",
    "Paldean Clodsire Ex", "Paldean Wooper", "Pikachu", "Pineco", "Professor'S Research", "Raichu", "Rare Candy", "Revavroom",
    "Shiny Armarouge", "Shiny Ceruledge", "Shiny Ditto", "Shiny Finizen", "Shiny Hoppip", "Shiny Mew Ex", "Shiny Mimikyu",
    "Shiny Pachirisu", "Shiny Palafin", "Side Eye Penny", "Tandemaus", "Technical Machine Crisis Punch", "Toedscool",
    "Toedscruel", "Ultra Ball", "Varoom", "Whimsicott", "Zatu"
]

image_filenames = [
    "armarouge.png", "artazon.png", "charcadet.png", "charizard.png", "charmander.png", "charmeleon.png", "chinchou.png",
    "clobbopus.png", "cottonee.png", "electric_generator.png", "forretress_ex.png", "frigibax.png", "grapploct.png", "iono.png",
    "iron_treads_ex.png", "lanturn.png", "lapras.png", "locked_in_shiny_palafin.png", "maushold.png", "moonlit_hill.png",
    "natu.png", "nemona's_backpack.png", "nest_ball.png", "noibat.png", "noivern_ex.png", "paldean_clodsire_ex.png",
    "paldean_wooper.png", "pikachu.png", "pineco.png", "professor's_research.png", "raichu.png", "rare_candy.png", "revavroom.png",
    "shiny_armarouge.png", "shiny_ceruledge.png", "shiny_ditto.png", "shiny_finizen.png", "shiny_hoppip.png", "shiny_mew_ex.png",
    "shiny_mimikyu.png", "shiny_pachirisu.png", "shiny_palafin.png", "side_eye_penny.png", "tandemaus.png",
    "technical_machine_crisis_punch.png", "toedscool.png", "toedscruel.png", "ultra_ball.png", "varoom.png", "whimsicott.png",
    "zatu.png"
]

# Combine the lists into a list of dictionaries
pokemon_data = [{"name": name, "filename": filename} for name, filename in zip(pokemon_names, image_filenames)]

# Write the data to a JSON file
with open('pokemon_cards.json', 'w') as json_file:
    json.dump(pokemon_data, json_file, indent=4)

print("JSON file 'pokemon_cards.json' created successfully.")
