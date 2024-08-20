def my_square(n):
    value = n * n
    yield value

for square in my_square(3):
    print(square)
    
