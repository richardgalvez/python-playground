from random import randint

class PasswordGenerator:

  def generate_password(self, length: int) -> str:
    password = ""

    # Allowed sets to use for character generation.
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    special_char = special_chars[randint(0, len(special_chars))]
    digits = str(randint(0, 9))
    lowercase_letters = chr(randint(65, 90))
    uppercase_letters = chr(randint(97, 122))

    # TODO: Mechanism to select from each of the 4 allowed sets.
    # An array is created with each of the 4 types of characters, each are inserted in random locations each time, to be selected
    # Create array
    character = [special_char, digits, lowercase_letters, uppercase_letters]
    pw_char = character[randint(0, len(character))]
    print(pw_char)
    # Append each type of character to the array
    # pass_char = randint(len(array))

    # TODO: Logic to check that at least one of each allowed set was used in the password.

    # TODO: Then randomize characters.
    # For the password, creating an array that will append each selected character 'length' amount of times.
    password = []
    for i in range(length):
      password.append(pw_char)
    # Needs a for i in range(length) loop that will append the randomly selected character per iteration.

    # Error-handling for password length constraints.
    if length < 4:
      raise ValueError("The password cannot meet complexity rules and must be longer than 4 characters.")
    elif length > 128:
      raise ValueError("The password exceeds recommended secure length, must be under 128 characters.")


    return "Your generated password is: " + str(password)


pg = PasswordGenerator()

print(pg.generate_password(10))  # returns something like "A1!hfjK3@z"
# print(pg.generate_password(3))   # raises ValueError
