binary_numbers = ["100100010110101101",
                  "00010101011110101",
                  "0000000000000000",
                  "100000010110101101",
                  "100000010110101101",
                  "10000100010110101101",
                  "11001100010110101101",
                  "11001101010110101101",
                  "11000100010110101101"]


# creates a list with indexes of all 1's (counting from right to left side)
def one_pos(input_string):
    one_indexes = []
    for idx, digit in enumerate(input_string):
        if digit == "1":
            one_indexes.append(len(input_string) - idx)
    return one_indexes


by_one_pos = [one_pos(x) for x in binary_numbers]

# prints the binary with highest 1 indexes and lowest 1 indexes
print("biggest:", binary_numbers[by_one_pos.index(sorted(by_one_pos)[-1])],
      "smallest:", binary_numbers[by_one_pos.index(sorted(by_one_pos)[0])])
