class Cake:

    def __init__(self, val, weight):
        self.val = val
        seld.weight = weight

def maximizecake(types, bagweight):
    maxvalues = [0 for x in range(0,bagweight + 1)]

    for j in range(0, bagweight + 1):

        currentmax = 0
	    for i in range(0, len(types)):
            if i.weight == 0 and i.value != 0:
                return "Bag can be infinitely filled"

            if i.weight < j:
	        	value = i.value + maxvalues[j - i.weight]
                currentmax = max(currentmax,value)

        maxvalues[j] = currentmax

    return maxvalues[bagweight]
