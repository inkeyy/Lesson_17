import random

numbers = []
for i in range(100):
    numbers.append(random.randint(0,100))
print(numbers)

print("число 13 есть") if 13 in numbers else print("числа нет в списке")

p = "число 13 есть" if 13 in numbers else "числа нет в списке"
print(p)