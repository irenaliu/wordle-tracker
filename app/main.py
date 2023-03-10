import csv

def check_if_word_exists(word):
    with open('app/words.csv', 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if word == row[0]:
                return True
        return False

print("Check if your word has already been used before!")

while True:
    user_input = input("Enter a word: ")
    word_exists = check_if_word_exists(word=user_input.lower())
    if word_exists:
        print("Word has already been used before.")
    else:
        print("Word has not been used yet.")
        break

