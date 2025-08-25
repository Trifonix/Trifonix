## How good are you really?

# There was a test in your class and you passed it. Congratulations! But you're an ambitious person. You want to know if you're better than the average student in your class. You receive an array with your peers' test scores. Now calculate the average and compare your score! Return true if you're better, else false!

def better_than_average(class_points, your_points):
    average = 0
    for points in class_points:
        average += points
    average = average / len(class_points)
    return your_points > average
