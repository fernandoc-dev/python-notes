logic_operators = """
The are three logic operators: and , or, not.
Those permit excecuting sentences accordind to the boolean values True or False,
but... What is taken as True or False in Python?

Some examples:
-> The keyword True is True, :)
-> A valid comparision like 5 > 1 is True,
-> A variable that has a valid value (not Null, not Empty) is True.

On another hand:
-> The key word False is False, :)
-> An invalid comparision like 5 < 1 is False,
-> A variable which value is Null or Empty

Example 1 using logic operators:
if(a>b):
    print("a is greater than b")

Example 2 using logic operators:
a=5
if(a):
    print("a has a valid value")

Now that we know what is True and what is False... Let's operate:

And:
True and True = True
True and False = False

Or:
True or True = True
True or False = True

Not: This is the negation, then: True becomes False and False becomes True

Example using not:
if(not(1 > 2)):
    print("1 is lower than 2")
"""
print(logic_operators)


input("Press a key if you liked the explanation :)")

if(not(1 > 2)):
    print("1 is lower than 2")
