import math
input = input().split()
n = int(input[0])
m = int(input[1])
a = int(input[2])
print(math.ceil(n / a) * math.ceil(m / a))
