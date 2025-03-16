#Shopping Cart
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (q to Quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price of a food {food}: $"))
        foods.append(food)
        prices.append(price)

print('-----Your Cart-----')
for food in foods:
    print(food)

for price in prices:
    total += price

print(f'Your Total is: ${total}')