#!/usr/bin/env python3

def sloper(r, d) -> int:
    cnt = 0
    ptr = r

    with open("inputs/day3.txt", "r") as f:
        anyad = f.readlines()

    anyad = list(map(lambda l: l.strip('\n') * 3000, anyad)) # I am highly disappointed in my skills rn

    i = d
    while i < len(anyad):

        if anyad[i][ptr] == '#':
            cnt += 1

        ptr += r

        i += d

    return cnt


def main():
    # right, down
    total = 1
    for task in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x = sloper(*task)
        print("result:", x)
        total *= x
    print("final", total)


if __name__ == '__main__':
    main()