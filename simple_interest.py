def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.

    :param principal: The principal amount
    :param rate: The annual interest rate (in percentage)
    :param time: The time the money is invested for (in years)
    :return: The simple interest
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    
    interest = calculate_simple_interest(principal, rate, time)
    print(f"The simple interest is: {interest}")
