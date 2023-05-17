#Program to find the min and max in the array

numbers = [1,3,5,11,17,28,37,0,-8,-12]
min = max = numbers[0]

for num in numbers:
    if num < min:
        min = num
    if num > max:
        max = num

print("Maximium number: {}".format(min))
print(" Minimum number: {}".format(max))