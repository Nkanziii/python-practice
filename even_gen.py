def even_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_generator(10):
    print(num)