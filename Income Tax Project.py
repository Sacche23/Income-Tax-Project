#taxpayers are charged a flat rate of 20%
#standard $10,000 deduction
#Each dependent allows a $3,000 deduction

print("Hello. This is an income tax calculator. Please enter the following information:")

ST_DEDUCTION = 10000

DEP_DEDUCTION = 3000

FLAT_RATE = 0.2

gross = float(input("\nEnter the gross income: "))

dep = int(input("Enter the number of dependents: "))

tax = float((gross - ST_DEDUCTION - (DEP_DEDUCTION * dep)) * FLAT_RATE)

print(f"The income tax is ${tax:.2f}\n")