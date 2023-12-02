# Author: epsilonr (https://github.com/epsilonr) - 2023-12-02

import re
import os

# Too dumb solution but I am lazy.

if __name__  == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("./input/input.txt") as f:
        lines = f.readlines()

    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # Structure
    # [(num, index), (num, index), ...)]
    found = []

    sum = 0
    # for line in lines:
    #     found = {}

    #     for num in nums:
    #         if num in line:
    #             found[str(nums.index(num))] = line.index(num)

    #     for i in range(0, len(line) - 1):
    #         if line[i].isdigit():
    #             found[line[i]] = i

    #     # Sort all elements in found by their value then convert to list
    #     found = list(dict(sorted(found.items(), key=lambda item: item[1])).keys())
    #     print(found)

    for line in lines:
        found = []

        for i in range(0, len(line) - 1):
            if line[i].isdigit():
                found.append((line[i], i))

        for num in nums:
            for match in re.finditer(num, line):
                found.append((str(nums.index(num)), match.start()))

        found = list(map(lambda x: x[0], sorted(found, key=lambda x: x[1])))
        sum += int(found[0] + found[-1])

    print(sum)