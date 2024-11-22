my_list = [2,3,4,5,6,7,8,9,10,11]


def print_list():
    print(my_list)

def print_sum():
    total = sum(my_list)
    print(total)

def largest():
    largest = max(my_list)
    print(largest)
    
def reverse():
    reverse = my_list[::-1]
    print(reverse)

def smallest():
    smallest = min(my_list)
    print(smallest)
    


print_list()
print_sum()
largest()
reverse()
smallest()
