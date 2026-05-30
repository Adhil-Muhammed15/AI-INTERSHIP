try:
    num = int(input("Enter a number: "))

    assert num != 0, "Number cannot be zero"

    result = 10 / num

    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except AssertionError as e:
    print(e)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Execution completed.")