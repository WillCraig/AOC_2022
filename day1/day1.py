

if __name__ == '__main__':

    # with open('day1_test.txt') as in_file:
    with open('day1_given.txt') as in_file:
        data = [line.rstrip() for line in in_file]

    calc_cal = []

    sum = 0

    # could be improved...
    while len(data) > 0:
        # went for a queueuueueue style solution.
        popped = data.pop(0)
        if popped != '':
            sum += int(popped)
        else:
            calc_cal.append(sum)
            sum = 0

    # this feels stupid too
    del data[:]

    # hate this
    calc_cal.sort(reverse=True)

    print(f"Highest Cal Count: {calc_cal[0]}\n")
    print(f"Sum of Top 3: {(calc_cal[0] + calc_cal[1] + calc_cal[2])}")
