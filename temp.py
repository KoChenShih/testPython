#tempConvert.py

val = input("Please enter the temp(C or F)")
if val[-1] in ['C', 'c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("after transform: %.2fF"%f)
elif val[-1] in ['F', 'f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("after transform: %.2fF"%c)
else:
    print("error")
