def convert_bits_to_index_form(bits):
    """
        Converts bits to an index form.
        eg: [1 0 0 0] => [3]
            [1 0 1 0] => [3,1]
    """

    bits.reverse()
    indexes = []
    for i, bit in enumerate(bits):
        if bit != 0:
            indexes.append(i)
    indexes.sort(reverse=True)
    return indexes


def xor(input1, input2):
    """
        Performs XOR operation on two values which are in the index form.
        eg: [3,1] + [2,0] = [3,2,1,0]   which basically means [1 0 1 0] + [0 1 0 1] = [1 1 1 1]
    """

    output = []
    for i in input1:
        if i in input2:
            input2.remove(i)
            continue
        output.append(i)
    output.extend(input2)
    return output

print("testing", xor([3,1],[3,1]))


def reduce(output):
    """
        Performs the functionality of the long division and returns the reduced form.
    """
    poly_of_reduction = [4, 1, 0]   # this represents x4 + x + 1
    while output[0] >= poly_of_reduction[0]:
        multiplier = output[0] - poly_of_reduction[0]                       # similar to dividing x6 by x4. ie, 6 - 4 = 2
        operand = [element + multiplier for element in poly_of_reduction]   # similar to multiplying polynomial_of_red by x2. In this case, adds 2 to each value in [4,1,0] => [6,3,2]  which represents x6+x3+x2
        output = xor(output, operand)                                       # performs XOR operation of the two values
    return output


def convert_to_bits(reduced_output, bit_length):
    """
        Converts the index form back to the bit form
        eg: [3] => [1 0 0 0]
            [2,0] => [0 1 0 1]

    :param reduced_output: index form
    :param bit_length: number of bits of the final output
    :return: result in bit form
    """
    output = [0 for i in range(bit_length)]
    for i in range(len(output)):
        for element in reduced_output:
            if i == element:
                output[i] = 1
    output.reverse()
    return output


def multiply(bits0, bits1):
    tmp = []
    for i in range(4):
        tmp.append([0, 0, 0, 0, 0, 0, 0])
        for j, bit in enumerate(bits0):
            if (bit != 0) and (bits1[i] != 0):
                tmp[i][j + i] = bit * bits1[i]

    output = []
    for i in range(7):
        sum = 0
        for j in range(4):
            sum += tmp[j][i]
        output.append(sum % 2)

    # ==== DIVISION ====
    output_index_form = convert_bits_to_index_form(output)  # converts to index form
    reduced_form = reduce(output_index_form)                # performs reduction

    return convert_to_bits(reduced_form, len(bits0))        # convert back to bit form


bits0 = [1, 0, 1, 0]
bits1 = [1, 0, 1, 0]

output = multiply(bits0, bits1)
print(bits0, '*', bits1, '=', output)
