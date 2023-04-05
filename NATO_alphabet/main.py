import pandas as pd




if __name__ == "__main__":
    df = pd.read_csv("./NATO_alphabet/nato_phonetic_alphabet.csv")
    nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
    
    name = input("Enter the word: ")
    name = list(name.upper())
    nato_alphabet_list = [nato_dict[i] for i in name]
    print(nato_alphabet_list)