

# Nesting a List in a Dictionary
# in this travel log, because you want to add multiple entries per each city, you couldn't just write them
# without making an actual list, since in a dictionary the value can only be one item not multiple
# so if you want multiple items you have to make it be a list
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)


# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log)


# Nesting both a dictionary and a list in a dictionary
dictionary1 = {
    "key_1": ["list_item_1", "list_item_2"],
    "key_2": {"inside_dictionary_key_1": "inside_dictionary_value_1",
              "inside_dictionary_key_2": "inside_dictionary_value_2"}
}
print(dictionary1)
