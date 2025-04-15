from random import randint

class PasswordGenerator:

  def generate_password(self, length: int) -> str:
    # Array to define specific special characters to use.
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

    # For the password, creating an array that will append each selected character 'length' amount of times.
    pw_array = []

    # Loop that will append a randomly selected character per iteration.
    for i in range(length):
      special_char = special_chars[randint(0, len(special_chars) - 1)]
      digits = str(randint(0, 9))
      lowercase_letters = chr(randint(65, 90))
      uppercase_letters = chr(randint(97, 122))

      # TODO: Logic to check that at least one of each allowed sets was used in the password (before PW generation, otherwise it would depend on race condition by waiting to get the right PW).
      # Example: special_char chosen, now choose from the other 3 sets, then once next is chosen, last 2 sets, then the final set will be used and then validation is complete.
      # required_types = []
      # And with each type selected, it will remove from the array? And then moved to the below character array?
      # It is like a scale where its starts on 4 on one side (available types) and 0 on the other (selected types) then it gradually moves from one side to the other and when it does, validation = True/Complete.
      character = [special_char, digits, lowercase_letters, uppercase_letters]
      pw_char = character[randint(0, len(character) - 1)]
      pw_array.append(pw_char)

    # Concatenate items in the array to generate the final password string.
    password = ""

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
# print(pg.generate_password(3))  # Raises ValueError.
