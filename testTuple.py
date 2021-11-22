
# Tuple

# stu = ("Kelda", 21, "male")

# print(stu.count("Bro"))

# for x in stu:
#     print(x)

# if "male" in stu:
#     print("OK")

# import math

# num = int(input())

# for i in range(num):
#     r = float(input())
#     area = r * r * math.pi
#     print(area)

import math

import numpy as np

np = []

num = int(input())

for i in range(num):
    n = float(input())
    np.append(n)

for i in range(num):
    area = np[i]*np[i]*math.pi
    print(area)
