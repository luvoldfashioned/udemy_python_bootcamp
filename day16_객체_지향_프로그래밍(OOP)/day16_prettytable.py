from prettytable import PrettyTable

# object   class
table = PrettyTable()

# call method
table.add_column("pokemon",
                 ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", 
                 ["Electric", "Water", "Fire"])

# attribute edit
table.align = "l"

print(table)