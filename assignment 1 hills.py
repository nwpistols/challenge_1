# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

amount_of_loans = len(loan_costs) # Amount of loans is equal to the length of the loan_costs list.
print(f"The total amount of loans is {amount_of_loans} loans.") # Printed the total amount of loans.


# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

total_of_all_loans = sum(loan_costs) # Assigned variable total_of_all_loans to the sum of all loans in the list.
print(f"The total value of all loans is ${total_of_all_loans}.") # Printed the $ total of all loans.

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

average_loan_amount = (total_of_all_loans)/(amount_of_loans) # Created variable called average_loan_amount that equals total of all loans divided by the amount of loans.
print(f"The average loan amount is ${average_loan_amount:.0f}.") # Printed the average loan amount in $, rounded to whole number to get rid of the .0 at the end of the amount.

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

future_value = loan.get("future_value") # Created a variable for future loan value 'future_value' by pulling the variable from the dictionary.
print(f"The future value of the loan is ${future_value}.") # Printed the future value of the loan.
remaining_months = loan.get("remaining_months") # Created a variable for future remaining months 'remaining_months' by pulling the variable from the dictionary.
print(f"The amount of months remaining is {remaining_months}.") # Printed the remaining months on the loan.


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount_rate = 0.2 # Assigned a variable of 0.2 (20%) to act as the discount rate.
fair_value = future_value / (1 + discount_rate/12) ** remaining_months # Used the monthly version of the present value formula to create a variable for the fair value of the loan. 
print(f"The fair value of the loan is ${fair_value:.2f}.") # Printed the fair value of the loan rounded to 2 decimal places to notate cents. 

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

loan_price = loan.get("loan_price") # Created a variable for loan price 'loan_price' by pulling the variable 'loan_price' from the dictionary.

if fair_value >= loan_price: # First part of the conditional statement, questioning whether the fair value is greater than or equal to the loan price.
    print("The loan is worth at least the cost to buy it!") # Printed message to buy the loan
else: # Second part of the conditional that would check whether the fair value is smaller than the loan price. 
    print("The loan is too expensive and not worth the price!") # Print option for the second part of the conditional that would print that the loan is too expensive.


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000, 
}
annual_discount_rate = 0.2 # Assigned variable for an annual discount rate of 20% or 0.20.
# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate): # First line of function, defining calculate_resent_value with the requested parameters.
    present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months # Second line of function definition, describing the formula for present value. 
    return present_value # returning the value for present_value.

new_loan_value = calculate_present_value(new_loan["future_value"],new_loan["remaining_months"],annual_discount_rate) 


print(f"The present value of the loan is ${new_loan_value:.2f}.") # Printed the present value of the loan, rounding to 2 decimal places.


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list.
for item in loans: # Used a for loop to access each inner dictionary. Noting I am looking for an item in each list.
    if item.get("loan_price") <= 500: # Used the get tool to inquire whether the loan price of each loan was less than or equal to 500.
        inexpensive_loans.append(item) # Ended the if statement by telling the for loop to append the loans less than or equal to 500 into the inexpensive loans list. 

    # loan_price = item["loan_price"] # Indicated that I am looking for the loan price in each dictionary, and this collection of prices is to be called 'loan_price'.
    # if loan_price <= 500: # Created a conditional to see whether each loan price is equal to or less than $500.
        # inexpensive_loans.append(loan_price)  # Signaled for loan values equal to or below $500 to be appended to the list of inexpensive loans.

# @TODO: Print the `inexpensive_loans` list
print(f"The list of inexpensive loans is: {inexpensive_loans}.")

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"] # Header was given.

# Set the output file path
output_path = Path("inexpensive_loans.csv") # Output path was given.

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
csvpath = Path("inexpensive_loans.csv") # This line of code selects the save output path and file name.csv.
with open(csvpath, 'w', newline='') as csvfile: # Using 'with open', I open the csv file, using 'w' to signify that I'm writing into a file, and newline='' to allow the csv file to accept any special characters.
    csvwriter = csv.writer(csvfile) # Created a csv.writer in order to write data in my new CSV file. 
    csvwriter.writerow(header) # Used the writerow() tool to write our header in the first row of the document.
    for loan in inexpensive_loans: # Used a 'for loop' to access data in the dictionaries within inexpensive_loans.
        csvwriter.writerow(loan.values()) # Used the values() tool to write the dictionary values as rows of data in the CSV file.
