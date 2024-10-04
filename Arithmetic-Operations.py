# Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!

steak = 40.00
onions = 6.51
buns = 5.00

total = steak + onions + buns
print(f"The total cost is: ${total}.")


# Task 2: If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

savings_account = 10000.00
interest = .07
end_of_year_amount = savings_account * interest + savings_account
print(f"Total amount after a year is: ${end_of_year_amount:.2f}")