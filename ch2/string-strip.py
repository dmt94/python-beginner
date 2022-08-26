fave_language = 'python    '

#is a new value that copies the fave_language value without the space
no_space = fave_language.rstrip()

print(no_space)

first_language = '   javascript  '
first_language = first_language.strip()

#__.rstrip() - strip whitespace from right
#__.lstrip() - strip whitespace from left
#__.strip() - strip all whitespace

print(first_language)

# In the real world, these stripping functions 
# are used most often to clean up user input before it’s stored in a program
