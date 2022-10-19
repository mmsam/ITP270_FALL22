#!/bin/python3

#sample lists
hairstyles = ["cut1", "cut2", "cut3", "cut4", "cut5"]
prices = [20, 50, 20, 25, 36]
last_week = [10, 4, 10, 8, 3]

#Task 1
total_price = 0

#Task 2
for price in prices:
	total_price += price
#print(total_price)

#Task 3
length = len(prices)
average_price = total_price / length

#Task 4
print("Average Haircut Price: ", average_price)

#Task 5
new_prices = []

for price in prices:
	new_prices.append(price - 5)

#Task 6
print(new_prices)

#Task 7
total_revenue = 0

#Task 8
for i in range(len(hairstyles)):
	
#Task 9
for n in [prices[i] * last_week[i] for i in range(len(hairstyles))]:
	total_revenue += n

#Task 10
print("Total Revenue: ", total_revenue)

#Task 11
average_daily_revenue = total_revenue / 7
print(f"{average_daily_revenue:.2f}")

#Task 12
cuts_under_30 = [new_prices[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]

#Task 13
print(cuts_under_30)


