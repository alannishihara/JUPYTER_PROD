# AN_TRY_EXCEPT.py

try:
    x = input("\nEnter a number to be used as the numerator: ")
    x = float(x)
    y = input("Enter a number to be used as the denominator: ")
    y = float(y)
    result = round((x / y), 8)
    print("Result of calculation: ", result)
except ZeroDivisionError:
    print("\nError: Division by zero error!")
except ValueError:
    print("\nError: Invalid value entered!")
else:
    print("\nNo errors or exceptions occurred")
finally:
    print("\n*** Python script run completed ***\n")