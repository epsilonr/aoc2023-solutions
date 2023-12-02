# Author: epsilonr (https://github.com/epsilonr) - 2023-12-02

import re
import os

if __name__  == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        digits = re.findall(r'\d', line)
        sum += int(digits[0] + digits[-1])

    print(sum)