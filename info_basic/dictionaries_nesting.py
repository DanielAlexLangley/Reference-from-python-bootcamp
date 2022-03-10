
# DICTIONARIES
# NESTING
# NEST A LIST (INSIDE A DICTIONARY) AS A VALUE
# NEST A DICTIONARY (INSIDE A DIFFERENT DICTIONARY) AS A VALUE, AND THAT DICTIONARY CAN HAVE A NESTED LIST INSIDE IT


# Nesting a list in a dictionary:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)


# Nesting a dictionary in a dictionary:
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log)


# Nesting both a dictionary and a list in a dictionary:
dictionary1 = {
    "key_1": ["list_item_1", "list_item_2"],
    "key_2": {"inside_dictionary_key_1": "inside_dictionary_value_1",
              "inside_dictionary_key_2": "inside_dictionary_value_2"}
}
print(dictionary1)
