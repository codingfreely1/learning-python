def linear_search(ordered_list, val):
    match = [v for v in ordered_list if v == val]
    print match
    # https://stackoverflow.com/questions/3965104/not-none-test-in-python
    if not match:
        print "Not Found"
    else:
        print "Found"


linear_search([0, 1, 2, 3, 4], 3)


def binary_search(ordered_list, val, start_inx, end_inx):
    res = -1
    if end_inx >= start_inx:
        middle = (start_inx + end_inx) // 2  # 5 / 2 will return 2.5 and 5 // 2 will return 2
        if ordered_list[middle] == val:
            return middle
        res = binary_search(ordered_list, val, start_inx, middle - 1)
        if res == -1:
            res = binary_search(ordered_list, val, middle + 1, end_inx)

    return res


print(binary_search([89, 90, 100, 109], 109, 0, 3))

order_list_from_input = raw_input("Enter your ordered list with space separator:").split()
search_value = raw_input("Which value do you want to search?")
print binary_search(order_list_from_input, search_value, 0, len(order_list_from_input) - 1)


# Check if list a is empty
# if not a:
#   print("List is empty")
