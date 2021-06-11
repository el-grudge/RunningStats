import numpy as np
import traceback as tb

inputList = []

print("Please enter your input one number per line, or 'q' to exit:")
while True:
    line = input()
    if line == 'q':
        break
    else:
        try:
            inputList.append(float(line))
        except ValueError:
            tbError = tb.format_exc()
            print("Invalid value entered, please try again.")

print("\nYour output is:")
for i in range(1, len(inputList)+1):
    print("{} {:.3f} {}".format(np.mean(inputList[:i]), np.nanstd(inputList[:i]), np.median(inputList[:i])))

print("Exit")


'''

for i in range(1, len(inputList)+1):
    print("{} {:.3f} {}".format(np.mean(inputList[:i]), np.nanstd(inputList[:i]), np.median(inputList[:i])))

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    else:
        inputList.append(line)
        
# [print(type(float(x))) for x in inputList]
# print(f'Input : {inputList}')

'''
