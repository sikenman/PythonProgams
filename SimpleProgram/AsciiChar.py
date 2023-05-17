
line_break = 0;

for i in range(32, 256):
    # bypassing characters that are not printable
    if i > 126 and i <= 160:
        continue;
    print(chr(i), end=' ')
    
    if line_break == 15:
        print()
        line_break = 0;
    else:
        line_break += 1;
print()