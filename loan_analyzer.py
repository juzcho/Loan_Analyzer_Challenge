# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list. - DONE
    2. Use the `sum` function to calculate the total of all loans in the list. - DONE
    3. Using the sum of all loans and the total number of loans, calculate the average loan price. - DONE
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
length_of_loan_costs = len(loan_costs)
print(f"The total number of loans: {length_of_loan_costs}.") #The total number of loans is 5.

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

total_of_loan_cost = sum(loan_costs)
print(f"\nThe sum of all loans is ${total_of_loan_cost}.") #The total of all the loan is $2750.


# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
average_loan_amount = total_of_loan_cost / length_of_loan_costs
print(f"\nThe average loan amount is ${average_loan_amount:.0f}.") #The average loan amount is $550.

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`. - DONE
    b. Print each variable. - DONE

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate. - DONE
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost? Done
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
# YOUR CODE HERE!
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"\nThe future value is ${future_value}, and the remaining months is {remaining_months} months.") #The future value is $1000, and the remaining months is 9 months.

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!
discount_rate = .20 #This is to initialize the discount rate variable.
present_value = future_value / (( 1 + (discount_rate/12)) ** remaining_months) #This is the formula to get the fair value of the loan.
fair_value = present_value

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!- Done
if present_value >= loan.get("loan_price"):
    print(f"\nThe fair value of the loan is ${present_value:.2f}. Buy it! The loan is worth more than the cost.") #If the amount of the fair value of the loan is more than the loan price, then you should buy the loan.
else: 
    print("\nDO NOT BUY!The loan is too expensive.") #If the amount of the fair value of the loan is less than the loan price, then it's expensive so do not buy the loan.

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

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

def calculate_present_value(future_value, remaining_months, annual_discount_rate): #This will define a new function called calculate_present_value with parameters.
 
    present_value = future_value / (( 1 + (annual_discount_rate /12)) ** remaining_months) #The formula for present value.
    return present_value #This will calculate the present value.

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
annual_discount_rate = 0.2
present_value_of_new_loan = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate) #This will call the new defined function, and it will use the parameters from the new_loan to calculate the present value.
print(f"\nThe present value of the new loan is: ${present_value_of_new_loan:.2f}")



"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
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
# YOUR CODE HERE! -Done
inexpensive_loans = [] #This is creating a new empty list.

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list - Done
# YOUR CODE HERE!
for loan in loans: #This for loop statement will run the every loan on the loan dictionary.
    if loan.get("loan_price") <= 500: # We created an if statement to get the loans that are less than or equal to 500.
        inexpensive_loans.append(loan) #Once we check if the loan price is less than or equal to 500, then it will add those loans to the inexpensive loans list.

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE! - Done

#This will now print the new set of list that are inexpensive loans.
print("\nThese are the inexpensive loans:")
'''Other ways to print'''
    # print(inexpensive_loan)
    # [print(loan) for loan in inexpensive_loans] # using list comprehension
    # for loan in inexpensive_loans:   # using for loop
    #     print(loan)
print(*inexpensive_loans, sep="\n") # Without using loops and using * operator in order to utilize a separator in each item in a list. In this case, the items will be separated by a newline by using \n.


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
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

print("\nWriting the data to a CSV file...")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

with open(output_path, 'w', newline = '') as csvfile: #This will open a newly created file, and then it will overwrite with whatever data we add.
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    #csvwriter.writerow(inexpensive_loans[0].keys()) '''This can be used an alternative as a header.'''
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values()) #We are using the for loop statement 
