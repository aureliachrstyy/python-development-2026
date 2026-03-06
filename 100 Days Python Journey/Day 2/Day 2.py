print("Welcome to the tip calculator")
# Bill 
bill = float(input("What was the total bill?$ "))
# Bill with Service Charge (10%)
bill_with_service_charge = float(bill * 10 / 100 + bill)
# Bill with PB1 (11%)
bill_with_sc_pb = float (bill * 11 / 100 + bill_with_service_charge)
# Bill tip and people
tip = int(input("How much tip do you want to give? 10 12 or 15? "))
people = int(input("How many people to split the bill? "))
# Bill with tip logic
bill_with_tip = tip / 100 * bill_with_sc_pb
# Bill per person logic
final_bill = round(bill_with_tip + bill_with_sc_pb, 2)
bill_per_person = final_bill / people
final_amount = round(bill_per_person, 2)
# Final Bill
final_bill_with_sc = print(f"Bill with service charge (10%): ${bill_with_service_charge}")
final_bill_with_pb1 = print(f"Bill with tax (11%): ${bill_with_sc_pb}")
finalized_amount = print(f"Bill: ${final_bill}")
final_amount_each = print(f"Each person should pay: ${final_amount}")