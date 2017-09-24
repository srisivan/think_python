
# Working out Exercises and problems from the book Think Python

# Chapter 1
# Variables, Expressions, and Statements

# 1. Values and Types

''' 
The Values in python are :

1. String
2. Integers
3. Float


The Types in python are :

1. str for String
2. int for Integers
3. float for Decimeals

'''
 
# We can find which type a object is, by typing it in the type() command, like this::

type('Hello World!')            # Outputs 'str'
type(1234)                    	# Outputs 'int'
type(3.1456)                  	# Outputs 'float'
type('123456')                  # DOES NOT Output as 'int'. Outputs as 'str', as they are inside quotes


# 2. Variables

'''
Variables are the most important of all programming languages. It is simply like a container, that holds values inside. If it is assigned a new value, 
the old one is discarded, and replaced by the new one.

'''

# We can declare a new variable like this :

interesting_word = 'Scrumdidllyumptious'         # Assingns the value 'Scrumdidllyumptious' to the variable interesting_word.
print(interesting_word)                          # Prints 'Scrumdidllyumptious'

interesting_word = 'Babblement'                  # Assingns the value 'Babblemnt' to the variable interesting_word. The old one is discarded.
print(interesting_word)                          # DOES NOT Print 'Scrumdidllyumptious'. It prints 'Babblement'.

# Variables can also be assigned integers as values :

interesting_number = 20

# They can also be used for operations

 print(interesting_number + 23)                 # Prints 43. (20 + 23)

 # .... And can also be assigned to Decimeals :

 pi = 3.14124787

