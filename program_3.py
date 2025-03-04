# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################    
total_rainfall = 0
months_count = 0

years = int(input("Enter the number of years: "))

for year in range(1, years + 1):
    print(f"Year {year}")
    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))

total_rainfall += rainfall
months_count += 1

average_rainfall = total_rainfall / months_count if months_count > 0 else 0

print("\nRainfall Statistics:")
print(f"Total months: {months_count}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
