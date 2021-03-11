import math

#the user is asked to pick the financial calculator they would like
#to use: an investment calculator or a home loan calculator.

print("\nChoose below whether you would like to use an investment calculator \nor a home loan calculator.\n")

calculator_ = input("Enter in what calculator you would like to use(home loan or investment): ")


#if the user chooses to use an investment calculator
#they are asked to enter a series of inputs which are than used to calculate 
#whatever it is they wish to be calculated 'simple interest or compound interest'
#the results are than displayed to the user.

if (calculator_ == 'investment') or (calculator_ == 'Investment') or (calculator_ == 'INVESTMENT'):
    money_dep = float(input("Enter the amount of money you would like to deposit: R"))
    interest_rate = float(input("Please enter the interest rate(%): "))
    years_inv = int(input("Please enter the number of years you would like to invest for: "))
    interest = input("would you like \'simple\' or \'compound\' interest on your money?: ")
    
    if (interest == 'simple') or (interest == 'Simple') or (interest == 'SIMPLE'):
        simple_interest = money_dep * (1 + (interest_rate / 100) * years_inv)
        print("Your total amount after {} years of interest would be R{}".format(years_inv,simple_interest))

    
    elif (interest == 'compound') or (interest == 'Compound') or (interest == 'COMPOUND'):
        compound_interest = round(money_dep * math.pow((1 + (interest_rate / 100)), years_inv),1)
        print ("Your total amount after {} years compound interest would be R{}.".format(years_inv,compound_interest))


#if the user inputs that they would like to use the home loan calculator
# they are asked to enter a few values that will be used to calculate their home loan repayments
#the results are than displayed to the user
elif (calculator_ == 'home loan') or (calculator_ == 'Home loan') or (calculator_ == 'HOME LOAN') or (calculator_ == 'homeloan') or (calculator_ == 'Homeloan') or (calculator_ == 'HOMELOAN'):
    value_home = float(input("Please enter in the present value of your house: R "))
    home_interest = float(input("Please enter the interest rate(%): "))
    repay = int(input("Enter the number of years you plan on taking to repay the bond: "))
    year_payment = round(((home_interest/100) * value_home) / (1 - (1 + (home_interest/100)) ** (-repay)))
    totalmonthly_payment = year_payment // 12

    print("Your total monthly instalments are R{}.".format(totalmonthly_payment))

#if the user enters an input that is not valid, they are displayed a message that tells them to reinput 
#a valid
else:
    print("Please make sure you\'ve chosen one of the given options.")


