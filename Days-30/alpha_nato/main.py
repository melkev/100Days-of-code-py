import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)


def generate_phonetic():
    user = input("enter a words: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in user]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
