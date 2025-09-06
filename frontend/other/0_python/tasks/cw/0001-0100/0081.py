## Find the next perfect square!

# You might know some pretty large perfect squares. But what about the NEXT one? Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer. If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

from math import sqrt

def find_next_square(sq):
    curr = round(sqrt(sq))
    if (curr*curr)==sq:
        curr2 = round(curr)+1
        return curr2*curr2
    else:
        return -1
