def is_num1_multiple_of_num2(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


def step1():
    num = raw_input("Enter a number: ")
    if int(num) % 2 == 0:
        print(num + " is even")
    else:
        print(num + " is odd")


def main():
    num1 = raw_input("Enter a number: ")
    num2 = raw_input("Enter a number: ")
    print("Is " + num1 + " multiply of " + num2 + "?")
    print(is_num1_multiple_of_num2(int(num1), int(num2)))


main()


