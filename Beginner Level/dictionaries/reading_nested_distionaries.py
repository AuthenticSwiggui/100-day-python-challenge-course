travel_log = {
    "France": ["Paris", "Marseille", "Lyon"],
    "Germany": ["Berlin", "Munich", "Hamburg"]
}

for key in travel_log:
    print(key)
    for city in travel_log[key]:
        print(f"- {city}")

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])