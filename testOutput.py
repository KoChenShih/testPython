import math

# num1 = input("BigINT : ")
# num2 = input("BigINT : ")

# print(num1 + num2)

val = input("Please enter the temp(C or F)")
if val[-1] == 'C' or val[-1] == 'c':
    f = 1.8 * float(val[0:-1]) + 32
    print("after transform: %.2fF" % f)
elif val[-1] == 'F' or val[-1] == 'f':
    c = (float(val[0:-1]) - 32) / 1.8
    print("after transform: %.2fC" % c)
else:
    print("error")
