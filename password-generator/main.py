from random import randint

class PasswordGenerator:

  def generate_password(self, length: int) -> str:
    # TODO: Logic to check that at least one of each allowed sets was used in the password (before PW generation, otherwise it would depend on race condition by waiting to get the right PW).
    # Example: special_char chosen, now choose from the other 3 sets, then once next is chosen, last 2 sets, then the final set will be used and then validation is complete.
    # available_types = [special_char, digits, lowercase_letters, uppercase_letters]
    required_types = []
    remaining_count = 4

    for i in range(4):
      # required_types.append()
      remaining_count -= 1

    # print(required_types)
    # And with each type selected, it will remove from the array? And then moved to the below character array?
    # It is like a scale where its starts on 4 on one side (available types) and 0 on the other (selected types) then it gradually moves from one side to the other and when it does, validation = True/Complete.
    # Maybe a better way is that once the range is filled, then it validation_complete = True

    # For the password, creating an array that will append each selected character 'length' amount of times.
    pw_array = []

    # Loop that will append a randomly selected character per iteration.
    for i in range(length):
      pw_array.append(self.generate_char())

    # Concatenate items in the array to generate the final password string.
    password = ""

    for i in range(len(pw_array)):
      password += pw_array[i]

    if length < 4:
      raise ValueError("The password cannot meet complexity rules and must be longer than 4 characters.")
    elif length > 128:
      raise ValueError("The password exceeds recommended secure length, must be under 128 characters.")

    return "Your generated password is: " + password

  def generate_char(self) -> str:
    # Array to define specific special characters to use.
    special_chars = ['!', '@' '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    special_char = special_chars[randint(0, len(special_chars) - 1)]
    digits = str(randint(0, 9))
    lowercase_letters = chr(randint(65, 90))
    uppercase_letters = chr(randint(97, 122))

    # Detection is needed as the character is created, if it can be detected, then it can be passed to the above method to check against if the type was used
    character = [special_char, digits, lowercase_letters, uppercase_letters]
    type_num = randint(0, len(character) - 1)
    pw_char = character[type_num]
    # if chosen pw_char's index is 1, special_char was used, if 2 then digits, and so on
    # It can return the pw_char as well as what the type was so it can be checked against above

    return pw_char


pg = PasswordGenerator()

# print(pg.generate_password(10))   # Returns something like "A1!hfjK3@z".
# print(pg.generate_password(16))   # Minimum length for a strong password.
print(pg.generate_password(4))    # Check that at least 1 of each set is being used.
# print(pg.generate_password(3))  # Raises ValueError.
