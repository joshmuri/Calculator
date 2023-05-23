# Ask the user to enter the charge for the food
food_cost = float(input("Enter the cost for the food: $"))
                  
# Calculate tip amount (18% of the food charge)
tip = 0.18 * food_cost

# Calculate the sales tax amount (7% of the food charge)
sales_tax = 0.07 * food_cost

grand_total = food_cost + tip + sales_tax

# Output the calculated amounts
print("Tip = $%.2f" % tip)
print("Sales tax = $%.2f" % sales_tax)
print("Grand total = $%.2f" % grand_total)