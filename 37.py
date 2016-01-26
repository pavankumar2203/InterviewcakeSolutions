def rand5_recursive():
    roll = rand7()
    return roll if roll <= 5 else rand5_recursive()

#O(infinity)

def rand5():
    result = 7 # arbitrarily large
    while result > 5:
        result = rand7()
    return result
