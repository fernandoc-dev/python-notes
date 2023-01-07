# Defining an Empty class:
# Using an Empty class is not common but we show it for learning purposes
class my_empty_class:  # Declaration of an empty class
    pass


# Instancing the empty class:
my_object = my_empty_class()  # my_object is an object that instances the class my_empty_class

print("We defined an empty class and the following print is our proof :)")
print(type(my_object))
# <class '__main__.my_empty_class'>

# Defining a regular class:


class pets_factory:
    # Builder method

    def __init__(self, breed, name=None, skill=None):
        # Atributes
        self.breed = breed
        self.name = name
        self.skill = skill
        if name is not None:
            print("This puppy was born with name included and is a beautiful {}"format(self.breed))
        else:
            print("This puppy is a beautiful {}"format(self.breed))

    # Destructor method

    def __del__(self):
        print("It is time to sleep")

    # Special methods

    def __str__(self):
        return "This method is executed when you try to print the object"

    def __len__(self):
        return "This method is executed when you try to size the object"

    # Methods

    def show_skill(self):
        print(f"this puppy can {self.skill} very well")
