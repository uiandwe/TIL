# list comprehensions

print([x for x in range(10)])


print([(lambda x: x**2)(i) for i in range(10)])


print([x for x in range(10) if x > 5])


print([x if x > 5 else 0 for x in range(10)])


print([x + 1 if x < 5 else x + 2 if x > 5 else x + 5 for x in range(10)])


print([(x, y) for x in range(3) for y in range(2)])
