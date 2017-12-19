birthday_dict = {"Albert Einstein": "March 14, 1879",
                 "Benjamin Franklin": "01/17/1706",
                 "Ada Lovelace": "December 10, 1815"}


def main():
    print "Welcome to the birthday dictionary. We know the birthday of:"
    for key in birthday_dict.keys():
        print key
    selected = raw_input("Who's birthday do you want to look up?")
    selected_b_day = birthday_dict.get(selected, "")

    if selected_b_day == "":
        print "The input is no good"
    else:
        print "{}'s birthday is {}".format(selected, selected_b_day)


main()
