try:
  n = int(input("Enter a numerator : "))
  d = int(input("Enter a denominator : "))
  r = n / d
  print("Result is : ",r)
except ZeroDivisionError:
  print("error : cannot divided by zero")
except ValueError:
  print("Error : please enter a valid integers")
