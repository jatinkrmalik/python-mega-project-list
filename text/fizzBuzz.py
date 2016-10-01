# Fizz Buzz
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

print("\n\t\tFizzBuzz\n")
for i in range(1,101):

    if i%3==0 and i%5==0:
        print("FizzBuzz",end="\t")

    elif i%3==0:
        print("Fizz", end="\t")

    elif i%5==0:
        print("Buzz", end="\t")

    else:
        print(i, end="\t")

