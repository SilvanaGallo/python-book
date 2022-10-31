number_list = []

for i in range(0,1000000):
    number_list.append(i+1)

print(f"The list starts in {min(number_list)} and finishes in {max(number_list)}")

print(f"The sum of values is: {sum(number_list)}")