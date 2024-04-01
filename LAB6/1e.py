# import re
# s = "Hello Everyone! Thank you so much for visting."
# print(re.sub("so", "very", s))
import os

# Get all environment variables
env_vars = os.environ

# Iterate and print each environment variable
for key, value in env_vars.items():
    print(f"{key}: {value}")
