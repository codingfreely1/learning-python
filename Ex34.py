import json


def load_birthday_dict(file_name):
    with open(file_name, "r") as f:
        info = json.load(f)
        print info
        return info


def add_new_person(birthday_dict):
    new_person = raw_input("Who's birthday do you want to add?")
    new_b_day = raw_input("When is his/her birthday?")

    if birthday_dict.get(new_person, ""):
        print "person already exist"
    else:
        print "person will be added"
        birthday_dict[new_person] = new_b_day
        to_json = json.dumps(birthday_dict)
        with open('info.json', 'w') as open_file:
            open_file.write(to_json)


def main():
    print "Welcome to the birthday dictionary. We know the birthday of:"
    birthday_dict = load_birthday_dict("info.json")
    for key in birthday_dict.keys():
        print key
    selected = raw_input("Who's birthday do you want to look up?")
    selected_b_day = birthday_dict.get(selected, "")

    if selected_b_day == "":
        print "The input is no good"
    else:
        print "{}'s birthday is {}".format(selected, selected_b_day)

    while raw_input("Do you want to add new birthdays?").lower() == "yes":
        add_new_person(birthday_dict)


main()
