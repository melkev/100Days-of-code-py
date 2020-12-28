from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemon name", ["pikachu", "salameche", "lagron"])
table.add_column("Type", ["electric" , "eau" , "feu"])

table.align = "l"

print(table)
