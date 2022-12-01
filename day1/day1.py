

if __name__ == '__main__':
    
    #with open('day1_test.txt') as in_file:
    with open('day1_given.txt') as in_file:
        data = [line.rstrip() for line in in_file]
    

    
    calc_cal = []
    
    sum = 0
    
    
    while len(data) > 0:
        popped = data.pop(0)
        if popped != '':
            sum += int(popped)
        else:
            calc_cal.append(sum)
            sum = 0
    
    calc_cal.sort(reverse=True)
    
    print(f"{calc_cal[0]}")
    
    print('\n')
    
    print((calc_cal[0] + calc_cal[1] + calc_cal[2]))
    
