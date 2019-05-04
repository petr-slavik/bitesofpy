numbers = list(range(-10, 11))

def filter_positive_even_numbers(numbers):
   """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
   return [x for x in numbers if x > 0 and not x % 2]