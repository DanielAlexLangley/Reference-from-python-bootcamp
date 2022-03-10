
# ENVIRONMENT VARIABLES

# First reason to use environment variables:
# Can use this to hide code, so that when you upload the code publicly,
# no one else can see your API keys and things like that.

# Second reason to use environment variables:
# For convenience. If you had a program running, you might not want to stop the code in order to update a variable.
# So you can go into the environment variables and change what you need to change without touching the code itself.

# In PyCharm open a project, click "Terminal" at the bottom, then make sure you're in Windows Powershell.
# Type "dir env:"
# This shows you the environment variables.
# To add a new one, type:
# setx variable_name "variable_value"

# Do that for each variable you want to save into the environmental variables.
# After entering the variables that way, I had to reboot PyCharm for them to show up when I did "dir env:"
# Add import os
# Make a new variable for each environmental variable you want to call.

# Examples:
# api_key_twilio = os.environ.get("API_KEY_TWILIO")
# api_key_owm = os.environ.get("API_KEY_OWM")
# Use those new variables in your code wherever you want to call those variables.
