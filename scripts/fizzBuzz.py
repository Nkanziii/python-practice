def fizzbuzz(n):

    for count in range(1, n+1):
        if count % 5 == 0 and count % 3 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)

fizzbuzz(15)
