print("welcome to calculator")
total_bill = float(input("Enter the total bill amount?$ "))
tip = int(input("what percentage tip would like to give ? 10 12 15"))
people= int(input("how many people to split the bill  "))
bill_with_tip = tip / 100 * total_bill + total_bill
print(bill_with_tip)