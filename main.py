import os
import csv

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = None  # Track changes
max_increase = float('-inf')  
min_decrease = float('inf')  
max_increase_date = None
min_decrease_date = None
previous_profit_loss = 0
changes = []
dates = []


# Define the relative directory path
relative_input_dir = '..\python-challenge\PyBank\Resources'

# Join the current directory with the relative directory
budget_csv = os.path.join(relative_input_dir,'budget_data.csv')

# Open the CSV file in read mode
with open(budget_csv, 'r') as csvfile:
    
# Create a CSV reader object
    csv_reader = csv.reader(csvfile)

# Skip the header row (if present)
    next(csv_reader)

# Process each row after skipping the header
    for row in csv_reader:
        current_profit_loss = float(row[1])
        
        # Calculate total months and profit/loss by counting each line item to get total months
        # and getting the sum of profit/loss in row[1] index
        total_months += 1
        total_profit_loss += current_profit_loss
        
        # Calculate changes in profits/losses   
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
            dates.append(row[0])
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_increase_date = dates[changes.index(max_increase)]
min_decrease = min(changes)
min_decrease_date = dates[changes.index(min_decrease)]

# Print results
print(f"Financial Analysis")
print(f"---------------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss:,.2f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:,.2f})")
print(f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease:,.2f})")

# Set variables for output file
# Define the relative directory path
relative_output_dir = '..\python-challenge\PyBank\Analysis'

# Join the current directory with the relative directory
analysis_output = os.path.join(relative_output_dir, "PyBank Financial Analysis")

# Write the results in the PyBannk Financial Analysis.txt file
with open(analysis_output, "w") as output_csv_file:
    output_csv_file.write("Financial Analysis\n")
    output_csv_file.write("---------------------------------------------------------------\n")
    output_csv_file.write(f"Total Months: {total_months}\n")
    output_csv_file.write(f"Total: ${int(total_profit_loss)}\n")
    output_csv_file.write(f"Average Change: ${round(average_change,2)}\n")
    output_csv_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    output_csv_file.write(f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease})\n")