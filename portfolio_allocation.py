def portfolio_allocation(stock_a, stock_b, stock_c):
    """
    Calculate and display the percentage allocation of three stocks in a portfolio.

    Parameters:
    stock_a, stock_b, stock_c: The dollar amounts invested in each stock
    """
    # Calculate the total portfolio value
    total = stock_a + stock_b + stock_c

    # Calculate each stock's percentage of the total portfolio
    allocation_a = stock_a / total * 100
    allocation_b = stock_b / total * 100
    allocation_c = stock_c / total * 100

    # Display the total and individual allocations
    print(f"total amount is: {total}")
    print(f"Stock A: {allocation_a:.2f}%")
    print(f"Stock B: {allocation_b:.2f}%")
    print(f"Stock C: {allocation_c:.2f}%")


# Get user input for each stock amount
stock_a = int(input("Enter the stock A: "))
stock_b = int(input("Enter the stock B: "))
stock_c = int(input("Enter the stock C: "))

# Call the function to calculate and display allocations
portfolio_allocation(stock_a, stock_b, stock_c)