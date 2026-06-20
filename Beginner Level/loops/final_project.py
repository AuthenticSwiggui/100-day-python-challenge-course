zuma = 0

for zuma in range(1, 100, 1):
    
    if zuma % 3 == 0:
        if zuma % 5 == 0:
            print("FizzBuzz")
        else: print("Fizz")
    elif zuma % 5 == 0:
        print("Buzz")
    else:
        print(zuma)
