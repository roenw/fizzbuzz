i = 0
n = 100

for i in range(n):
    if not i % 3:
        if not i % 5:
            print "FizzBuzz"
            continue
        else:
            print "Fizz"
    elif not i % 5:
        print "Buzz"
    else:
        print i
