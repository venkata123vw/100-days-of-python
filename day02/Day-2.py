bill = float(input("What was the total bill? $"))
tip = int(input("What is the percentage tip would you like to give? 10 12 or 15"))
split = int(input("How many people to split the bill?"))
bill_with_tip = bill*(1 + tip/100)
bill_per_person = bill_with_tip / split
final_bill = round(bill_per_person,2)
print(f"Each person should pay {final_bill} $")