# Defining an Empty class:
# Using an Empty class is not common but we show it for learning purposes
class my_empty_class:  # Declaration of an empty class
    pass


# Instancing the empty class:
my_object = my_empty_class()  # my_object is an object that instances the class my_empty_class

print("\nWe defined an empty class and the following print is our proof :)")
print(type(my_object))
# <class '__main__.my_empty_class'>
print()

# Defining a regular class:


class First_class:

    # Atributes
    attribute_1: str
    attribute_2: str
    attribute_3: str = "default value"

    # Constructor method
    def __init__(self, required_param, optional_param=None):

        self.attribute_1 = required_param
        self.attribute_2 = optional_param
        if self.attribute_3 != "value":
            print("This print is executed from constructor method\n")

    # Destructor method

    def __del__(self):
        print("This print is executed from destructor method and this is executed when all references to the object are deleted\n")

    # Special methods

    def __str__(self):
        return "This method is executed when you try to print the object\n"

    def __len__(self):
        return 2023  # This ill be the answer of len(my_object)"

    # Methods

    def method_1(self):
        print(f"This print is executed from method_1 which is a regular method, the required_param is: {self.attribute_1}\n")

    @classmethod
    def class_method(cls):
        print(
            f"This print is executed from class_method which has the decorator @classmethod thus it can be executed without create an instance of the class previously but it can use the attributes' default values. Eg. {cls.attribute_3}\n")

    @staticmethod
    def static_method(parameter_for_static_method):
        print(
            "This print is executed from static_method which has the decorator @staticmethod thus it can be executed without create an instance of the class previously and it can not use the class attributes but can receive its own parameters. Eg. {parameter_for_static_method}\n")


print("My First regular class:\n")

# Create an instance of First_class
my_object = First_class('required_value')

# Execute the __str__ special method
print(my_object)

# Execute the __len__ special method
print("The length of my_object is: ", len(my_object), "# This answer is set in __len__ method\n")

# Execute the regular method "method_1"
my_object.method_1()

# Execute the class method
First_class.class_method()

# Execute the static method
First_class.static_method('static value')
