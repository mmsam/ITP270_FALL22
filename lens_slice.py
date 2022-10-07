#!/bin/python3

#Task-1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Task-2
prices = [2, 6, 1, 3, 2, 7, 2]

#Task-3
num_two_dollar_slices = prices.count(2)
print("There are " + str(num_two_dollar_slices) + " kinds of pizza that cost $2")

#Task-4 
num_pizzas = len(toppings)

#Task-5
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Task-6	
pizza_and_prices = [[prices[0], toppings[0]], [prices[1], toppings[1]], [prices[2], toppings[2]], [prices[3], toppings[3]], [prices[4], toppings[4]], [prices[5], toppings[5]], [prices[6], toppings[6]]]

#Task-7
print(pizza_and_prices)

#Task-8
pizza_and_prices.sort()
#print(pizza_and_prices)

#Task-9
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

#Task-10
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

#Task-11
pizza_and_prices.pop()

#Task-12
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices)

#Task-13
three_cheapest = pizza_and_prices[0:3]

#Task-14
print(three_cheapest)

