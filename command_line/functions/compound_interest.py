def main():
    principal = 1000  # Initial amount
    rate = 0.20  # Interest rate
    num_years = 5  # Number of years
    year = 1
    while year <= num_years: # functionality done with a while loop
    # for years in range(num_years): # same functionality in a for loop
        principal = principal * (1 + rate)
        print(year, principal)
        # print(f"{year:5} {principal:0.2f}") # Optional spacing and trimming to make it easier to read
        year += 1


if __name__ == "__main__":
    main()
