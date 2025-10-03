def calculate_future_value(principal, rate, time):  # principal, rate, time are parameters
    future_value = principal * (1 + rate)**time
    return future_value
principal_amount = 1000
interest_rate = 0.05
investment_period = 10
future_value = calculate_future_value(principal_amount, interest_rate, investment_period) # principal_amount, interest_rate, investment_period are arguments
print(future_value)