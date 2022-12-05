number = int(input("Enter an integer, the input ends if its 0: "))

negative = 0
positive = 0
sum_of_numbers = 0

average = 0

while number != 0:
    if number < 0:
        negative = negative + 1
    if number > 0:
        positive += 1

    sum_of_numbers += number
    count = negative + positive
    average = sum_of_numbers / count

    number = int(input("Enter an integer, the input ends if its 0: "))

if number == 0:
    #print("No numbers are entered except 0.")
#else:
    print("The numbers of positive numbers are ", positive)
    print("The numbers of negative numbers are ", negative)
    print("The total of numbers is", float(sum_of_numbers))
    print("The average of numbers is", float(average))

