import random

def search(data, number):
    print("The list of numbers is {}".format(data))
    print("The number to search is ", number)
    low = 0
    high = len(data) - 1
    while True:
        if low > high:
            print("NUMBER NOT FOUND")
            break
        else:
            mid = data[(low + high)//2]
            if mid == number:
                print('NUMBER IS FOUND...!!!')
                break
            elif number > mid:
                low = data.index(mid) + 1
            else:
                high = data.index(mid) - 1

data_list = sorted(random.sample(range(1, 1000),10))

number_to_search = random.randint(1,1000)

search(data = data_list, number = number_to_search)

data_list = sorted(random.sample(range(1, 1000),10))

number_to_search = random.choice(data_list)

search(data = data_list, number = number_to_search)


