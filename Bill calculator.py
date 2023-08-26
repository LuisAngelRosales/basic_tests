'''Second project of Udemy python academy'''
print("Welcome to the bill calculator")
bill_amount = float(input("What was the total amount of the bill?: $"))
tip_percentage = float(input("What percentage do you want to tip (10, 12, 15)?: "))
bill_split = float(input("How many people to split the bill?: "))
final_bill = (bill_amount+(bill_amount*tip_percentage/100))/bill_split
final_bill_format="{:.2f}".format(final_bill)
print(f"Each person should pay ${final_bill_format}")

