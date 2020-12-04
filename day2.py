#!/usr/bin/env python3

def main():
    valid = 0
    with open("inputs/day2.txt", "r") as f:
        for line in f:
            min, _, line = line.partition('-')
            max, _, line = line.partition(' ')
            letter, _, line = line.partition(':')

            cnt = line.count(letter)

            valid += int(min) <= cnt <= int(max)

    print(valid)


def main2():
    valid = 0
    with open("inputs/day2.txt", "r") as f:
        for line in f:
            first, _, line = line.partition('-')
            second, _, line = line.partition(' ')
            letter, _, line = line.partition(':')

            valid += (line[int(first)] == letter) ^ (line[int(second)] == letter)


    print(valid)


if __name__ == '__main__':
    main()
    main2()
