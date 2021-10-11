num = int(input("Please enter a number: "))

if num > 5:
    array = [i for i in range(1,num) if not i%3 or not i%5]
    print(array)
    print("Sum: " + str(sum(array)))
else:
    print("Input must be greater than 5!")