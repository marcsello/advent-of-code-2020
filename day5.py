def main():
    max_seat = 0
    with open('inputs/day5.txt', 'r') as f:
        for line in f:
            row = 0
            # F: lower
            # B: upper
            for i in range(7):
                if line[i] == 'B':
                    row += 2 ** (6 - i)

            col = 0
            # L: Lower
            # R: Upper
            for i in range(7, 10):
                if line[i] == 'R':
                    col += 2 ** (2 - (i - 7))

            seat = row * 8 + col

            if seat > max_seat:
                max_seat = seat

    print(max_seat)


def main2():
    occupied_seats = []
    with open('inputs/day5.txt', 'r') as f:
        for line in f:
            row = 0
            # F: lower
            # B: upper
            for i in range(7):
                if line[i] == 'B':
                    row += 2 ** (6 - i)

            col = 0
            # L: Lower
            # R: Upper
            for i in range(7, 10):
                if line[i] == 'R':
                    col += 2 ** (2 - (i - 7))

            seat_id = row * 8 + col
            occupied_seats.append(seat_id)

    occupied_seats.sort()
    last_occupied_seat_id = occupied_seats[0]
    i = 1
    while True:
        if (occupied_seats[i] - last_occupied_seat_id != 1):
            print(last_occupied_seat_id+1)
            break
        last_occupied_seat_id = occupied_seats[i]
        i += 1

if __name__ == '__main__':
    main2()
