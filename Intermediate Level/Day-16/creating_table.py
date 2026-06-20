from prettytable import PrettyTable

TYPES = [
    "Electric",
    "Water",
    "Fire"
]


POKEMONS = [
    "Pikachu",
    "Squirtle",
    "Charmander"
]

table = PrettyTable()


table.add_column("Pokémon Name", POKEMONS)
table.add_column("Type", TYPES)
table.align = "l"

print(table)

