def minion_game(string):
    # your code goes here

    score_stuart = 0
    score_kevin = 0

    for i in range(len(string)) :
        if (string[i] in "AEIOU"):
                score_kevin += len(string)-i
        else :
                score_stuart +=len(string)-i

    print("Stuart",score_stuart) if score_stuart>score_kevin else (print("Kevin", score_kevin) if score_kevin > score_stuart else print("Draw"))



if __name__ == '__main__':
    s = input()
    minion_game(s)
