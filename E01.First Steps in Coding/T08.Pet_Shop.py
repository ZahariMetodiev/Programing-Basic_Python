dog_food_price = 2.5
cat_food_price = 4

dog_food_count = int(input())
cat_food_count = int(input())

total_price = dog_food_price * dog_food_count + cat_food_price * cat_food_count

print(f"{total_price:.1f} lv.")
