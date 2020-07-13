# Create a tuple named zoo that contains 10 of your favorite animals.

zoo = ('alligator', 'bee', 'cow', 'deer', 'eagle',
       'fox', 'giraffe', 'horse', 'iguana', 'jaguar')
print(zoo)

# Find one of your animals using the tuple.index(value) syntax on the tuple.
# # Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1
print(zoo.index("jaguar"))

# Determine if an animal is in your tuple by using value in tuple syntax.
# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
#     # Print that the animal was found
animal_to_find = 'bee'
found_animal = False

for animal in zoo:
    if animal == animal_to_find:
        found_animal = True
print(found_animal)

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
children = list(("Sally", "Hansel", "Gretel", "Svetlana"))
(first_child, second_child, third_child, fourth_child) = children
print(first_child)  # Output is "Sally"
print(second_child)  # Output is "Hansel"
print(third_child)  # Output is "Gretel"
print(fourth_child)  # Output is "Svetlana"
children.extend(['Daniel', 'Felipe', 'John'])
print(children)
children = tuple(children)
print(children)

# Create a variable for the animals in your zoo tuple, and print them to the console.
# Convert your tuple into a list.
# Use extend() to add three more animals to your zoo.
# Convert the list back into a tuple.
