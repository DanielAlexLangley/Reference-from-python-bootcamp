
text = '''

Classes can inherit attributes and/or methods from other classes.
Like if you had a Chef class with three methods: bake(), stir(), and measure(),
then later on you realize you also need a PastryChef who can do those same three methods
but who also needs to be able to knead() and whisk(),
you could have the PastryChef inherit the three methods from the Chef.
How to have a class inherit from another class?
If we had a class called Fish that wanted to inherit from a class called Animal:

class Fish(Animal):
    def __init__(self):
        super().__init__()
        
This will inherit both the attributes and methods.
The "super" refers to the superclass that is in parenthesis.
In this case, the superclass would be the animal while the subclass would be the fish.

(In the quiz, it said "The call to super() in the initialiser is recommended, but not strictly required.")
(I think this means as long as the superclass is in the parentheses of the subclass,
then the call to super can be omitted.)

'''


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()
nemo.swim()

# As seen above, a class can inherit a method from another class, but modify/add to it.
