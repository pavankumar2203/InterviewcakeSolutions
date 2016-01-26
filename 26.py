def reverse_string_in_place(input):

    input = list(input)
    start = 0
    end = len(input) - 1

    while(start < end):
        input[start], input[end] = input[end], input[start]
        start += 1
        end -= 1

    return input

if __name__ == "__main__":

    print(reverse_string_in_place("inputs"))

    
