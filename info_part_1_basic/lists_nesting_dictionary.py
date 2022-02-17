
# Nesting Dictionaries in Lists

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

# 🚨 Do NOT change the code above
# assignment: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(add_new_country_name, add_new_country_cities_visited, add_new_country_total_visits):
    new_country = {}
    new_country["country"] = add_new_country_name
    new_country["cities_visited"] = add_new_country_cities_visited
    new_country["total_visits"] = add_new_country_total_visits
    travel_log.append(new_country)


# 🚨 Do not change the code below
print(travel_log)
print("\n")
add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)
