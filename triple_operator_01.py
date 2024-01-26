import random

numbers = []
for i in range(100):
    numbers.append(random.randint(0,100))
print(numbers)

result = None
if 4 in numbers:
    result ='Есть'
else:
    result = "НЕТ"
print("Результат выражения:\n", result)