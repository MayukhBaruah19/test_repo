try:
    num = int(input("Enter a number: "))
    result = 18/num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("you are good to go .")
print("End of program.")