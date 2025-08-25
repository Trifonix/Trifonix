## Calculate average

# Write a function which calculates the average of the numbers in a given array.

def find_average(numbers):
    ave = 0
    if len(numbers) != 0:
        for num in numbers:
            ave += num
        ave = ave / len(numbers)
    return ave
