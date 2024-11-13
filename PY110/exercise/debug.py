data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for item in data:
    unique_data.append(item) if item not in unique_data else None

print(unique_data == [4, 2, 1, 3])