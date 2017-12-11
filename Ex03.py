a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def sol0():
    for i in a:
        if i < 5:
            print(i)


def sol1(arr, threshold):
    output = []
    for i in arr:
        if i < threshold:
            output.append(i)
    print(output)


def sol3():
    threshold = raw_input("Enter a number")
    print("Here are all the numbers smaller then " + threshold + ":")
    sol1(a, int(threshold))


# sol0
# sol1
sol3()
