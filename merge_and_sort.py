# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Dec. 20, 2022
# This program adds two lists together and then sorts them

# concatenates the two input lists then sorts them least to greatest
def merge_and_sort_least_to_greatest(list1, list2):
    # concatenates the two input lists
    final_list = list1 + list2

    # sorts the list
    for counter in range(0, len(final_list) - 1):
        for i in range(0, len(final_list) - 1):
            # checks if the current number is less than or equal to the next number
            if (final_list[i] < final_list[i + 1]) | (
                final_list[i] == final_list[i + 1]
            ):
                continue
            # if the current number is greater than the next number
            elif final_list[i] > final_list[i + 1]:
                # then swap it with the next number
                temp = final_list[i]
                final_list[i] = final_list[i + 1]
                final_list[i + 1] = temp
    return final_list


# concatenates the two input lists then sorts them greatest to least
def merge_and_sort_greatest_to_least(list1, list2):
    # concatenates the two input lists
    final_list = list1 + list2

    # sorts the list
    for counter in range(0, len(final_list) - 1):
        for i in range(0, len(final_list) - 1):
            # checks if the current number is less than or equal to the next number
            if (final_list[i] > final_list[i + 1]) | (
                final_list[i] == final_list[i + 1]
            ):
                continue
            # if the current number is greater than the next number
            elif final_list[i] < final_list[i + 1]:
                # then swap it with the next number
                temp = final_list[i]
                final_list[i] = final_list[i + 1]
                final_list[i + 1] = temp
    return final_list


# creates a number line with the numbers separated by the correct amount compared to each other
def number_line(sort_list, line_length):
    # initialize all required variables
    current_pos = 0
    num = 0
    diff = sort_list[len(sort_list) - 1] - sort_list[0]
    num_per_char = diff / line_length

    # create the list one character at a time
    while True:
        length = len(list(str(sort_list[0])))
        if current_pos == 0:
            print(sort_list[0], end="")
            offset = (sort_list[0] / num_per_char) + 1
            current_pos += offset
            current_pos += length
            sort_list.pop(0)
        if current_pos * num_per_char > sort_list[0]:
            print(sort_list[0], end="")
            current_pos += length
            sort_list.pop(0)
        else:
            print("_", end="")
        if current_pos >= (line_length + offset):
            print()
            break
        current_pos += 1


def main():
    print("This program requires you to input two lists")
    print("then it adds and sorts them greatest to least or least to greatest")

    # get user input
    user_list1_str = input(
        "enter a list of integers separated with comas e.g.'1,2,3': "
    )
    user_list2_str = input(
        "enter a list of integers separated with comas e.g.'4,5,6': "
    )

    # split the user input into lists
    user_list1 = user_list1_str.split(",")
    user_list2 = user_list2_str.split(",")

    # checks if the user inputted the numbers properly
    try:
        for index in range(0, len(user_list1)):
            user_list1[index] = int(user_list1[index])
        for index in range(0, len(user_list2)):
            user_list2[index] = int(user_list2[index])

        # asks user for direction of sorting
        print("Do you want to sort least to greatest or greatest to least? ")
        greatest_or_least = input("'<' or '>' : ")

        # check which way the user wants to sort
        if greatest_or_least == "<":
            sorted_list = merge_and_sort_least_to_greatest(user_list1, user_list2)
            print(sorted_list)
            number_line(sorted_list, 100)

        elif greatest_or_least == ">":
            sorted_list = merge_and_sort_greatest_to_least(user_list1, user_list2)
            print(sorted_list)

        # if the user did not enter a valid sorting direction
        else:
            print("Please enter '<' or '>'")

    except:
        print("please enter integers in proper format")


if __name__ == "__main__":
    main()
