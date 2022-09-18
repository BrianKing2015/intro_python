def main(age):
    """
    This function accepts a single variable, age it needs to be an int but input() produces a string
     so we need change it to an integer to work with it.
     Once we have the int then we perform some checks on it and for each age bracket we print some logic
    """
    if age < 13:
        print("Admission costs $2")
    elif 13 <= age < 18:
        print("Admission costs $3")
    else:
        print("Admission costs $8")


if __name__ == "__main__":
    print("Enter your age:")
    input_value = input()
    try:
        main(age=int(input_value))
    except ValueError:
        print("Try entering a number next time!")

