number = 1
while number < 101:
    if number % 3 == 0 and number % 5 == 0:
        print("fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
