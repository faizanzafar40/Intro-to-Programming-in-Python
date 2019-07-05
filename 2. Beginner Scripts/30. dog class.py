class Dog():
    def __init__(self, name, color="white"):
        self.name = name
        self.color = color

    def sit(self):
        print(self.name, "sits.")

    def jump(self, num):
        print(self.name, "jumps", num, "times")


dog1 = Dog("super dog")
dog2 = Dog("lazy dog")
dog3 = Dog("python dog")

dog3.trained = True

if(hasattr(dog3, "trained")):
    print(dog3, "is trained")
else:
    print(dog3, "is not trained")


if(hasattr(dog1, "trained")):
    print(dog1, "is trained")
else:
    print(dog1, "is not trained")
