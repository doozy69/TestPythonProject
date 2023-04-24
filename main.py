import random

words = ["code", "bit", "soul", "next"]
answers = []
morse_alphabet = {"A": ".-", "B": "-...",
                  "C": "-.-.",
                  "D": "-..",
                  "E": ".",
                  "F": "..-.",
                  "G": "--.",
                  "H": "....",
                  "I": "..",
                  "J": ".---",
                  "K": "-.-",
                  "L": ".-..",
                  "M": "--",
                  "N": "-.",
                  "O": "---",
                  "P": ".--.",
                  "Q": "--.-",
                  "R": ".-.",
                  "S": "...",
                  "T": "-",
                  "U": "..-",
                  "V": "...-",
                  "W": ".--",
                  "X": "-..-",
                  "Y": "-.--",
                  "Z": "--..",
                  " ": "/"}


def morse_encode(word):
    morse_string = ""
    for letter in word:
        morse_string += morse_alphabet[letter.upper()] + " "
    return morse_string


def get_word(list_words):
    return random.sample(list_words, 1)[0]


def print_stats():
    correct = 0
    for i in answers:
        if i:
            correct += 1

    print(f"Всего задачек:",len(answers),
          "\nОтвечено верно:", correct,
          "\nОтвечено неверно:", len(answers)-correct)
print("Погнали!")
for i in range(len(words)):
    random_word = get_word(words)
    words.pop(words.index(random_word))
    print("Слово ", i, " ", morse_encode(random_word))
    if input("Ваш ответ: ") == random_word:
        answers.append(True)
        print("Верно!")
    else:
        answers.append(False)
        print("Неверно, было загадано: ", random_word)
        print()


print_stats()
