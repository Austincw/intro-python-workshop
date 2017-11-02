# coding: utf-8

'''
Variables

Documentation:
	https://www.tutorialspoint.com/python/python_variable_types.htm

'''

# In Python, you create a variable by assigning a value to a name:
count = 5

# A variable is a placeholder for a value, an can be used anywhere the value could be used:
count = count + 5	# count is now 10

# A shortcut for adding a number to the variable is += :
count += 10	# count is now 20
print count

# You can assign any kind of new value to an existing variable, it doesn't have to be the same 
# kind of value it previously held. So we can assign a string to count:
count = "fifty"
count += " horses"	# count is now "fifty horses"
print count

# Because everything in Python is an object, a variable is really a pointer to an object.