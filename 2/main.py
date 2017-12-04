# The spreadsheet consists of rows of apparently-random numbers.
# To make sure the recovery process is on the right track, they
# need you to calculate the spreadsheet's checksum. For each row,
# determine the difference between the largest value and the
# smallest value; the checksum is the sum of all of these differences.


def corruption_checksum(value_input):
    rows = value_input.split('\n')

    checksums = []

    for row in rows:
        values = [int(x) for x in row.split('\t')]
        print(values)

        max_v = max(values)
        min_v = min(values)

        checksums.append(max_v - min_v)

    return sum(checksums)
