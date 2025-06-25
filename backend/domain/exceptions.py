class EmptyFields(Exception):
  def __init__(self, message="Fields are empty"):
    self.message=message

class InvalidUsername(Exception):
  def __init__(self, message="Invalid characters in the username"):
    self.message=message

class InvalidPassword(Exception):
  def __init__(self, message="Invalid characters in the password"):
    self.message=message

class UnavailableUsername(Exception):
  def __init__(self, message="This username is not available"):
    self.message=message

class WrongLogin(Exception):
  def __init__(self, message="Invalid username or password"):
    self.message=message

class InvalidToken(Exception):
  def __init__(self, message="Invalid Token"):
    self.message=message
