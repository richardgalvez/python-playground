from random import randint, shuffle

class PasswordGenerator:

  def generate_password(self, length: int) -> str:
    # Array to define specific special characters to use.
    special_chars = ['!', '@' '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    special_char = special_chars[randint(0, len(special_chars) - 1)]
    digits = str(randint(0, 9))
    lowercase_letters = chr(randint(65, 90))
    uppercase_letters = chr(randint(97, 122))

    pw_array = []
    password = ""

    required_chars = [special_char, digits, lowercase_letters, uppercase_letters]

    # For first 4 chars, use one of each from the required set of characters.
    shuffle(required_chars)
    for i in range(len(required_chars)):
      password += required_chars[i]

    # Generate characters for the remaining amount of length.
    if length > 4:
      for i in range(length - 4):
        special_char = special_chars[randint(0, len(special_chars) - 1)]
        digits = str(randint(0, 9))
        lowercase_letters = chr(randint(65, 90))
        uppercase_letters = chr(randint(97, 122))
        character = [special_char, digits, lowercase_letters, uppercase_letters]
        pw_char = character[randint(0, len(character) - 1)]
        pw_array.append(pw_char)

      # Extra shuffle for good measure before concatenation to array to create final password.
      shuffle(pw_array)
      for i in range(len(pw_array)):
        password += pw_array[i]

    if length < 4:
      raise ValueError("The password cannot meet complexity rules and must be longer than 4 characters.")
    elif length > 128:
      raise ValueError("The password exceeds recommended secure length, must be under 128 characters.")

    return "Your generated password is: " + password


pg = PasswordGenerator()

print(pg.generate_password(10))   # Returns something like "A1!hfjK3@z".
print(pg.generate_password(16))   # Minimum length for a strong password.
print(pg.generate_password(4))    # Check that at least 1 of each set is being used.
print(pg.generate_password(3))  # Raises ValueError.
