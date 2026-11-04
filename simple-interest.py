def calculate_interest(principal, rate, time):
    """Calculate simple interest."""
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return interest, total_amount


def get_positive_number(prompt):
    """Get and validate positive numerical input."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Error: Enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def display_result(principal, rate, time, interest, total):
    """Display the calculation result."""
    print("\n" + "=" * 45)
    print("       SIMPLE INTEREST CALCULATOR")
    print("=" * 45)

    print(f"Principal Amount : ₦{principal:,.2f}")
    print(f"Interest Rate    : {rate:.2f}%")
    print(f"Time Period      : {time:.2f} years")

    print("-" * 45)
    print(f"Simple Interest  : ₦{interest:,.2f}")
    print(f"Total Amount     : ₦{total:,.2f}")
    print("=" * 45)


def main():
    print("WELCOME TO THE ADVANCED INTEREST CALCULATOR")

    while True:
        print("\n1. Calculate Simple Interest")
        print("2. Exit")

        choice = input("Select an option (1 or 2): ")

        if choice == "1":
            principal = get_positive_number(
                "Enter Principal Amount (₦): "
            )

            rate = get_positive_number(
                "Enter Annual Interest Rate (%): "
            )

            time = get_positive_number(
                "Enter Time (in years): "
            )

            interest, total = calculate_interest(
                principal, rate, time
            )

            display_result(
                principal, rate, time, interest, total
            )

        elif choice == "2":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Select 1 or 2.")

if __name__ == "__main__":
    main()
