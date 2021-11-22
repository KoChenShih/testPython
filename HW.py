
import numpy as np

while True:

    np = []

    num = int(input("The INT: "))

    count = int(0)

    for i in range(num+1):
        n = input("num :")
        np.append(n)

    print("y =", end=" ")

    for i in range(num+1):
        if((i+1) % (num+1) != 0):
            print(str(np[i]) + "x^" + str(count) + " + ")
        else:
            print(str(np[i]) + "x^" + str(count))

        count += 1
