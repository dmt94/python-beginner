# list : collection of items in a particular order ... an array lol

my_pokemons = ['sylveon', 'rhydon', 'swampert', 'umbreon']
print(f"My favorite pokemon in my team is {my_pokemons[0].title()}!!")


# adds to the END of the list
my_pokemons.append('primarina')

print(f"My new favorite pokemon in my team is {my_pokemons[-1].title()}!!")


# inserting elements into a list => will shift other elements' positions 
my_pokemons.insert(0, 'dragonite')
print(f"My strongest pokemon may be {my_pokemons[0].title()}, but my original favorite is {my_pokemons[1].title()}!")


# removing elements from a list, need to know index position
del my_pokemons[3] #removed swampert (new position after adding dragonite)
print(my_pokemons)



grocery_list = [
  'avocados',
  'basil',
  'pasta noodles',
  'lavander & rose kombucha',
  'lemons',
  'salmon',
  'heavy cream',
  'vanilla ice cream',
  'spinach',
  'oat milk',
]

# "oat milk", the last in the list, is removed from the original list
#  and assigned to "retrieved" variable below
retrieved = grocery_list.pop()
print(grocery_list)
print(retrieved) # "oat milk"


# popping items from any position
priority_food = grocery_list.pop(0) # first on the list
print(f"First, I made sure to buy {priority_food.upper()}")

#  when you want to delete an item from a list 
# and not use that item in any way, use the del statement; 
# if you want to use an item as you remove it, use the pop() method.



# removing item by value, say you don't know an element's index position
# removes the FIRST INSTANCE of element only, use loop if occurs more than once in list
too_much_sugar = 'vanilla ice cream'
grocery_list.remove(too_much_sugar) # removes from list
print(grocery_list)
print(f"I've decided not to buy {too_much_sugar}...it's not the best option for me right now.")