numbers = [number for number in range(16, 100, 4)]
print({s for s in numbers if s ** 0.5 == int(s ** 0.5)})
