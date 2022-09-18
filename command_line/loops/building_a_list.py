def main():
    """
    This function counts up by a value, printing along the way for clarity and then appends each number to a list.
    Building a new list, which is then printed at the end. Deleting the print(starting_from) would have no effect on the
    list built.
    """
    list_to_build = []
    count_up_by_this = 3
    starting_from = 0
    for iteration in range(0, 5):
        print(starting_from)
        list_to_build.append(starting_from)
        starting_from = starting_from + count_up_by_this

    print(list_to_build)


if __name__ == '__main__':
    main()
