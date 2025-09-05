def binary_search(list, item):
    print(f"\n==== ==== ==== ==== {len(list)}")
    low = 0
    high = len(list)
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        #print("count===",count,': low=',low,'high=',high,'mid=',mid)
        guess = list[mid]
        
        if guess == item:
            return f"mid={mid} count={count+1}"
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return f"mid={None} count={count+1}"

my_list = [x for x in range(1,240001,1)]    
print(binary_search(my_list, 2))            # 19
print(binary_search(my_list, -1))           # 18

my_list = [x for x in range(1,129,1)]
print(binary_search(my_list, -1))           # 8

my_list = [x for x in range(1,257,1)]       
print(binary_search(my_list, -1))           # 9

my_list = [x for x in range(1,101)]       
print(binary_search(my_list, -1))           # 7
'''
my_list = [x for x in range(1,40000001)]       
print(binary_search(my_list, -1))           # 26
'''                            
my_list = [x for x in range(1,1000000000)]       
print(binary_search(my_list, -1))           # 30 ?
