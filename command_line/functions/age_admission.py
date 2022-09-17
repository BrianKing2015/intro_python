def main(age):
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

