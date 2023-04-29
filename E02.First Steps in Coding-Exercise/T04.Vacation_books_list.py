number_of_page = int(input())
page_per_hour = int(input())
days = int(input())

total_hours = int(number_of_page / page_per_hour)
hours_per_day = int(total_hours / days)

print(hours_per_day)
