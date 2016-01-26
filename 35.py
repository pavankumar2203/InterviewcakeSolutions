import random

def randomize(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(items):

    last = len(items) - 1

    for i in range(0, last + 1):
        rand = randomize(i, last)
        items[i], items[rand] = items[rand], items[i]


    return items

if __name__ == "__main__":

    print(shuffle([1,2,3,4]))
    
