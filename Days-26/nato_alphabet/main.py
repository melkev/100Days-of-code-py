import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("enter a words: ").upper()

output_list = [nato_dict[letter] for letter in user]

print(output_list)
