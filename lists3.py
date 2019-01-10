odd_numbers = [1,3,5,7,9,11,13,15,17,19 ]
for odd_number in odd_numbers:
    print(odd_number)

numbers =[3,6,9, 12,15,18,21,24,27]
for number in numbers:
    print(number)
cube = []
for value in range(1,10):
    cube.append(value**3)
    print(cube)

cube = [value**3 for values in range(1,10)]
print(cube)
countries = ["Canada", "France", "Belgium", "Ireland", "Italy"]
print("The first three items in the list are:")
print(countries[0:3])
print("Three items in the middle of the list are:")
print(countries[1:4])
print("The last three items in the list are:")
print(countries[2:])
my_pizzas = ["meat pizzas","chicken pizzas","vegtable pizzas"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("olives pizzas")
print(my_pizzas)
friend_pizzas.append("felafel pizzas")
print(friend_pizzas)
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
for my_pizza in my_pizzas:
    print(my_pizza)

for friend_pizza in friend_pizzas:
    print(friend_pizza)

buffet_foods = ("chips beef","chips chicken","chips liver","katogo")
for buffet_food in buffet_foods:
    print(buffet_food)
buffet_foods = ("chips beef","chips chicken","chips liver","katogo")
print("original buffet_foods")
for buffet_food in buffet_foods:
    print(buffet_food)
print("\nmodified buffet_foods")    
buffet_foods = ("chips beef","chips chaps","chips chicken","chips eggs")
for buffet_food in buffet_foods:
    print(buffet_food)
    