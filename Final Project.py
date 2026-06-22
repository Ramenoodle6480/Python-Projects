#######################################################################
# Program Filename: Final Project
# Author: Roman Anderson
# Date: 5/29/26
# Description: Takes an amount of money in dollars and outputs the number of bills and coins required to make that amount and a bar graph of the realtive usages of each bill
# Input: Amount of money in dollars
# Output: A list of how many of each bill and coin is required and a bar graph comparing their usage rates
#######################################################################

#import libraries
import matplotlib.pyplot as plt

#set error code
error = "Invalid input, must be a number greater than 0"

#start stracking currency
currency_counts = {
    "100s": {"value" : 10000, "count" : 0}, 
    "50s": {"value" : 5000, "count" : 0}, 
    "20s": {"value" : 2000, "count" : 0}, 
    "10s": {"value" : 1000, "count" : 0}, 
    "5s": {"value" : 500, "count" : 0}, 
    "1s": {"value" : 100, "count" : 0}, 
    "Quarters": {"value" : 25, "count" : 0}, 
    "Dimes": {"value" : 10, "count" : 0}, 
    "Nickels": {"value" : 5, "count" : 0}, 
    "Pennies": {"value" : 1, "count" : 0}
}

#######################################################################
# Function: update_counts
# Description: updates the number of the specified currency in the dictionary and returns the remainder
# Parameters: a specified denomination and an amount
# Return values: updated dictionary and amount left
# Pre-Conditions: a calculated count of required currency
# Post-Conditions: none
#######################################################################
def update_counts(input_amount, key): 
        #sets the value of the current currency based off the dictionary
        value = currency_counts[key]["value"]
        #sets the respective currency count
        currency_counts[key]["count"] = input_amount // value
        #calculates and returns the amount left
        amount_left = input_amount - value * currency_counts[key]["count"]
        return amount_left

#ask user for input
while True:
    try:
        user_input = round(100*float(input("Total value (dollars.cents): ").replace(",","")))
        if user_input > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)

#loop through function for each item in dictionary
for name in currency_counts:
    user_input = update_counts(user_input, name)
    print(currency_counts[name]["count"], name)

#generate plot
#defines the x and y values from dictionary
labels = list(currency_counts.keys())
values = [currency_counts[key]["count"] for key in labels]
#defines the bars
plt.bar(labels, values, color='skyblue')
#labels the axis
plt.xlabel('Currency Denomination')
plt.ylabel('Total Count Used')
#sets the title
plt.title('Usage Frequency of Bills and Coins')
#rotates the labels so they dont overlap
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
#saves and displays the finished plot
plt.savefig('currency_usage.png')
plt.show()