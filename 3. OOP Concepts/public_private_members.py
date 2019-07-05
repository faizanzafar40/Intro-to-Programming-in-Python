class MyClass:
    def __init__(self):
        self.public = "I am public"
        self.__private = "I am private"


# Create object of type MyClass
c = MyClass()


# Access public variable via the .-notation
print(c.public)

# Show that accessing private variable via .-notation
#       leads to an error
print(c.private)


# A trick to do it anyways :)
print(c._MyClass__private)
