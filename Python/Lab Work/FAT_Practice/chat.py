# Function to calculate gross pay
def calculate_gross_pay(hours, rate_per_hour):
    # Basic Pay calculation
    basic_pay = hours * rate_per_hour
    
    # DA (14%) and HRA (10%) allowances
    DA = 0.14 * basic_pay
    HRA = 0.10 * basic_pay
    
    # PF (4%) deduction
    PF = 0.04 * basic_pay
    
    # Gross Pay = Basic Pay + DA + HRA - PF
    gross_pay = basic_pay + DA + HRA - PF
    
    return gross_pay

# Main part of the program
def main():
    # Input: Hours worked and rate per hour
    hours = float(input("Enter Hours: "))
    rate_per_hour = float(input("Enter Hour Rate: "))
    
    # Calculate the gross pay
    gross_pay = calculate_gross_pay(hours, rate_per_hour)
    
    # Output: Display the gross pay
    print(f"Gross Pay: {gross_pay:.2f}")

# Call the main function to execute the program
main()
