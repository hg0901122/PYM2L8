def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")

Bill = int(input("Enter the total ammount: "))
Tip = int(input("Enter how much percent you want to tip: "))

total_calc(Bill, Tip)
          