"""
Nesting
{
    key: [List],
    Key2: {Dict},
}
"""
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "stuttgart"]
}

#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionary in a List
travel_log = [
    {"country": "France",
     "cities_visited" : ["Paris", "Lille", "Dijon"],
     "total_visits": 12
    },
    {"country": "Germany",
     "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
    },
]