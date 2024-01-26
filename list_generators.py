import random

result = []
result01 = {random.randint(1,100) for i in range(100)}
print(result01)

result012 = {i:i**2 for i in range(1,10)}
print(result012)
