while True:
    try:
        sum = input('enter number or press "S" to stop: ')
        print()

        if sum.upper() == "S":
            print()
            print("program exited")
            break
        elif int(sum) > 5:
            result = 0
            for i in range(1,int(sum)):
                if i % 3 == 0 or i % 5 == 0:
                    result = result + i
                    print(str(result))
            print("sum: " + str(result))
            print()
        elif int(sum) != 6:
            print()
            print("Number must be greater than 5")
            print()
        else:
            raise Exception()

    except Exception as e:
        print()
        print("Only number will be accepted")
        print()