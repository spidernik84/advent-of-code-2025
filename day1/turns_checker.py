
dial = 50
clicks = 0
# turns = (10, -10, 40, -230, 400, 100, 0)
turns = (-68, -30, 48, -5, 60, -55, -1, -99, 14, -82)


def turns_checker(turn, dial, clicks):

    if turn == +100 or turn == -100:
        # no turn, count a click
        clicks += 1
        dial = (dial+turn)%100
        print("1 click")
        print(f"value {turn} +100 or -100")
        return dial, clicks

    if turn < 100 and turn > 0:
        # no turn
        dial = (dial+turn)%100
        if dial == 0:
            clicks +=1
            print(f"value {turn} <100 and >0, dial matches 0, 1 click")
        else:    
            print(f"value {turn} <100 and >0")
        return dial, clicks

    if turn > 100 or turn < -100:
        # multiple turns
        turns = abs(int(turn/100))
        clicks += turns
        dial = (dial+turn)%100
        print(f"value {turn} >100 or < -100. multiple turns: {turns} clicks. Value {dial}")
        return dial, clicks
    else:
        if dial == 0:
            if dial + turn < 0 and dial+turn > 100:
                dial = (dial+turn)%100
                # clicks += 1
                print(f"value {turn} <100, computed dial {dial}, 1 click")
            else:
                dial = (dial+turn)%100
                print(f"value {turn} <100, computed dial {dial}, 0 clicks")
        return dial, clicks


for i in turns:
    print(f"evaluating {i}, dial before calculation: {dial}")
    dial, clicks = turns_checker(i,dial,clicks)
    print(f"new dial {dial}, total clicks {clicks}\n")


print(f"clicks {clicks}")
print(f"dial {dial}")
