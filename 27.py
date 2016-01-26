def reverse_string_in_place(inputs, low, high):
    start = low
    end = high

    while(start < end):
        inputs[start], inputs[end] = inputs[end], inputs[start]
        start += 1
        end -= 1

    return inputs

def reverse_words_in_place(inputs):
    inputs = list(inputs)
    reversed_input = reverse_string_in_place(inputs, 0, len(inputs)-1)
    start = 0
    for i in range(0, len(inputs)+1):
        if i == len(inputs) or reversed_input[i] == ' ':
            reverse_string_in_place(reversed_input, start, i-1)
            start = i + 1


    return "".join(reversed_input)

if __name__ == "__main__":

    print(reverse_words_in_place("inputs helo"))
