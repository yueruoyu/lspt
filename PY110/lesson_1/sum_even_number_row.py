def sum_even_number_row(row_number):
    row = []
    start = 2
    for row_index in range(1, row_number + 1):
        row.append(create_row(start, row_index))
        start = row[-1][-1] + 2
    print(row)
    return sum(row[-1])

def create_row(start_number, row_length):
    elemental_row = []
    for _ in range(row_length):
        elemental_row.append(start_number)
        start_number += 2
    return elemental_row


print(sum_even_number_row(6))