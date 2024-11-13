def leftover_block(blocks):
    sum = 0
    layer = 1
    while sum <= blocks:
        sum += layer ** 2
        layer += 1
        print(sum, layer)
    return blocks - sum + (layer - 1) ** 2


print(leftover_block(65))

