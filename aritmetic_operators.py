print()
a = int(input("Insert an integer number, a = "))
b = int(input("Insert other integer number, b = "))
print()

# Addition
addition = a + b
print(f"The addition a + b = {addition} \n")

# Subtraction
subtraction = a - b
print(f"The subtraction a - b = {subtraction} \n")

# Multiplication
multiplication = a * b
print(f"The multiplication a * b = {multiplication} \n")

# Division
division = a / b
print(f"The division a / b = {division} \n")

# Modulus
modulus = a % b
print(f"The modulus a % b = {modulus} \n")

# Floor division
floor_division = a // b
print(f"The floor division a // b = {floor_division} \n")

# Exponentiation
exponentiation = a ** b
print(f"The exponentiation a ** b = {exponentiation} \n")


order_of_precedence = """
Order of precedence of Arithmetic operators in Python:
() ->           Parentheses
** ->           Exponent
%, *, /, // ->  Modulos, Multiplication, Division and Floor division
+, - ->         Addition and Subtraction
"""

print(order_of_precedence)
