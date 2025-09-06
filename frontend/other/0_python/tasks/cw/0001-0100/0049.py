## Find The Parity Outlier

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    count_even = 0
    count_odd = 0
    find_odd = False
    find_even = False
    for x in integers:
        if x%2:
            count_odd += 1
        else:
            count_even += 1
        if count_even > 1 or count_odd > 1:
            if count_even > 1:
                find_odd = True
            elif count_odd > 1:
                find_even = True
            for y in integers:
                if y%2 and find_odd:
                    return y
                elif y%2==0 and find_even:
                    return y
