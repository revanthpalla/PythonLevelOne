import binary
import math

t = int(input())

while t:
    n = int(input())
    val = [int(i) for i in input().split()][0:n]
    n1 = max(val)
    bits = n
    n2 = int(math.pow(2,bits))
    binaries = []
    for i in range(n2):
        b_val = binary.dtob(i)
        y = ''
        if len(b_val)<bits:
            x = bits-len(b_val)
            for i in range(x):
                y += '0'
        b_val = y + b_val
        binaries.append(b_val)
    powerset = []
    for i in range(len(binaries)):
        bin_val = binaries[i]
        x = []
        for j in range(bits):
            if bin_val[j]=='1':
                x.append(val[j])
        powerset.append(x)
    print(powerset)
    t -= 1