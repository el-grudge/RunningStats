import numpy as np
import traceback as tb

inputList = []

print("Please enter your input one number per line, or 'q' to exit:")
while True:
    line = input()
    if line == 'q':
        print("Exit")
        break
    else:
        try:
            inputList.append(float(line))
            print("Your output is:")
            print("{:.3f} {:.3f} {}".format(np.mean(inputList), np.nanstd(inputList), np.median(inputList)))

        except ValueError:
            tbError = tb.format_exc()
            print("Invalid value entered, please try again, or enter 'q' to exit.")

