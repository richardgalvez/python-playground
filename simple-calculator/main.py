# Started 4/8/2025

# Simple Calculator

# Create a simple, interactive CLI calculator that can add, subtract, multiply, and divide two provided numbers.
# Implement check logic (input numbers only), keep asking until numbers are provided or user exits.

def simple_calculator():
  is_complete = False
  
  while is_complete == False:
    is_calculated = False   # Reset to False upon new loop to perform new calculation.

    x = input("\nPlease enter the first number or hit Enter to quit: ")
    if x == "":
      is_complete = True
    elif x.isnumeric() == False:
      print("\nPlease enter only numbers.")
    else:
      y = input("\nPlease enter the second number or leave empty for 0: ")
      if y == "":
        y = "0"
        print("I am here")
      # TODO: Fix detection by looping back to input option, cannot use else statement
      elif y.isnumeric() == False:
        print("\nPlease enter only numbers or leave empty for 0.")
      
      x = int(x)
      y = int(y)

      while is_calculated == False:
        operation = input("\nWhat mathematical operation do you want to use? Type in +, -, *, or /: ")
        add = x + y
        subtract = x - y
        muliply = x * y
          
        # Account for ZeroDivisionError (Cannot divide by zero)
        if y == 0:
          divide = 0
        else:
          divide = int(x / y)

        if operation == "+":
          print("\n" + str(add))
          is_calculated = True
        elif operation == "-":
          print("\n" + str(subtract))
          is_calculated = True
        elif operation == "*":
          print("\n" + str(muliply))
          is_calculated = True
        elif operation == "/":
          if y == 0:
            print("\n" + "Undefined - Cannot divide by zero.")
            is_calculated = True
          else:  
            print("\n" + str(divide))
            is_calculated = True
        else:
          print("\nInvalid operation, please enter again from below.")

simple_calculator()