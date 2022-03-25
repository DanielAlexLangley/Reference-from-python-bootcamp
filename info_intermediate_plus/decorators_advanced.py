
# ********Day 55 Start**********
# Advanced Python Decorator Functions
# What if we want to add a condition before we call the function from within a decorator?
# What if we needed to call a function with some sort of inputs,
# how would we get inputs, if function was inside decorator?


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)
