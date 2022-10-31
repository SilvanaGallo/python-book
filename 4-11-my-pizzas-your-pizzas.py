pizzas = ['Barbecue', 'Ham and cheese', 'Carbonara', '4 Cheeses']

friend_pizzas = pizzas[:] #makes a copy

pizzas.append('Hawaian')
friend_pizzas.append('Neapolitan')

print("My favorite pizzas are: ")
for p in pizzas:
    print(f"{p}")


print("My friend's favorite pizzas are: ")
for p in friend_pizzas:
    print(f"{p}")

