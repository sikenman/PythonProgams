# Python function to generate multiplication table
# with zero and space padding
def multiplication_table(num):
    for no in range(1,11):
        result = no*num
        if num > 9:
            print(f'{num:02d} x {no:>2} = {result:>3}')
        else:
            print(f'{num:02d} x {no:>2} = {result:>3}')

# Usage
multiplication_table(7)
print()
multiplication_table(9)
print()
multiplication_table(13)
print()
