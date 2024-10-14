def main():
    print(" This is a monthly payment loan calculator ")
    print("")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))
    
    monthly_interest_rate = apr / 1200
    # apr --24 => monthly interest rate = 0.02
    amount_of_months = years * 12
    # amount of  months 4*12 = 48
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    # monthly_payment = (principal*(1+(monthly_interest_rate*amount_of_months)))/amount_of_months
    print(" The monthly payment for this loan is: %.2f " % monthly_payment)

main()
