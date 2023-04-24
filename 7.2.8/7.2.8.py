import json


def load_questions(file):
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def show_field(data):

    for i in data["questions"].items():
        str1 = ""
        str1 += i[0].ljust(13)
        for x in i[1].items():
            if not x[1]["asked"]:
                str1 += x[0].ljust(5)
            else:
                str1 += "---".ljust(5)
        print(str1.ljust(30))

def parse_input():
    user_input = input("Выбираем:")
    topic, price = user_input.split(" ")
    print(data_json["questions"][topic][price])


# _____
data_json = load_questions("questions.json")
print(data_json)
show_field(data_json)
parse_input()
