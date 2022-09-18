def main():
    list_one = ["a", "b", "c", "d"]
    list_two = ["1", "2", "3", "4"]
    for letter in list_one:
        print(letter)
        for number in list_two:
            print(f"Letter {letter} plus {number}")


if __name__ == '__main__':
    main()
