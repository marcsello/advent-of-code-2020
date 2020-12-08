def main():
    vote_yes_to = set()
    sum_yes_votes = 0
    with open('inputs/day6.txt', 'r') as f:
        for line in f:
            if line[0] == '\n':
                sum_yes_votes += len(vote_yes_to)
                vote_yes_to = set()

            for chr in line:
                if chr != '\n':
                    vote_yes_to.add(chr)

    sum_yes_votes += len(vote_yes_to)  # Because there is no empty line at the end of the file
    print(sum_yes_votes)


def main2():
    num_people = 0
    vote_count = {}
    sum_yes_votes = 0
    with open('inputs/day6.txt', 'r') as f:
        for line in f:
            if line[0] == '\n':
                sum_yes_votes += len(list(filter(lambda item: item[1] == num_people, vote_count.items())))
                vote_count = {}
                num_people = 0
                continue

            num_people += 1

            for chr in line:
                if chr != '\n':
                    if chr not in vote_count:
                        vote_count[chr] = 1
                    else:
                        vote_count[chr] += 1

    sum_yes_votes += len(list(filter(lambda item: item[1] == num_people, vote_count.items())))  # Because there is no empty line at the end of the file
    print(sum_yes_votes)


if __name__ == '__main__':
    main2()
