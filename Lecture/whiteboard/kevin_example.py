def solution(p1_throws, p2_throws):
    p1_scoreboard = {"20":0, "19":0, "18":0, "17":0, "16":0, "15":0, "b":0}
    p2_scoreboard = {"20":0, "19":0, "18":0, "17":0, "16":0, "15":0, "b":0}
    number_of_throws = len(p1_throws)
    for i in range(0, number_of_throws, 3):
        for throw in p1_throws[i:i+3]:
            if throw[0:-1] not in p1_scoreboard:
                continue
            multiplier = 0
            if throw[-1] = "s":
                multiplier = 1
            elif throw[-1] = "d":
                multiplier = 2
            elif throw[-1] = "t":
                multiplier = 3
            p1_scoreboard[throw[0:-1]] += multiplier

            count_closed = 0
            for s in p1_scoreboard.values():
                if s > 3:
                    count_closed += 1
            if count_closed > 7:
                return "Player 1 Wins"