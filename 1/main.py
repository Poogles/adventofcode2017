# The captcha requires you to review a sequence of digits (your puzzle
# input)and find the sum of all digits that match the next digit in
# the list. The list is circular, so the digit after the last digit is
# the first digit in the list.


def inverse_captcha(input):
    split_input = [int(x) for x in str(input)]
    # The last value we want to roll around.
    start = split_input[0]
    # Get the length so we can check the last value.
    length = len(split_input)
    total = 0
    # The input is circular
    previous = split_input[-1]
    for position, value in enumerate(split_input):
        if value == previous:
            total += value
        # Checkl to see if the we're the last value.
        if position == length:
            if value == start:
                total += value
        # Update the previous value.
        previous = value
    return total


# Now, instead of considering the next digit, it wants you to consider the
# digit halfway around the circular list. That is, if your list contains
# 10 items, only include a digit in your sum if the digit 10/2 = 5 steps
# forward matches it. Fortunately, your list has an even number of elements.


def inverse_captcha_extended(input):
    split_input = [int(x) for x in str(input)]

    length = len(split_input)
    opposite = int(length / 2)
    total = 0

    for position, value in enumerate(split_input):

        # it wants you to consider the digit halfway around the circular list.
        _i_position = position + opposite
        # This value needs to overflow...
        if _i_position >= length:
            opposite_position = _i_position - length
        else:
            opposite_position = _i_position

        opposite_value = split_input[opposite_position]

        if value == opposite_value:
            total += value

    return total
