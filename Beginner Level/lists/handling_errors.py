countries = ["Colombia", "Paraguay", "Costa Rica"]

try:
    num_of_countries = len(countries)
    print(countries[num_of_countries - 1])

except IndexError:
    print("Error")

