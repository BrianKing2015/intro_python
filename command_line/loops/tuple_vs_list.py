def main():
    """
    Each time through the first loop it prints an object.
    It is the same old thing with the tuple, iterate through it and print each object
    """
    list_of_numbers = [1, 2, 3]
    tuple_of_numbers = (4, 5, 6)
    for number in list_of_numbers:
        print(number)

    for number in tuple_of_numbers:
        print(number)


if __name__ == '__main__':
    main()
