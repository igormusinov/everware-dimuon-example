with open('var.txt', 'r') as file:
  mass = float(file.readline())
  if 3.0 < mass and mass < 3.2:
    print(mass)
  else:
    raise Exception('wrong value')
