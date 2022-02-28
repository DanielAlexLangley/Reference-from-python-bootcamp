

text1 = '''
A method always needs to have a self parameter as the first parameter.
This is unlike a function. Why?
This means when this method is called, it knows the object that called it.

Self is a way to refer to the object that will be created from this class inside the class blueprint.

This is why you'll never see self when you're using objects...
but you'll see it a lot when writing code inside your class.
'''


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  # this function is for when a user decides to follow another user
        user.followers += 1  # the user who we are following, their follower count goes up by 1
        self.following += 1  # our own following count goes up by 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
