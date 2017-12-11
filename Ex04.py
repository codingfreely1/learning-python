
def divisors():
    number = raw_input("Enter a number: ")
    print "Here are all the numbers that are divisors of " + number
    for num in range(1, int(number)):
        if int(number) % num == 0:
            print num


def divisors2():
    number = raw_input("Enter a number: ")
    print "Here are all the numbers that are divisors of " + number
    res = [num for num in range(1, int(number)) if int(number) % num == 0]
    print(res)


divisors2()


#Ex8 & Ex20
