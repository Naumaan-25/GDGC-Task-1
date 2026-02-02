try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Program continues...")