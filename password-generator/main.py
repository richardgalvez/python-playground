from random import randint

class PasswordGenerator:

  def generate_password(self, length: int) -> str:
    password = ""

    # Allowed sets to use for character generation.
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    digits = str(randint(0, 9))
    lowercase_letters = chr(randint(65, 90))
    uppercase_letters = chr(randint(97, 122))

    # TODO: Randomly select from special_chars based on randomly chosen index #.
    # TODO: Mechanism to select from each of the 4 allowed sets.
    # TODO: Logic to check that at least one of each allowed set was used in the password.
    # TODO: Ensure order of characters are randomized.

    # Error-handling for password length constraints.
    if length < 4:
      raise ValueError("The password cannot meet complexity rules and must be longer than 4 characters.")
    elif length > 128:
      raise ValueError("The password exceeds recommended secure length, must be under 128 characters.")

    password = length * "a"

    return "Your generated password is: " + password


pg = PasswordGenerator()

print(pg.generate_password(10))  # returns something like "A1!hfjK3@z"
# print(pg.generate_password(3))   # raises ValueError