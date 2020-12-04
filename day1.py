#!/usr/bin/env python3

def main():
    with open("inputs/day1.txt", "r") as f:
        numbers = list(map(int, f.readlines()))

    target = 2020

    for a in numbers:
        for b in numbers:
            for c in numbers:
                if (a + b + c) == target:
                    print(a * b * c)


def main_oneline():
    print(list(map(lambda a: a[0], filter(lambda a: any(a[0]+x == 2020 for x in a[1]), [a for a in map(lambda x: (int(x), map(int, open(
        "inputs/day1.txt", "r").readlines())), open("inputs/day1.txt", "r").readlines())])))[0] * list(map(lambda a: a[0], filter(lambda a: any(a[0] + x == 2020 for x in a[1]), [a for a in map(lambda x: (int(x), map(int, open(
        "inputs/day1.txt", "r").readlines())), open("inputs/day1.txt", "r").readlines())])))[1])


if __name__ == '__main__':
    main_oneline()
