import os

os.environ["VARIABLE_NAME"] = "variable value"

SECRET_KEY = os.environ.get('SECRET_KEY', '')
