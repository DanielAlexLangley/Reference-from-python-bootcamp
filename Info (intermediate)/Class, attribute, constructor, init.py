
text1 = '''
How to create a class:
class ClassName:
    code
'''


class User1:
    pass


user_1 = User1()
# create an attribute for your class
user_1.id = "001"
print(user_1.id)

text2 = '''
How to set attributes when you create object from the class?

Constructor:
AKA
Initializing (an object)
AKA
Initialize

Part of the blueprint that allows us to specify what should happen when our object is being constructed.

When object is initialized, we can set variables or counters to their starting values.
In python, we create the constructor by using a special function:
init function
This is normally used to initialize attributes.

The init will be called every time you create a new object from this class.
'''


class User2:
    def __init__(self):
        # inside here is where we initialize or create starting values for our attributes.
        pass


class Car:
    # You can add as many parameters as you wish (like "seats" below).
    # Those parameters will be passed in when an object is constructed from this class.
    def __init__(self, seats):  # "self" refers to the actual object that is being created/initialized.
        self.seats = seats  # Once you receive that data, you can use it to set the objects attributes.


my_car = Car(5)
# This "5" is what it looks like to call our constructor.
# if we do it like this, the variable my_car.seats will be equal to 5.
# in other words, it's the same as if we made the attribute like this:
# my_car.seats = 5


class User3:
    def __init__(self, user_id, username):
        self.id = user_id  # the "self.id" will be an attribute that is associated with this class
        self.username = username


user_3 = User3("001", "Angela")
print(user_3.id)
print(user_3.username)


text3 = '''
When you add parameters to constructor like above,
Whenever a new object is constructed from this class,
You must provide these two pieces of data.
'''

text4 = '''
How to have a default value for an attribute if that attribute isn't passed in?
Don't add that attribute as a parameter to be passed in.
Instead, add it as an attribute inside the class, then set its value.
See below:
'''


class User4:
    def __init__(self):
        self.follower_count = 0


user_4 = User4()
print(user_4.follower_count)
