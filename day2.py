

def play_round(ai: chr, usr: chr) -> int:
    ai_play = -1
    usr_play = -1
    
    # Switch/Match statement?
    if ai == 'A':
        ai_play = 1
    elif ai == 'B':
        ai_play = 2
    elif ai == 'C':
        ai_play = 3
    
    if usr == 'X':
        usr_play = 1
    elif usr == 'Y':
        usr_play = 2
    elif usr == 'Z':
        usr_play = 3
        
        
        
    # 0 for loss
    # 3 for draw
    # 6 for win
    # + move.
        
    if usr_play == ai_play:
        # draw
        return usr_play + 3
    elif usr_play == 1 and ai_play == 2:
        return usr_play + 0
    elif usr_play == 2 and ai_play == 1:
        return usr_play + 6
    elif usr_play == 1 and ai_play == 3:
        return usr_play + 6
    elif usr_play == 3 and ai_play == 1:
        return usr_play + 0
    elif usr_play == 2 and ai_play == 3:
        return usr_play + 0
    elif usr_play == 3 and ai_play == 2:
        return usr_play + 6
    else:
        print("ERROR")
        return -1


if __name__ == '__main__':

    
    #with open('day2_test.txt') as in_file:
    with open('day2_given.txt') as in_file:
        data = [line.rstrip() for line in in_file]


    game = 0
    
    for moves in data:
        game += play_round(moves[0], moves[2])
        
        
    print("TOTAL SCORE", game)
    


