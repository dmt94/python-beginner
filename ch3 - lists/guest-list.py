from tokenize import maybe


my_guest_list = [
  'thich nhat hanh',
  'jay shetty',
  'taylor swift',
  'keke palmer',
  'awkwafina',
  'bea alonzo',
  'olivia rodrigo',
  'jose rizal',
  'oprah winfrey',
  'william shakespeare'
]

type_of_party = 'summer dinner gala'

print(f"These are the people coming to my {type_of_party.title()}:\n{my_guest_list}\n\n")

busy =  my_guest_list.pop()
author_addition = 'george r. r. martin'
my_guest_list.append(author_addition)
print(f"{busy.title()} can't make it to my {type_of_party.title()}. He is too busy writing a romantic comedy about a dinner party")
print(f"{author_addition.title()} will be replacing his seat at the table, though!\n\n")
print(my_guest_list)

busy_with_hero_stuff = 'jose rizal'

family_member = 'dad'
my_guest_list.remove(busy_with_hero_stuff)
print(f"\n\n{busy_with_hero_stuff.title()} is very important and needs to attend to leading people. He can't make it, understandably.")
my_guest_list.insert(-2, family_member)
print(f"My {family_member} could come, though! He will be the new {busy_with_hero_stuff.title()} at the party LOL")
print(my_guest_list)

new_person1 = 'deepak chopra'
new_person2 = 'beyonce'
new_person3 = 'radhi shetty'


my_guest_list.insert(0, new_person1)
my_guest_list.append(new_person2)
my_guest_list.insert(3, new_person3)

print(my_guest_list)

