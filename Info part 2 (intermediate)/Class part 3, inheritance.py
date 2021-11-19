
text = '''

Classes can inherit attributes and methods from other classes.

Like if you had a Chef class with three methods: bake(), stir(), and measure(),
then later on you realize you also need a PastryChef who can do those same three methods
but who also needs to be able to knead() and whisk(),
you could have the PastryChef inherit the three methods from the Chef.

How to do have a class inherit from another class?
If we had a class called:

class Fish():
    def __init__(self):
        etc.
        
Then write it like:

class Fish(Animal):
    def __init__(self):
        super().__init__()
        
The "super" refers to the superclass that is in parenthesis.
In this case, the superclass would be the animal while the subclass would be the fish.
(In the quiz, it said "The call to super() in the initialiser is recommended, but not strictly required.")
(I think this means as long as the superclass is in the parentheses of the subclass,
then the call to super can be omitted.)
So it means initialize everything the superclass can do in our fish class.

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
nemo.breathe()

'''
