import random

def get_numbers_ticket(min, max, quantity):
  if min < 1 or max > 1000:
    return []
  random_values = set()
  for i in range(quantity):
    random_values.add(random.randrange(min, max))
  return sorted(random_values)

print(get_numbers_ticket(2,900,6))
print(get_numbers_ticket(0,900,6))
