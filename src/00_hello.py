# # Print "Hello, world!" to your terminal
# print("Hello, world!")

# # declaring a variable
# name = "Elvis"

# print("Hello " + name)

# # f-strings
# # `Hello {name}`
# print(f'Hello, {name}')

# # create a list with some numbers (sometimes called collections)
# p = [10, 60, 20, 5]

# # add an element to p
# print(p)
# p.append(77)
# print(p)

# # print all values in each list
# for number in p:
#     print(number)

# # Tuple mode
# for (index, element) in enumerate(p):
#     print(f'Element at {index} is {element}')

# using list comprehensions...
# create a new list containing the squares of all values in `numbers`
numbers = [1, 4, 9, 16, 25]

squares = [num*num for num in numbers]
print(squares)

# create a new list containing only the even values of `numbers`
# list comprehension
evens = [num for num in numbers if num % 2 == 0]

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)

print(evens)

# create a new list containing only the names that start with `s`
# so that they are properly capitalized (regardless of how the name originally appears)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

# create an empty dictionary
new_dict = {}

# create a dictionary with at least two key : value pairs
food = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}

# access and print an element in the dictionary
chosen_food = 'apple'
print(food[chosen_food])

# iterate through dictionary
# order is not guaranteed
# for key in food:
#     print(f'{key} {food[key]}')
for key, value in food.items():
    print(f'{key} {value}')


# Tuples

tup = 1, 2, 3, 4,

for item in tup:
    print(item)

# impossible
# tup[2] = 'new_thing'

# Set
fruit = {'apple', 'banana', 'cucumber'}
print(len(fruit))

for item in fruit:
    print(item)

print('cucumber' in fruit)

if 'cucumber' in fruit:
    print('Pretty sure its a vegetable')

if 'carrot' not in fruit:
    print('the world is predictable')
