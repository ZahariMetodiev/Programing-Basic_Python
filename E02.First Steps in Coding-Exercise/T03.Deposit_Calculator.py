deposit = float(input())
period = int(input())
percent = float(input())

interest = deposit * percent / 100
interest_for_month = interest / 12
total_sum = deposit + period * interest_for_month
print(f"{total_sum:.2f}")

